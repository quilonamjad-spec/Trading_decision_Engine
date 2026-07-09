"""
====================================================
Trade Decision Engine (TDE)

Version : 0.5
Module  : Market Data Engine

Author  : Amjad + ChatGPT
====================================================
"""

from typing import Dict
import pandas as pd
import yfinance as yf

from utils.watchlist import load_watchlist
import config


class MarketDataEngine:
    """
    Downloads market data for the configured watchlist.

    Responsibilities
    ----------------
    • Read watchlist
    • Download OHLCV data
    • Validate data
    • Return dictionary of DataFrames

    Does NOT

    • Calculate indicators
    • Score stocks
    • Make recommendations
    """

    def __init__(self):

        self.watchlist = load_watchlist()

        self.interval = config.INTERVAL

        self.period = config.PERIOD

    def download_watchlist(self) -> Dict[str, pd.DataFrame]:

        market_data = {}

        print("Downloading market data...\n")

        for ticker in self.watchlist:

            try:

                df = yf.download(

                    ticker,

                    period=self.period,

                    interval=self.interval,

                    progress=False,

                    auto_adjust=True

                )

                if df.empty:

                    print(f"{ticker} : No Data")

                    continue

                market_data[ticker] = df

                print(f"{ticker} : {len(df)} candles")

            except Exception as e:

                print(f"{ticker} : ERROR")

                print(e)

        print("\nDownload Complete.")

        return market_data
