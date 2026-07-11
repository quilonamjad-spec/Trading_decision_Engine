from data.market_data import MarketDataEngine
from indicators import ema

# ----------------------------------
# Download Market Data
# ----------------------------------

market = MarketDataEngine()

market_data = market.download_watchlist()

# Get SBIN DataFrame
df = market_data["SBIN.NS"]

# ----------------------------------
# Run EMA Engine
# ----------------------------------

result = ema.calculate(df)

print(result["decision"])
