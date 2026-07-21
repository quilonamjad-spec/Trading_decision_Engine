"""
====================================================
Trade Decision Engine (TDE)

Version : 1.0
Module  : Market Data Engine
====================================================
"""

from typing import Dict

import pandas as pd
import yfinance as yf

from utils.watchlist import load_universe

import config


class MarketDataEngine:

    """
    Downloads market data for TDE.

    Responsibilities

    • Download watchlists
    • Download individual stocks
    • Validate downloaded data
    • Return pandas DataFrames
    """

    # -----------------------------------------------------

    def __init__(self, universe="nifty50"):

        self.universe = universe

        self.watchlist = load_universe(universe)

        self.period = config.PERIOD

        self.interval = config.INTERVAL

     # -----------------------------------------------------

    def get_data(self, ticker):
    
        df = yf.download(
    
            ticker,
    
            period=self.period,
    
            interval=self.interval,
    
            progress=False,
    
            auto_adjust=True
    
        )
    
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
    
        return df

     
     # ---------------------------------------------------    
    def get_data_until(self, ticker, end_datetime):
    
        import pandas as pd
    
        df = self.get_data(ticker)
    
        print("\n========== DEBUG ==========")
        print("Index dtype :", df.index.dtype)
        print("Index tz    :", df.index.tz)
        print("Input type  :", type(end_datetime))
        print("Input value :", end_datetime)
    
        ts = pd.Timestamp(end_datetime)
    
        print("Timestamp   :", ts)
        print("Timestamp tz:", ts.tz)
    
        if df.index.tz is not None:
            ts = ts.tz_localize(df.index.tz)
    
        print("After localize:", ts)
        print("===========================\n")
    
        df = df[df.index <= ts]
    
        return df



     # ---------------------------------------------------    

 
    
    # -----------------------------------------------------
    # Internal Downloader
    # -----------------------------------------------------

    def _download(self, ticker):

        ticker = ticker.upper().strip()

        if not ticker.endswith(".NS"):

            ticker += ".NS"

        df = yf.download(

            ticker,

            period=self.period,

            interval=self.interval,

            progress=False,

            auto_adjust=True

        )

        if isinstance(df.columns, pd.MultiIndex):

            df.columns = df.columns.get_level_values(0)

        if df.empty:

            return None

        return df

    # -----------------------------------------------------
    # Download Watchlist
    # -----------------------------------------------------

    def download_watchlist(self) -> Dict[str, pd.DataFrame]:

        market_data = {}

        print("\nDownloading market data...\n")

        for ticker in self.watchlist:

            try:

                df = self._download(ticker)

                if df is None:

                    print(f"{ticker} : No Data")

                    continue

                market_data[ticker] = df

                print(f"{ticker} : {len(df)} candles")

            except Exception as e:

                print(f"{ticker} : ERROR")

                print(e)

        print("\nDownload Complete.")

        return market_data
    # -----------------------------------------------------
    # Download Single Stock
    # -----------------------------------------------------

    def download_stock(self, ticker):

        """
        Download one stock.

        Used by:

        • My Ideas
        • Manual Analysis
        • Commit Trade
        • Portfolio Analysis
        """

        try:

            return self._download(ticker)

        except Exception as e:

            print(f"{ticker} : ERROR")

            print(e)

            return None

    # -----------------------------------------------------
    # Refresh Universe
    # -----------------------------------------------------

    def set_universe(self, universe):

        """
        Switch watchlists without
        recreating the MarketDataEngine.
        """

        self.universe = universe

        self.watchlist = load_universe(universe)

    # -----------------------------------------------------
    # Current Watchlist
    # -----------------------------------------------------

    def get_watchlist(self):

        """
        Returns the currently
        loaded watchlist.
        """

        return self.watchlist

    # -----------------------------------------------------
    # Current Settings
    # -----------------------------------------------------

    def settings(self):

        """
        Useful for debugging and
        displaying current engine settings.
        """

        return {

            "Universe": self.universe,

            "Stocks": len(self.watchlist),

            "Period": self.period,

            "Interval": self.interval

        }
