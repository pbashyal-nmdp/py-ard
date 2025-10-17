# -*- coding: utf-8 -*-

from unittest.mock import Mock, patch
from pyard.strategies.u2_strategy import U2Strategy


def test_u2_strategy_two_field_allele():
    mock_ard = Mock()

    strategy = U2Strategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "A*01:01"


def test_u2_strategy_unambiguous_reduction():
    mock_ard = Mock()
    mock_ard._is_allele_in_db.return_value = True

    with patch(
        "pyard.strategies.u2_strategy.get_n_field_allele", return_value="A*01:01"
    ):
        strategy = U2Strategy(mock_ard)
        result = strategy.reduce("A*01:01:01")
        assert result == "A*01:01"


def test_u2_strategy_ambiguous_reduction():
    mock_ard = Mock()
    mock_ard._is_allele_in_db.return_value = False
    mock_ard._redux_allele.return_value = "A*01:01"

    with patch(
        "pyard.strategies.u2_strategy.get_n_field_allele", return_value="A*01:01"
    ):
        strategy = U2Strategy(mock_ard)
        result = strategy.reduce("A*01:01:01")
        assert result == "A*01:01"
