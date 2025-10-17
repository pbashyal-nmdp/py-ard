# -*- coding: utf-8 -*-

import sqlite3
import threading
from contextlib import contextmanager
from typing import Optional
from queue import Queue, Empty


class ConnectionPool:
    """Thread-safe SQLite connection pool for improved performance"""

    def __init__(
        self, database_path: str, max_connections: int = 5, read_only: bool = True
    ):
        self.database_path = database_path
        self.max_connections = max_connections
        self.read_only = read_only
        self._pool = Queue(maxsize=max_connections)
        self._lock = threading.Lock()
        self._created_connections = 0

        # Pre-populate pool with initial connections
        self._initialize_pool()

    def _initialize_pool(self):
        """Initialize the connection pool with connections"""
        for _ in range(min(2, self.max_connections)):  # Start with 2 connections
            conn = self._create_connection()
            if conn:
                self._pool.put(conn)

    def _create_connection(self) -> Optional[sqlite3.Connection]:
        """Create a new database connection"""
        try:
            if self.read_only:
                conn = sqlite3.connect(f"file:{self.database_path}?mode=ro", uri=True)
            else:
                conn = sqlite3.connect(self.database_path)
                conn.execute("PRAGMA journal_mode=WAL")

            # Configure connection for better performance
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.execute("PRAGMA cache_size=10000")
            conn.execute("PRAGMA temp_store=MEMORY")

            with self._lock:
                self._created_connections += 1

            return conn
        except sqlite3.Error as e:
            return None

    @contextmanager
    def get_connection(self):
        """Get a connection from the pool (context manager)"""
        import traceback

        traceback.print_stack()

        conn = None
        try:
            # Try to get existing connection from pool
            try:
                conn = self._pool.get_nowait()
            except Empty:
                # Create new connection if pool is empty and under limit
                with self._lock:
                    if self._created_connections < self.max_connections:
                        conn = self._create_connection()

                if conn is None:
                    # Wait for a connection to become available
                    conn = self._pool.get(timeout=30)

            yield conn

        finally:
            # Return connection to pool
            if conn:
                try:
                    # Test if connection is still valid
                    conn.execute("SELECT 1")
                    self._pool.put_nowait(conn)
                except (sqlite3.Error, Exception):
                    # Connection is broken, don't return to pool
                    with self._lock:
                        self._created_connections -= 1

    def close_all(self):
        """Close all connections in the pool"""
        while not self._pool.empty():
            try:
                conn = self._pool.get_nowait()
                conn.close()
            except (Empty, sqlite3.Error):
                break

        with self._lock:
            self._created_connections = 0
