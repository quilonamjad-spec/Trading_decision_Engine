"""
====================================================
Trade Decision Engine (TDE)

EMA Engine V2
====================================================
"""

from typing import Dict
import pandas as pd
import config


def percentage_distance(price: float, reference: float) -> float:
    """
    Percentage distance between current price and reference.
    """
    return round(((price - reference) / reference) * 100, 2)


def calculate(df: pd.DataFrame, candle: int = -1) -> Dict:

    close = df["Close"]

    ema5 = close.ewm(span=config.EMA_FAST, adjust=False).mean()
    ema9 = close.ewm(span=config.EMA_MEDIUM, adjust=False).mean()
    ema20 = close.ewm(span=config.EMA_SLOW, adjust=False).mean()
    ema50 = close.ewm(span=config.EMA_TREND, adjust=False).mean()

    price = float(close.iloc[candle])

    e5 = float(ema5.iloc[candle])
    e9 = float(ema9.iloc[candle])
    e20 = float(ema20.iloc[candle])
    e50 = float(ema50.iloc[candle])

    # ----------------------------------
    # Trend Alignment
    # ----------------------------------

    if e5 > e9 > e20 > e50:
        alignment = "Bullish"

    elif e5 < e9 < e20 < e50:
        alignment = "Bearish"

    else:
        alignment = "Mixed"

    # ----------------------------------
    # Price Position
    # ----------------------------------

    price_vs_ema20 = "Above EMA20" if price > e20 else "Below EMA20"
    price_vs_ema50 = "Above EMA50" if price > e50 else "Below EMA50"

    # ----------------------------------
    # Distances
    # ----------------------------------

    distance20 = percentage_distance(price, e20)
    distance50 = percentage_distance(price, e50)

    return {

        "name": "EMA",

        "pillar": "Trend",

        "values": {

            "price": round(price,2),

            "ema5": round(e5,2),

            "ema9": round(e9,2),

            "ema20": round(e20,2),

            "ema50": round(e50,2)

        },

        "analysis": {

            "alignment": alignment,

            "price_vs_ema20": price_vs_ema20,

            "price_vs_ema50": price_vs_ema50,

            "distance_ema20_pct": distance20,

            "distance_ema50_pct": distance50

        }

    }


