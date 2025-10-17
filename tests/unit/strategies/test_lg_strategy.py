# -*- coding: utf-8 -*-

from unittest.mock import Mock
from pyard.strategies.lg_strategy import LGXStrategy, LGStrategy


def test_lgx_strategy_with_mapping():
    mock_ard = Mock()
    mock_ard.ars_mappings.lgx_group = {"A*01:01:01": "A*01:01"}

    strategy = LGXStrategy(mock_ard)
    result = strategy.reduce("A*01:01:01")
    assert result == "A*01:01"


def test_lgx_strategy_without_mapping():
    mock_ard = Mock()
    mock_ard.ars_mappings.lgx_group = {}

    strategy = LGXStrategy(mock_ard)
    result = strategy.reduce("A*01:01:01:01")
    assert result == "A*01:01"


def test_lg_strategy_with_g_suffix():
    mock_ard = Mock()
    mock_ard.ars_mappings.lgx_group = {"A*01:01:01": "A*01:01"}
    mock_ard._config = {"ARS_as_lg": False}

    strategy = LGStrategy(mock_ard)
    result = strategy.reduce("A*01:01:01")
    assert result == "A*01:01g"


def test_lg_strategy_with_ars_suffix():
    mock_ard = Mock()
    mock_ard.ars_mappings.lgx_group = {"A*01:01:01": "A*01:01"}
    mock_ard._config = {"ARS_as_lg": True}

    strategy = LGStrategy(mock_ard)
    result = strategy.reduce("A*01:01:01")
    assert result == "A*01:01ARS"


def test_lg_strategy_with_slash_delimited():
    mock_ard = Mock()
    mock_ard.ars_mappings.lgx_group = {}
    mock_ard._config = {"ARS_as_lg": False}

    strategy = LGStrategy(mock_ard)
    result = strategy.reduce("A*01:01:01/A*01:02:01")
    assert result == "A*01:01g/A*01:02g"
