"""
=========================================================

Trade Decision Engine (TDE)

Conviction Engine Test Bench

Purpose
-------
Tests the Conviction Engine using simulated
decision histories.

=========================================================
"""

from engine.memory import DecisionMemory
from engine.conviction import ConvictionEngine


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def run_test(test_name, scores):

    print("\n")
    print("=" * 70)
    print(test_name)
    print("=" * 70)

    memory = DecisionMemory()
    conviction = ConvictionEngine()

    for score in scores:

        memory.record(

            symbol="TEST",

            consensus=score,

            trade_score=score,

            status="READY",

            reason="Simulation"

        )

    history = memory.history("TEST")

    result = conviction.evaluate(history)

    print("Scores : ", scores)
    print()

    print("Previous     :", result["previous"])
    print("Current      :", result["current"])
    print("Average      :", result["average"])
    
    print()
    
    print("Immediate    :", result["immediate"])
    print("Context      :", result["context"])
    print("Persistence  :", result["persistence"])
    print("Velocity     :", result["velocity"])
    
    print()
    
    print("Change       :", result["change"])
    print("Message      :", result["message"])

    print("=" * 70)


# =========================================================
# Test Cases
# =========================================================

# 1. Strong Downtrend
run_test(

    "TEST 1 : Gradual Weakening",

    [96, 94, 91, 88, 85, 82]

)

# ---------------------------------------------------------

# 2. Strong Uptrend
run_test(

    "TEST 2 : Increasing Conviction",

    [82, 85, 88, 91, 94, 96]

)

# ---------------------------------------------------------

# 3. Sideways Confidence
run_test(

    "TEST 3 : Stable Conviction",

    [90, 91, 90, 91, 90, 91]

)

# ---------------------------------------------------------

# 4. One Bad Candle
run_test(

    "TEST 4 : Sudden Dip",

    [96, 96, 96, 95, 96, 90]

)

# ---------------------------------------------------------

# 5. Recovery

run_test(

    "TEST 5 : Recovery",

    [96, 92, 88, 90, 93, 96]

)

# ---------------------------------------------------------

# 6. Collapse

run_test(

    "TEST 6 : Conviction Collapse",

    [96, 90, 82, 70, 60, 48]

)

# ---------------------------------------------------------

# 7. Slow Recovery

run_test(

    "TEST 7 : Slow Recovery",

    [72, 74, 75, 77, 80, 84]

)

# ---------------------------------------------------------

# 8. Flat High Confidence

run_test(

    "TEST 8 : Flat High Confidence",

    [96, 96, 95, 96, 95, 96]

)

# ---------------------------------------------------------

print("\n")
print("=" * 70)
print("All Conviction Tests Completed")
print("=" * 70)
