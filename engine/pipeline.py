"""
pipeline.py

TDE Intelligence Pipeline

Runs the complete Trade Decision Engine from
market data to final explanation.
"""

from engine.ema import EMAEngine
from engine.macd import MACDEngine
from engine.rsi import RSIEngine

from engine.consensus import ConsensusEngine
from engine.gatekeeper import Gatekeeper
from engine.trade_quality import TradeQualityEngine

from engine.memory import DecisionMemory
from engine.conviction import ConvictionEngine
from engine.decision import DecisionEngine
from engine.explain import ExplanationEngine


class Pipeline:

    def __init__(self):

        # Expert Engines
        self.ema = EMAEngine()
        self.macd = MACDEngine()
        self.rsi = RSIEngine()

        # Decision Engines
        self.consensus = ConsensusEngine()
        self.gatekeeper = Gatekeeper()
        self.trade_quality = TradeQualityEngine()

        # Intelligence Layer
        self.memory = DecisionMemory()
        self.conviction = ConvictionEngine()
        self.decision = DecisionEngine()

        # Explainability
        self.explainer = ExplanationEngine()
