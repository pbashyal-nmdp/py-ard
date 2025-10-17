# -*- coding: utf-8 -*-

from unittest.mock import Mock
from pyard.strategies.strategy_factory import StrategyFactory
from pyard.strategies.g_strategy import GGroupStrategy
from pyard.strategies.p_strategy import PGroupStrategy
from pyard.strategies.lg_strategy import LGStrategy, LGXStrategy
from pyard.strategies.w_strategy import WStrategy
from pyard.strategies.exon_strategy import ExonStrategy
from pyard.strategies.u2_strategy import U2Strategy
from pyard.strategies.s_strategy import SStrategy
from pyard.strategies.default_strategy import DefaultStrategy


def test_strategy_factory_initialization():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    assert factory.ard == mock_ard
    assert len(factory._strategies) == 9


def test_strategy_factory_get_g_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("G")
    assert isinstance(strategy, GGroupStrategy)


def test_strategy_factory_get_p_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("P")
    assert isinstance(strategy, PGroupStrategy)


def test_strategy_factory_get_lg_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("lg")
    assert isinstance(strategy, LGStrategy)


def test_strategy_factory_get_lgx_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("lgx")
    assert isinstance(strategy, LGXStrategy)


def test_strategy_factory_get_w_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("W")
    assert isinstance(strategy, WStrategy)


def test_strategy_factory_get_exon_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("exon")
    assert isinstance(strategy, ExonStrategy)


def test_strategy_factory_get_u2_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("U2")
    assert isinstance(strategy, U2Strategy)


def test_strategy_factory_get_s_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("S")
    assert isinstance(strategy, SStrategy)


def test_strategy_factory_get_default_strategy():
    mock_ard = Mock()
    factory = StrategyFactory(mock_ard)
    strategy = factory.get_strategy("unknown")
    assert isinstance(strategy, DefaultStrategy)
