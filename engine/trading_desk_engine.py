from datetime import datetime

from data.market_data import MarketDataEngine
from engine.trade_quality import TradeQualityEngine

# Indicator Engines
from engine import ema
from engine import macd
from engine import rsi


class TradingDeskEngine:

    def __init__(self):

        self.market = MarketDataEngine()
        self.trade_quality = TradeQualityEngine()

    # -------------------------------------------------

    def analyze(self, ticker, analysis_datetime):

        # -----------------------------------------
        # Load market data up to requested time
        # -----------------------------------------

        df = self.market.get_data_until(
            ticker=ticker,
            end_datetime=analysis_datetime
        )

        print("--------------------------------")
        print(df.head())
        print("--------------------------------")
        print(df.columns)
        print("--------------------------------")
        print(type(df))
        print("--------------------------------")
        print(df.shape)
        print("--------------------------------")
        print(df.index)

        # -----------------------------------------
        # Run Expert Engines
        # -----------------------------------------

        ema_result = ema.calculate(df)

        macd_result = macd.calculate(df)

        rsi_result = rsi.calculate(df)

        # -----------------------------------------
        # Calculate Trade Quality
        # -----------------------------------------

        quality = self.trade_quality.evaluate(
            ema_result,
            macd_result,
            rsi_result
        )

        # -----------------------------------------
        # Return Trading Desk Result
        # -----------------------------------------

        return {

            "ticker": ticker,

            "analysis_time": analysis_datetime,

            "trade_health": quality["score"],

            "confidence": quality["confidence"],

            "consensus": quality["consensus"],

            "direction": quality["direction"],

            "status": quality["status"],

            "grade": quality["grade"],

            "qualified": quality["qualified"],

            "recommendation": quality["status"],

            "reasons": quality["evidence"],

            # Keep complete engine output
            "raw": quality

        }
