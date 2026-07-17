"""
=========================================================

Trade Decision Engine (TDE)

Explanation Engine Test Bench

Purpose
-------
Tests the Explanation Engine.

=========================================================
"""

from engine.explain import ExplanationEngine


explainer = ExplanationEngine()


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def run_test(test_name):

    print()
    print("=" * 80)
    print(test_name)
    print("=" * 80)

    # -----------------------------------------------------
    # Dummy EMA Expert
    # -----------------------------------------------------

    ema = {

        "decision": {

            "signal": "Bullish",

            "score": 92

        }

    }

    # -----------------------------------------------------
    # Dummy MACD Expert
    # -----------------------------------------------------

    macd = {

        "decision": {

            "signal": "Improving",

            "score": 89

        }

    }

    # -----------------------------------------------------
    # Dummy RSI Expert
    # -----------------------------------------------------

    rsi = {

        "decision": {

            "signal": "Healthy",

            "score": 84

        }

    }

    # -----------------------------------------------------
    # Consensus
    # -----------------------------------------------------

    consensus = 91

    # -----------------------------------------------------
    # Conviction
    # -----------------------------------------------------

    conviction = {

        "immediate": "Improving",

        "context": "Persistent Improvement",

        "persistence": 6,

        "velocity": "Moderate"

    }

    # -----------------------------------------------------
    # Decision
    # -----------------------------------------------------

    decision = {

        "state": "COMMIT",

        "confidence": "High",

        "recommendation":

            "Strong conviction. Stay with the trade."

    }

    # -----------------------------------------------------
    # Generate Explanation
    # -----------------------------------------------------

    explanation = explainer.explain(

        ema,

        macd,

        rsi,

        consensus,

        conviction,

        decision

    )

    print(explanation)

    print("=" * 80)


# =========================================================
# Run Test
# =========================================================

run_test(

    "TEST 1 : Complete Trade Explanation"

)

print()

print("=" * 80)
print("Explanation Engine Test Complete")
print("=" * 80)
