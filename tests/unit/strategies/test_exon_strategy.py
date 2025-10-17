# -*- coding: utf-8 -*-

from unittest.mock import Mock, patch
from pyard.strategies.exon_strategy import ExonStrategy


def test_exon_strategy_with_mapping():
    mock_ard = Mock()
    mock_ard.ars_mappings.exon_group = {"A*01:01:01:01": "A*01:01:01"}

    strategy = ExonStrategy(mock_ard)
    result = strategy.reduce("A*01:01:01:01")
    assert result == "A*01:01:01"


def test_exon_strategy_with_expression_char():
    mock_ard = Mock()
    mock_ard.ars_mappings.exon_group = {"A*01:01:01:01N": "A*01:01:01"}
    mock_ard.is_shortnull.return_value = True

    with patch("pyard.strategies.exon_strategy.expression_chars", ["N"]):
        strategy = ExonStrategy(mock_ard)
        result = strategy.reduce("A*01:01:01:01N")
        assert result == "A*01:01:01N"


def test_exon_strategy_w_redux_recursion():
    mock_ard = Mock()
    mock_ard.ars_mappings.exon_group = {}
    mock_ard.redux.side_effect = ["A*01:01:01:01", "A*01:01:01"]

    strategy = ExonStrategy(mock_ard)
    result = strategy.reduce("A*01:XX")
    assert result == "A*01:01:01"


def test_exon_strategy_no_recursion():
    mock_ard = Mock()
    mock_ard.ars_mappings.exon_group = {}
    mock_ard.redux.return_value = "A*01:01"

    strategy = ExonStrategy(mock_ard)
    result = strategy.reduce("A*01:XX")
    assert result == "A*01:XX"
