from datetime import datetime

from engine.market_data import MarketDataEngine
from engine.trade_quality import TradeQualityEngine


class TradingDeskEngine:

    def __init__(self):
        self.market = MarketDataEngine()
        self.trade_quality = TradeQualityEngine()

    def analyze(self, ticker, analysis_datetime):

        # Load market data up to requested time
        df = self.market.get_data_until(
            ticker=ticker,
            end_datetime=analysis_datetime
        )

        # Calculate Trade Quality
        result = self.trade_quality.evaluate(df)

        return result
