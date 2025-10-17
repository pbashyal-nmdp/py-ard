# -*- coding: utf-8 -*-

import pytest
from unittest.mock import Mock
from pyard.strategies.default_strategy import DefaultStrategy
from pyard.exceptions import InvalidAlleleError


def test_default_strategy_p_suffix():
    mock_ard = Mock()
    mock_ard.ars_mappings.p_group.values.return_value = ["A*01:01P"]

    strategy = DefaultStrategy(mock_ard)
    result = strategy.reduce("A*01:01P")
    assert result == "A*01:01P"


def test_default_strategy_g_suffix():
    mock_ard = Mock()
    mock_ard.ars_mappings.g_group.values.return_value = ["A*01:01G"]

    strategy = DefaultStrategy(mock_ard)
    result = strategy.reduce("A*01:01G")
    assert result == "A*01:01G"


def test_default_strategy_valid_allele():
    mock_ard = Mock()
    mock_ard._is_allele_in_db.return_value = True

    strategy = DefaultStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01"


def test_default_strategy_invalid_allele():
    mock_ard = Mock()
    mock_ard.ars_mappings.p_group.values.return_value = []
    mock_ard.ars_mappings.g_group.values.return_value = []
    mock_ard._is_allele_in_db.return_value = False

    strategy = DefaultStrategy(mock_ard)
    with pytest.raises(InvalidAlleleError):
        strategy.reduce("INVALID*01:01")
