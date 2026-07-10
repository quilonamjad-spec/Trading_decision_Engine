"""
====================================================
Trade Decision Engine

Indicator Engine
====================================================
"""

from indicators.ema import calculate as ema_calculate
from indicators.macd import calculate as macd_calculate
from indicators.rsi import calculate as rsi_calculate


class IndicatorEngine:

    def analyse_stock(self, df):

        return {

            "trend": ema_calculate(df),

            "momentum": macd_calculate(df),

            "risk": rsi_calculate(df)

        }

    def analyse_market(self, market_data):

        results = {}

        for ticker, df in market_data.items():

            results[ticker] = self.analyse_stock(df)

        return results
