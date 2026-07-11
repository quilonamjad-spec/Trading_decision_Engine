from indicators import ema
from data.market_data import MarketData

# -----------------------------------
# Download Data
# -----------------------------------

market = MarketData()

data = market.download_data(["SBIN.NS"])

df = data["SBIN.NS"]

# -----------------------------------
# Run EMA Engine
# -----------------------------------

result = ema.calculate(df)

print(result["decision"])
