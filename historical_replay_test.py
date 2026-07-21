from datetime import datetime
from data.market_data import MarketDataEngine
from engine import ema
from engine import macd
from engine import rsi
from engine import trade_quality
from engine.trade_quality import TradeQualityEngine




market = MarketDataEngine()
trade_engine = TradeQualityEngine()


def analyze_snapshot(ticker, analysis_time):

    df = market.get_data_until(
        ticker,
        analysis_time
    )
    ema_result = ema.calculate(df)
    macd_result = macd.calculate(df)
    rsi_result = rsi.calculate(df)

    result = trade_engine.evaluate(
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
