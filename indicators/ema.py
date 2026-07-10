"""
====================================================
Trade Decision Engine (TDE)

Version : 0.6
Module  : EMA Engine

Author  : Amjad + ChatGPT
====================================================
"""

from typing import Dict

import pandas as pd

import config


def calculate(df: pd.DataFrame, candle: int = -1) -> Dict:
    """
    Calculate EMA values and determine alignment.

    Parameters
    ----------
    df : DataFrame
        OHLCV DataFrame

    candle : int
        Candle index (-1 = latest)

    Returns
    -------
    dict
    """

    close = df["Close"]

    ema5 = close.ewm(span=config.EMA_FAST, adjust=False).mean()
    ema9 = close.ewm(span=config.EMA_MEDIUM, adjust=False).mean()
    ema20 = close.ewm(span=config.EMA_SLOW, adjust=False).mean()
    ema50 = close.ewm(span=config.EMA_TREND, adjust=False).mean()

    e5 = float(ema5.iloc[candle])
    e9 = float(ema9.iloc[candle])
    e20 = float(ema20.iloc[candle])
    e50 = float(ema50.iloc[candle])

    # ---------------------------------
    # Alignment
    # ---------------------------------

    if e5 > e9 > e20 > e50:

        alignment = "Bullish"

    elif e5 < e9 < e20 < e50:

        alignment = "Bearish"

    else:

        alignment = "Mixed"

    return {

        "ema5": round(e5,2),

        "ema9": round(e9,2),

        "ema20": round(e20,2),

        "ema50": round(e50,2),

        "alignment": alignment

    }
