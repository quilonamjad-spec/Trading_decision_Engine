"""
====================================================
Trade Decision Engine (TDE)

RSI Engine V2
====================================================
"""

from typing import Dict
from research.calibration_manager import CalibrationManager
calibration = CalibrationManager()
import pandas as pd


def calculate(df: pd.DataFrame, period: int = 14, candle: int = -1) -> Dict:
    """
    Calculate RSI and classify market condition.
    """

    close = df["Close"]

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    rsi_value = round(float(rsi.iloc[candle]), 2)

    # -------------------------------------
    # RSI Zone
    # -------------------------------------

    if rsi_value < 30:

        zone = "Oversold"
        risk = "Low"

    elif rsi_value < 40:

        zone = "Recovering"
        risk = "Low"

    elif rsi_value < 60:

        zone = "Healthy"
        risk = "Low"

    elif rsi_value < 70:

        zone = "Strong"
        risk = "Medium"

    elif rsi_value < 80:

        zone = "Overheated"
        risk = "High"

    else:

        zone = "Extreme"
        risk = "Very High"

    # -------------------------------------
    # Decision
    # -------------------------------------

    # Score

    score = calibration.get_risk_score(risk)

    if risk == "Low":
    
        confidence = "High"
    
    elif risk == "Medium":
    
        confidence = "Medium"
    
    else:
    
        confidence = "Low"

    # Direction

    if zone in ["Oversold", "Recovering"]:

        direction = "LONG"

    elif zone in ["Overheated", "Extreme"]:

        direction = "SHORT"

    else:

        direction = "NEUTRAL"

    # Explainability

    reason = f"{zone} ({risk} Risk)"

    return {

        "name": "RSI",

        "pillar": "Risk",

        "values": {

            "rsi": rsi_value

        },

        "analysis": {

            "zone": zone,

            "risk": risk

        },

        "decision": {

            "score": score,

            "direction": direction,

            "confidence": confidence,

            "reason": reason

        }

    }
