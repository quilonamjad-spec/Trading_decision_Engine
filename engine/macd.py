"""
====================================================
Trade Decision Engine (TDE)

MACD Engine V2
====================================================
"""

from typing import Dict
from research.calibration_manager import CalibrationManager
calibration = CalibrationManager()
import pandas as pd


def calculate(df: pd.DataFrame, candle: int = -1) -> Dict:

    close = df["Close"]

    # ----------------------------
    # MACD Calculation
    # ----------------------------

    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()

    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()

    histogram = macd_line - signal_line

    macd = float(macd_line.iloc[candle])
    signal = float(signal_line.iloc[candle])
    hist = float(histogram.iloc[candle])

    prev_hist = float(histogram.iloc[candle - 1])

    # ----------------------------
    # Momentum Bias
    # ----------------------------

    if macd > signal:
        momentum_bias = "Bullish"

    elif macd < signal:
        momentum_bias = "Bearish"

    else:
        momentum_bias = "Neutral"

    # ----------------------------
    # Histogram Interpretation
    # ----------------------------

    if hist >= 0:

        if hist > prev_hist:
            histogram_state = "Bullish Momentum Increasing"

        else:
            histogram_state = "Bullish Momentum Weakening"

    else:

        if hist > prev_hist:
            histogram_state = "Bearish Momentum Weakening"

        else:
            histogram_state = "Bearish Momentum Increasing"

    # ----------------------------
    # Momentum Strength
    # ----------------------------

    abs_hist = abs(hist)

    if abs_hist > 0.50:

        strength = "Strong"

    elif abs_hist > 0.20:

        strength = "Moderate"

    else:

        strength = "Weak"

    # ----------------------------------
    # Decision
    # ----------------------------------

    score = calibration.get_momentum_score(momentum_bias)

    if momentum_bias == "Bullish":
    
        direction = "LONG"
    
    elif momentum_bias == "Bearish":
    
        direction = "SHORT"
    
    else:
    
        direction = "NEUTRAL"

    # Confidence

    if strength == "Strong":

        confidence = "High"

    elif strength == "Moderate":

        confidence = "Medium"

    else:

        confidence = "Low"

    # Explainability

    reason = histogram_state

    # ----------------------------
    # Return
    # ----------------------------

    return {

        "name": "MACD",

        "pillar": "Momentum",

        "values": {

            "macd": round(macd, 2),

            "signal": round(signal, 2),

            "histogram": round(hist, 2)

        },

        "analysis": {

            "momentum_bias": momentum_bias,

            "histogram_state": histogram_state,

            "strength": strength

        },

        "decision": {

            "score": score,

            "direction": direction,

            "confidence": confidence,

            "reason": reason

        }

    }
