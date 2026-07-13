"""
====================================================

Trade Decision Engine

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

    # -------------------------------------------------

    @property
    def trend_weight(self):

        return self.config["positive"]["trend"]

    @property
    def momentum_weight(self):

        return self.config["positive"]["momentum"]

    @property
    def risk_weight(self):

        return self.config["positive"]["risk"]

    @property
    def pattern_weight(self):

        return self.config["positive"]["pattern"]

    @property
    def volume_weight(self):

        return self.config["positive"]["volume"]

    # -------------------------------------------------

    @property
    def penalty_conflicting(self):

        return self.config["penalties"]["conflicting_signals"]

    @property
    def penalty_overextended(self):

        return self.config["penalties"]["overextended"]

    @property
    def penalty_volume(self):

        return self.config["penalties"]["weak_volume"]

    @property
    def penalty_late_entry(self):

        return self.config["penalties"]["late_entry"]

    # -------------------------------------------------

    @property
    def qualification_trend(self):

        return self.config["qualification"]["minimum_trend"]

    @property
    def qualification_consensus(self):

        return self.config["qualification"]["minimum_consensus"]
