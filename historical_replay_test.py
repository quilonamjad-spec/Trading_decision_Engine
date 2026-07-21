from datetime import datetime
import market_data
import ema
import macd
import rsi
import trade_quality


def analyze_snapshot(ticker, analysis_time):
    """
    Runs the complete engine up to the given time.
    """

    df = data.market_data.get_data_until(ticker, analysis_time)

    ema_result = ema.calculate(df)
    macd_result = macd.calculate(df)
    rsi_result = rsi.calculate(df)

    result = trade_quality.evaluate(
        ema_result,
        macd_result,
        rsi_result
    )

    return result


# -----------------------------------------
# USER INPUT
# -----------------------------------------

ticker = "SBIN.NS"

market_open = datetime(2026, 7, 21, 9, 15)

analysis_time = datetime(2026, 7, 21, 11, 5)

# -----------------------------------------
# ANALYSIS
# -----------------------------------------

opening = analyze_snapshot(
    ticker,
    market_open
)

current = analyze_snapshot(
    ticker,
    analysis_time
)

# -----------------------------------------
# DISPLAY
# -----------------------------------------

print("\n========== OPEN ==========")
print(opening)

print("\n========== CURRENT ==========")
print(current)

print("\n========== CHANGE ==========")

print(
    "Trade Health :",
    opening["score"],
    "->",
    current["score"]
)

print(
    "Consensus :",
    opening["consensus"],
    "->",
    current["consensus"]
)

print(
    "Confidence :",
    opening["confidence"],
    "->",
    current["confidence"]
)

print(
    "Direction :",
    current["direction"]
)
