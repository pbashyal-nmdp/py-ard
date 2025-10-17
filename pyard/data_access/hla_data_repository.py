# -*- coding: utf-8 -*-

import functools
from typing import List, Dict, Set, Optional
from .connection_pool import ConnectionPool
from .. import db


class HLADataRepository:
    """Centralized data access layer for HLA database operations"""

    def __init__(self, connection_pool: ConnectionPool):
        self.connection_pool = connection_pool

        # Cache frequently accessed data
        self._g_group_cache = {}
        self._p_group_cache = {}
        self._mac_cache = {}
        self._serology_cache = {}
        self._cwd_cache = {}

    @functools.lru_cache(maxsize=1000)
    def get_g_group_mapping(self, allele: str) -> Optional[str]:
        """Get G group mapping for allele"""
        if allele in self._g_group_cache:
            return self._g_group_cache[allele]

        with self.connection_pool.get_connection() as conn:
            cursor = conn.execute(
                "SELECT allele FROM g_group WHERE allele = ?", (allele,)
            )
            result = cursor.fetchone()
            mapping = result[0] if result else None
            self._g_group_cache[allele] = mapping
            return mapping

    @functools.lru_cache(maxsize=1000)
    def get_p_group_mapping(self, allele: str) -> Optional[str]:
        """Get P group mapping for allele"""
        if allele in self._p_group_cache:
            return self._p_group_cache[allele]

        with self.connection_pool.get_connection() as conn:
            cursor = conn.execute(
                "SELECT allele FROM p_group WHERE allele = ?", (allele,)
            )
            result = cursor.fetchone()
            mapping = result[0] if result else None
            self._p_group_cache[allele] = mapping
            return mapping

    @functools.lru_cache(maxsize=500)
    def get_mac_alleles(self, code: str) -> List[str]:
        """Get alleles for MAC code"""
        if code in self._mac_cache:
            return self._mac_cache[code]

        with self.connection_pool.get_connection() as conn:
            alleles = db.mac_code_to_alleles(conn, code)
            self._mac_cache[code] = alleles
            return alleles

    @functools.lru_cache(maxsize=500)
    def get_serology_alleles(self, serology: str) -> List[str]:
        """Get alleles for serology"""
        if serology in self._serology_cache:
            return self._serology_cache[serology]

        with self.connection_pool.get_connection() as conn:
            alleles = db.serology_to_alleles(conn, serology)
            self._serology_cache[serology] = alleles
            return alleles

    @functools.lru_cache(maxsize=100)
    def get_cwd_alleles(self, locus: str) -> Set[str]:
        """Get CWD alleles for locus"""
        if locus in self._cwd_cache:
            return self._cwd_cache[locus]

        with self.connection_pool.get_connection() as conn:
            cwd_alleles = db.load_cwd(conn, locus)
            self._cwd_cache[locus] = cwd_alleles
            return cwd_alleles

    @functools.lru_cache(maxsize=200)
    def find_serology_for_allele(
        self, allele: str, table_name: str = "allele_list"
    ) -> Dict[str, str]:
        """Find serology mapping for allele"""
        with self.connection_pool.get_connection() as conn:
            return db.find_serology_for_allele(conn, allele, table_name)

    @functools.lru_cache(maxsize=100)
    def find_xx_for_serology(self, serology: str) -> str:
        """Find XX code for serology"""
        with self.connection_pool.get_connection() as conn:
            return db.find_xx_for_serology(conn, serology)

    @functools.lru_cache(maxsize=200)
    def alleles_to_mac_code(self, alleles: str) -> Optional[str]:
        """Find MAC code for allele list"""
        with self.connection_pool.get_connection() as conn:
            return db.alleles_to_mac_code(conn, alleles)

    @functools.lru_cache(maxsize=100)
    def similar_alleles(self, prefix: str) -> Set[str]:
        """Find similar alleles with prefix"""
        with self.connection_pool.get_connection() as conn:
            return db.similar_alleles(conn, prefix)

    @functools.lru_cache(maxsize=100)
    def similar_mac(self, prefix: str) -> Set[str]:
        """Find similar MAC codes with prefix"""
        with self.connection_pool.get_connection() as conn:
            return db.similar_mac(conn, prefix)

    @functools.lru_cache(maxsize=50)
    def v2_to_v3_allele(self, v2_allele: str) -> Optional[str]:
        """Convert V2 allele to V3"""
        with self.connection_pool.get_connection() as conn:
            return db.v2_to_v3_allele(conn, v2_allele)

    def get_db_version(self) -> int:
        """Get database version"""
        with self.connection_pool.get_connection() as conn:
            return db.get_user_version(conn)

    def clear_cache(self):
        """Clear all caches"""
        self._g_group_cache.clear()
        self._p_group_cache.clear()
        self._mac_cache.clear()
        self._serology_cache.clear()
        self._cwd_cache.clear()

        # Clear LRU caches
        self.get_g_group_mapping.cache_clear()
        self.get_p_group_mapping.cache_clear()
        self.get_mac_alleles.cache_clear()
        self.get_serology_alleles.cache_clear()
        self.get_cwd_alleles.cache_clear()
        self.find_serology_for_allele.cache_clear()
        self.find_xx_for_serology.cache_clear()
        self.alleles_to_mac_code.cache_clear()
        self.similar_alleles.cache_clear()
        self.similar_mac.cache_clear()
        self.v2_to_v3_allele.cache_clear()

    def close(self):
        """Close the connection pool"""
        self.connection_pool.close_all()
