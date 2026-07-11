"""
====================================================
Trade Decision Engine (TDE)

MACD Engine Test
====================================================
"""

from data.market_data import MarketDataEngine
from indicators import macd

# ----------------------------------
# Download Market Data
# ----------------------------------

market = MarketDataEngine()

market_data = market.download_watchlist()

# Test using SBIN
df = market_data["SBIN.NS"]

# ----------------------------------
# Run MACD Engine
# ----------------------------------

result = macd.calculate(df)

# ----------------------------------
# Display Decision
# ----------------------------------

print("\n===================================")
print("MACD DECISION TEST")
print("===================================")

print(result["decision"])

print("\n===================================")
