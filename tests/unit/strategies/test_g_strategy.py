# -*- coding: utf-8 -*-

from unittest.mock import Mock
from pyard.strategies.g_strategy import GGroupStrategy


def test_g_strategy_with_data_repository():
    mock_ard = Mock()
    mock_ard.data_repository.get_g_group_mapping.return_value = "A*01:01:01G"

    strategy = GGroupStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01:01G"


def test_g_strategy_with_dup_g():
    mock_ard = Mock()
    mock_ard.data_repository = None
    mock_ard.ars_mappings.g_group = {"A*01:01": "A*01:01:01G"}
    mock_ard.ars_mappings.dup_g = {"A*01:01": "A*01:01:01G"}

    strategy = GGroupStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01:01G"


def test_g_strategy_without_dup_g():
    mock_ard = Mock()
    mock_ard.data_repository = None
    mock_ard.ars_mappings.g_group = {"A*01:01": "A*01:01:01G"}
    mock_ard.ars_mappings.dup_g = {}

    strategy = GGroupStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01:01G"


def test_g_strategy_fallback_to_super():
    mock_ard = Mock()
    mock_ard.data_repository = None
    mock_ard.ars_mappings.g_group = {}
    mock_ard._is_allele_in_db.return_value = True

    strategy = GGroupStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01"
