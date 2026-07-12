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

rows = dashboard.build(

    market_data,

    trade_engine,

    ema,

    macd,

    rsi

)

print("\n==============================")
print("TDE DASHBOARD TEST")
print("==============================\n")

for row in rows:

    print(

        f"{row['ticker']:<18}"

        f"{row['score']:>3}/100   "

        f"{row['status']}"

    )
