"""
=========================================================

Trade Decision Engine (TDE)

CORE PIPELINE VALIDATION

Version 1.0

Purpose
-------
Runs the complete intelligence pipeline
from Expert Engines to Explanation.

=========================================================
"""

import yfinance as yf

from engine import ema
from engine import macd
from engine import rsi

from engine.consensus import ConsensusEngine
from engine.gatekeeper import Gatekeeper
from engine.trade_quality import TradeQualityEngine

from engine.memory import DecisionMemory
from engine.conviction import ConvictionEngine
from engine.decision import DecisionEngine
from engine.explain import ExplanationEngine


# -------------------------------------------------------
# Initialise Engines
# -------------------------------------------------------

consensus_engine = ConsensusEngine()

gatekeeper = Gatekeeper()

trade_quality_engine = TradeQualityEngine()

memory = DecisionMemory()

conviction_engine = ConvictionEngine()

decision_engine = DecisionEngine()

explanation_engine = ExplanationEngine()


SYMBOL = "RELIANCE.NS"

print()
print("=" * 70)
print("        TDE CORE INTELLIGENCE VALIDATION")
print("=" * 70)

# -------------------------------------------------------
# Download Data
# -------------------------------------------------------

print("\nDownloading Market Data...")

df = yf.download(
    SYMBOL,
    period="40d",
    interval="5m",
    progress=False
)

print(f"✓ Loaded {len(df)} candles")

print(df.columns)

# -------------------------------------------------------
# Expert Engines
# -------------------------------------------------------

ema_result = ema.calculate(df)

print("✓ EMA Engine")

macd_result = macd.calculate(df)

print("✓ MACD Engine")

rsi_result = rsi.calculate(df)

print("✓ RSI Engine")

# -------------------------------------------------------
# Consensus
# -------------------------------------------------------

consensus = consensus_engine.evaluate(
    ema_result,
    macd_result,
    rsi_result
)

print("✓ Consensus Engine")

# -------------------------------------------------------
# Gatekeeper
# -------------------------------------------------------

gate = gatekeeper.qualify(
    ema_result,
    macd_result,
    rsi_result
)

print("✓ Gatekeeper")

# -------------------------------------------------------
# Trade Quality
# -------------------------------------------------------

trade = trade_quality_engine.evaluate(
    ema_result,
    macd_result,
    rsi_result
)

print("✓ Trade Quality")

# -------------------------------------------------------
# Memory
# -------------------------------------------------------

# Simulate history so Conviction has something to analyse

sample_consensus = [
    74,
    77,
    80,
    84,
    87,
    consensus["consensus"]
]

for score in sample_consensus:

    memory.record(

        SYMBOL,

        consensus=score,

        trade_score=trade["score"],

        status=trade["status"],

        reason="Pipeline Test"

    )

print("✓ Decision Memory")

# -------------------------------------------------------
# Conviction
# -------------------------------------------------------

history = memory.history(SYMBOL)

conviction = conviction_engine.evaluate(history)

print("✓ Conviction Engine")

# -------------------------------------------------------
# Decision
# -------------------------------------------------------

decision = decision_engine.evaluate(conviction)

print("✓ Decision Engine")

# -------------------------------------------------------
# Explanation
# -------------------------------------------------------

explanation = explanation_engine.explain(

    ema_result,

    macd_result,

    rsi_result,

    consensus["consensus"],

    conviction,

    decision

)

print("✓ Explanation Engine")

# -------------------------------------------------------
# Report
# -------------------------------------------------------

print()
print("=" * 70)
print("FINAL REPORT")
print("=" * 70)

print()

print(f"Consensus    : {consensus['consensus']}")
print(f"Agreement    : {consensus['agreement']}")

print()

print(f"Gatekeeper   : {gate['status']}")

print()

print(f"Trade Score  : {trade['score']}")
print(f"Trade Grade  : {trade['grade']}")
print(f"Trade Status : {trade['status']}")

print()

print(f"Decision     : {decision['state']}")
print(f"Confidence   : {decision['confidence']}")

print()

print("-" * 70)
print("Explanation")
print("-" * 70)

print(explanation)

print()
print("=" * 70)
print("TDE CORE INTELLIGENCE PIPELINE PASSED")
print("=" * 70)
