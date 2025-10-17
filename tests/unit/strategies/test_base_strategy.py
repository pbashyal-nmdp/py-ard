# -*- coding: utf-8 -*-

import pytest
from unittest.mock import Mock
from pyard.strategies.base_strategy import ReductionStrategy


class ConcreteStrategy(ReductionStrategy):
    def reduce(self, allele: str) -> str:
        return f"reduced_{allele}"


def test_base_strategy_initialization():
    mock_ard = Mock()
    strategy = ConcreteStrategy(mock_ard)
    assert strategy.ard == mock_ard


def test_base_strategy_abstract_method():
    mock_ard = Mock()
    with pytest.raises(TypeError):
        ReductionStrategy(mock_ard)


def test_concrete_strategy_reduce():
    mock_ard = Mock()
    strategy = ConcreteStrategy(mock_ard)
    result = strategy.reduce("A*01:01")
    assert result == "reduced_A*01:01"
