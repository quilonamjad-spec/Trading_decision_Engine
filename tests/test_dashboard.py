from data.market_data import MarketDataEngine

from indicators import ema
from indicators import macd
from indicators import rsi

from engine.trade_quality import TradeQualityEngine
from engine.dashboard import DashboardEngine


market = MarketDataEngine()

market_data = market.download_watchlist()

trade_engine = TradeQualityEngine()

dashboard = DashboardEngine()

result = dashboard.build(

    market_data,

    trade_engine,

    ema,

    macd,

    rsi

)

print("\n===================================")
print("TDE DASHBOARD ENGINE TEST")
print("===================================\n")

print("Market Score :", result["market_score"])

print("\nSummary")
print(result["summary"])

print("\nDirection Summary")
print(result["direction_summary"])

print("\nConfidence Summary")
print(result["confidence_summary"])

print("\nBest Opportunity")
print(result["best_trade"]["ticker"],
      result["best_trade"]["score"],
      result["best_trade"]["status"])

print("\n===================================")
print("STOCK RANKING")
print("===================================\n")

for row in result["stocks"]:

    print(

        f"{row['ticker']:<18}"

        f"{row['score']:>3}/100   "

        f"{row['status']}"

    )
