"""
====================================================

Trade Decision Engine (TDE)

Calibration Manager

====================================================
"""

import json
from pathlib import Path


class CalibrationManager:

    def __init__(self):

        calibration_file = (
            Path(__file__).parent /
            "calibration.json"
        )

        with open(calibration_file, "r") as file:

            self.config = json.load(file)

    # =================================================
    # Trend Expert
    # =================================================

    def get_trend_score(self, alignment: str):

        trend = self.config["experts"]["trend"]

        if alignment == "Bullish":
            return trend["bullish"]

        elif alignment == "Bearish":
            return trend["bearish"]

        return trend["mixed"]

    # =================================================
    # Momentum Expert
    # =================================================

    def get_momentum_score(self, bias: str):

        momentum = self.config["experts"]["momentum"]
    
        if bias == "Bullish":
            return momentum["bullish"]
    
        elif bias == "Bearish":
            return momentum["bearish"]
    
        return momentum["neutral"]

    # =================================================
    # Risk Expert
    # =================================================

    def get_risk_score(self, state: str):

        risk = self.config["experts"]["risk"]

        if state == "Healthy":
            return risk["healthy"]

        elif state == "Warning":
            return risk["warning"]

        return risk["high"]

    # =================================================
    # Penalties
    # =================================================

    @property
    def conflicting_penalty(self):

        return self.config["penalties"]["conflicting_signals"]

    @property
    def overextended_penalty(self):

        return self.config["penalties"]["overextended"]

    @property
    def weak_volume_penalty(self):

        return self.config["penalties"]["weak_volume"]

    @property
    def late_entry_penalty(self):

        return self.config["penalties"]["late_entry"]

    # =================================================
    # Qualification
    # =================================================

    @property
    def minimum_trend(self):

        return self.config["qualification"]["minimum_trend"]

    @property
    def minimum_consensus(self):

        return self.config["qualification"]["minimum_consensus"]

    # =================================================
    # Metadata
    # =================================================

    @property
    def version(self):

        return self.config["research"]["version"]

    @property
    def calibration_name(self):

        return self.config["research"]["name"]
