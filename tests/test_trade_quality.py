from data.market_data import MarketDataEngine

from indicators import ema
from indicators import macd
from indicators import rsi

from engine.trade_quality import TradeQualityEngine

# ---------------------------------------
# Download Data
# ---------------------------------------

market = MarketDataEngine()

market_data = market.download_watchlist()

df = market_data["SBIN.NS"]

# ---------------------------------------
# Expert Engines
# ---------------------------------------

ema_result = ema.calculate(df)

macd_result = macd.calculate(df)

rsi_result = rsi.calculate(df)

# ---------------------------------------
# Trade Quality Engine
# ---------------------------------------

engine = TradeQualityEngine()

trade = engine.evaluate(

    ema_result,

    macd_result,

    rsi_result

)

# ---------------------------------------
# Report
# ---------------------------------------

print("\n=======================================")
print("TRADE QUALITY ENGINE TEST")
print("=======================================")

print(f"Score      : {trade['score']} / 100")
print(f"Grade      : {trade['grade']}")
print(f"Status     : {trade['status']}")
print(f"Direction  : {trade['direction']}")
print(f"Confidence : {trade['confidence']}")

print("\nBreakdown")

for k, v in trade["breakdown"].items():

    print(f"  {k:<10}: {v}")

print("\nEvidence")

for item in trade["evidence"]:

    print(f"  • {item}")

print("=======================================")
