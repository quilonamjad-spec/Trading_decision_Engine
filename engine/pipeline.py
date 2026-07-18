"""
pipeline.py

Trade Decision Engine (TDE)
Pipeline Orchestrator

Runs the complete intelligence pipeline.
"""

import engine.ema as ema
import engine.macd as macd
import engine.rsi as rsi

from engine.consensus import ConsensusEngine
from engine.gatekeeper import Gatekeeper
from engine.trade_quality import TradeQualityEngine
from engine.memory import DecisionMemory
from engine.conviction import ConvictionEngine
from engine.decision import DecisionEngine
from engine.explain import ExplanationEngine


class Pipeline:

    def __init__(self, verbose=False):

        self.verbose = verbose

        self.consensus = ConsensusEngine()
        self.gatekeeper = Gatekeeper()
        self.trade_quality = TradeQualityEngine()

        self.memory = DecisionMemory()
        self.conviction = ConvictionEngine()
        self.decision = DecisionEngine()
        self.explainer = ExplanationEngine()

    # -------------------------------------------------

    def log(self, message):
        if self.verbose:
            print(message)

    # -------------------------------------------------

    def evaluate(self, symbol, df):

        self.log(f"Starting TDE Pipeline : {symbol}")

        # -----------------------------
        # Expert Engines
        # -----------------------------

        self.log("Running EMA...")
        ema_result = ema.calculate(df)

        self.log("Running MACD...")
        macd_result = macd.calculate(df)

        self.log("Running RSI...")
        rsi_result = rsi.calculate(df)

        # -----------------------------
        # Consensus
        # -----------------------------

        self.log("Running Consensus...")
        consensus_result = self.consensus.evaluate(
            ema_result,
            macd_result,
            rsi_result
        )

        # -----------------------------
        # Gatekeeper
        # -----------------------------

        self.log("Running Gatekeeper...")
        gatekeeper_result = self.gatekeeper.qualify(
            ema_result,
            macd_result,
            rsi_result
        )

        # -----------------------------
        # Trade Quality
        # -----------------------------

        self.log("Running Trade Quality...")
        trade_quality = self.trade_quality.evaluate(
            ema_result,
            macd_result,
            rsi_result
        )

        # -----------------------------
        # Memory
        # -----------------------------

        self.log("Updating Memory...")

        self.memory.record(
            symbol=symbol,
            consensus=consensus_result["consensus"],
            trade_score=trade_quality["score"],
            status=trade_quality["status"],
            reason=consensus_result["reason"]
        )

        history = self.memory.history(symbol)

        # -----------------------------
        # Conviction
        # -----------------------------

        self.log("Running Conviction...")
        conviction = self.conviction.evaluate(history)

        # -----------------------------
        # Decision
        # -----------------------------

        self.log("Running Decision...")
        decision = self.decision.evaluate(conviction)

        # -----------------------------
        # Explanation
        # -----------------------------

        self.log("Building Explanation...")

        explanation = self.explainer.explain(
            ema_result,
            macd_result,
            rsi_result,
            consensus_result["consensus"],
            conviction,
            decision
        )

        self.log("Pipeline Complete.")

        return {

            "symbol": symbol,

            "ema": ema_result,

            "macd": macd_result,

            "rsi": rsi_result,

            "consensus": consensus_result,

            "gatekeeper": gatekeeper_result,

            "trade_quality": trade_quality,

            "history": history,

            "conviction": conviction,

            "decision": decision,

            "explanation": explanation

        }

