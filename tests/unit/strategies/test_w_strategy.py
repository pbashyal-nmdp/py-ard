# -*- coding: utf-8 -*-

from unittest.mock import Mock
from pyard.strategies.w_strategy import WStrategy


def test_w_strategy_who_allele():
    mock_ard = Mock()
    mock_ard._is_who_allele.return_value = True

    strategy = WStrategy(mock_ard)
    result = strategy.reduce("A*01:01:01:01")
    assert result == "A*01:01:01:01"


def test_w_strategy_with_who_group():
    mock_ard = Mock()
    mock_ard._is_who_allele.return_value = False
    mock_ard.code_mappings.who_group = {"A*01:XX": ["A*01:01", "A*01:02"]}
    mock_ard.redux.return_value = "A*01:01:01/A*01:02:01"

    strategy = WStrategy(mock_ard)
    result = strategy.reduce("A*01:XX")
    assert result == "A*01:01:01/A*01:02:01"


def test_w_strategy_no_mapping():
    mock_ard = Mock()
    mock_ard._is_who_allele.return_value = False
    mock_ard.code_mappings.who_group = {}

    strategy = WStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01"
