# -*- coding: utf-8 -*-

from unittest.mock import Mock, patch
from pyard.strategies.s_strategy import SStrategy


def test_s_strategy_two_field_allele():
    mock_ard = Mock()
    mock_ard._redux_allele.return_value = "A*01:01"
    mock_ard.db_connection = Mock()
    mock_ard.smart_sort_comparator = Mock()

    with patch("pyard.strategies.s_strategy.is_2_field_allele", return_value=True):
        with patch(
            "pyard.strategies.s_strategy.db.find_serology_for_allele",
            return_value={"A1": "A*01:01/A*01:02"},
        ):
            strategy = SStrategy(mock_ard)
            result = strategy.reduce("A*01:01")
            assert result == "A1"


def test_s_strategy_non_two_field_allele():
    mock_ard = Mock()
    mock_ard.db_connection = Mock()
    mock_ard.smart_sort_comparator = Mock()

    with patch("pyard.strategies.s_strategy.is_2_field_allele", return_value=False):
        with patch(
            "pyard.strategies.s_strategy.db.find_serology_for_allele",
            return_value={"A1": "A*01:01:01/A*01:02:01"},
        ):
            strategy = SStrategy(mock_ard)
            result = strategy.reduce("A*01:01:01")
            assert result == "A1"


def test_s_strategy_multiple_serology():
    mock_ard = Mock()
    mock_ard.db_connection = Mock()
    mock_ard.smart_sort_comparator = lambda x, y: 0

    with patch("pyard.strategies.s_strategy.is_2_field_allele", return_value=False):
        with patch(
            "pyard.strategies.s_strategy.db.find_serology_for_allele",
            return_value={"A1": "A*01:01:01", "A2": "A*01:01:01"},
        ):
            strategy = SStrategy(mock_ard)
            result = strategy.reduce("A*01:01:01")
            assert "A1" in result and "A2" in result
