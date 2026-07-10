"""
====================================================
Trade Decision Engine (TDE)

Version : 0.6
Module  : MACD Engine

Author  : Amjad + ChatGPT
====================================================
"""

from typing import Dict
import pandas as pd


def calculate(df: pd.DataFrame, candle: int = -1) -> Dict:
    """
    Calculate MACD and analyze momentum.

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

    # MACD Calculation
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()

    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    histogram = macd_line - signal_line

    macd = float(macd_line.iloc[candle])
    signal = float(signal_line.iloc[candle])
    hist = float(histogram.iloc[candle])

    # Previous histogram for momentum comparison
    prev_hist = float(histogram.iloc[candle - 1])

    # -----------------------------
    # Analysis
    # -----------------------------

    if macd > signal:
        trend = "Bullish"
        cross = "Above Signal"
    elif macd < signal:
        trend = "Bearish"
        cross = "Below Signal"
    else:
        trend = "Neutral"
        cross = "Equal"

    if hist > prev_hist:
        histogram_direction = "Increasing"
    elif hist < prev_hist:
        histogram_direction = "Decreasing"
    else:
        histogram_direction = "Flat"

    if abs(hist) > 0.50:
        momentum = "Strong"
    elif abs(hist) > 0.20:
        momentum = "Moderate"
    else:
        momentum = "Weak"

    return {

        "name": "MACD",

        "pillar": "Momentum",

        "values": {

            "macd": round(macd, 2),
            "signal": round(signal, 2),
            "histogram": round(hist, 2)

        },

        "analysis": {

            "trend": trend,
            "cross": cross,
            "histogram_direction": histogram_direction,
            "momentum": momentum

        }

    }
