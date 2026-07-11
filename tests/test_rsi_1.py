"""
====================================================
Trade Decision Engine (TDE)

RSI Engine Test
====================================================
"""

from data.market_data import MarketDataEngine
from indicators import rsi

# ----------------------------------
# Download Market Data
# ----------------------------------

market = MarketDataEngine()

market_data = market.download_watchlist()

df = market_data["SBIN.NS"]

# ----------------------------------
# Run RSI Engine
# ----------------------------------

result = rsi.calculate(df)

decision = result["decision"]

print("\n===================================")
print("RSI DECISION TEST")
print("===================================")

print(f"Score      : {decision['score']}")
print(f"Direction  : {decision['direction']}")
print(f"Confidence : {decision['confidence']}")
print(f"Reason     : {decision['reason']}")

print("===================================")
