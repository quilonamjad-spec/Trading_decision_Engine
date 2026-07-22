from data.market_data import MarketDataEngine

from engine import ema
from engine import macd
from engine import rsi
from engine.trade_quality import TradeQualityEngine


# ---------------------------------
# INITIALIZE
# ---------------------------------

market = MarketDataEngine()
trade_engine = TradeQualityEngine()


# ---------------------------------
# STOCK
# ---------------------------------

ticker = "SBIN.NS"


# ---------------------------------
# DOWNLOAD DATA
# ---------------------------------

print("\nDownloading Market Data...\n")

df = market.get_data(ticker)

print(f"Candles Downloaded : {len(df)}")


# ---------------------------------
# RUN INDICATORS
# ---------------------------------

ema_result = ema.calculate(df)

macd_result = macd.calculate(df)

rsi_result = rsi.calculate(df)


# ---------------------------------
# TRADE QUALITY
# ---------------------------------

trade = trade_engine.evaluate(
    ema_result,
    macd_result,
    rsi_result
)


# ---------------------------------
# DISPLAY
# ---------------------------------

print("\n==============================")
print("TRADE DECISION ENGINE")
print("==============================\n")

print("Ticker :", ticker)

print("\nTrade Health :", trade["score"], "/100")
print("Status       :", trade["status"])
print("Grade        :", trade["grade"])
print("Stars        :", trade["stars"])

print("\nDirection    :", trade["direction"])
print("Confidence   :", trade["confidence"])

print("\nConsensus")

print(trade["consensus"])

print("\nBreakdown")

print(trade["breakdown"])

print("\nEvidence")

for item in trade["evidence"]:
    print("-", item)

print("\nGatekeeper")

print(trade["gatekeeper"])
