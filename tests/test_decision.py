"""
=========================================================

Trade Decision Engine (TDE)

Decision Engine Test Bench

Purpose
-------
Tests the Decision Engine using simulated
Conviction Engine outputs.

=========================================================
"""

from engine.decision import DecisionEngine


decision = DecisionEngine()


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def run_test(test_name, conviction):

    print()
    print("=" * 70)
    print(test_name)
    print("=" * 70)

    result = decision.evaluate(conviction)

    print("\nConviction Input\n")

    for key, value in conviction.items():

        print(f"{key:15}: {value}")

    print("\nDecision Output\n")

    print(f"State          : {result['state']}")
    print(f"Confidence     : {result['confidence']}")
    print(f"Recommendation : {result['recommendation']}")
    print(f"Reason         : {result['reason']}")

    print("=" * 70)


# =========================================================
# TEST 1
# Strong Bullish
# =========================================================

run_test(

    "TEST 1 : Strong Bullish Conviction",

    {

        "immediate": "Improving",

        "context": "Persistent Improvement",

        "velocity": "Moderate",

        "persistence": 6

    }

)

# =========================================================
# TEST 2
# Early Improvement
# =========================================================

run_test(

    "TEST 2 : Early Improvement",

    {

        "immediate": "Improving",

        "context": "Stable",

        "velocity": "Slow",

        "persistence": 2

    }

)

# =========================================================
# TEST 3
# Stable Trade
# =========================================================

run_test(

    "TEST 3 : Stable Trade",

    {

        "immediate": "Stable",

        "context": "Stable",

        "velocity": "Slow",

        "persistence": 5

    }

)

# =========================================================
# TEST 4
# Weakening Slowly
# =========================================================

run_test(

    "TEST 4 : Weakening Slowly",

    {

        "immediate": "Weakening",

        "context": "Persistent Weakening",

        "velocity": "Moderate",

        "persistence": 4

    }

)

# =========================================================
# TEST 5
# Fast Collapse
# =========================================================

run_test(

    "TEST 5 : Fast Collapse",

    {

        "immediate": "Weakening",

        "context": "Persistent Weakening",

        "velocity": "Fast",

        "persistence": 6

    }

)

# =========================================================
# TEST 6
# Mixed Signals
# =========================================================

run_test(

    "TEST 6 : Mixed Signals",

    {

        "immediate": "Improving",

        "context": "Mixed",

        "velocity": "Moderate",

        "persistence": 2

    }

)

# =========================================================
# TEST 7
# Weakening but Stable Context
# =========================================================

run_test(

    "TEST 7 : Minor Weakness",

    {

        "immediate": "Weakening",

        "context": "Stable",

        "velocity": "Slow",

        "persistence": 1

    }

)

# =========================================================
# TEST 8
# No History
# =========================================================

run_test(

    "TEST 8 : Insufficient Conviction",

    {

        "immediate": "Unknown",

        "context": "Insufficient History",

        "velocity": "Unknown",

        "persistence": 0

    }

)

print()
print("=" * 70)
print("All Decision Engine Tests Completed")
print("=" * 70)
