# -*- coding: utf-8 -*-

from unittest.mock import Mock
from pyard.strategies.p_strategy import PGroupStrategy


def test_p_strategy_with_data_repository():
    mock_ard = Mock()
    mock_ard.data_repository.get_p_group_mapping.return_value = "A*01:01P"

    strategy = PGroupStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01P"


def test_p_strategy_with_p_group_mapping():
    mock_ard = Mock()
    mock_ard.data_repository = None
    mock_ard.ars_mappings.p_group = {"A*01:01": "A*01:01P"}

    strategy = PGroupStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01P"


def test_p_strategy_fallback_to_super():
    mock_ard = Mock()
    mock_ard.data_repository = None
    mock_ard.ars_mappings.p_group = {}
    mock_ard._is_allele_in_db.return_value = True

    strategy = PGroupStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01"
