"""
=========================================================
Trade Decision Engine (TDE)

Trade Quality Engine
Version : 1.0
=========================================================
"""


class TradeQualityEngine:

    """
    Combines outputs from all indicator engines
    into one Trade Quality Score.
    """

    def __init__(self):

        self.MAX_SCORE = 100

        self.TREND_WEIGHT = 35

        self.MOMENTUM_WEIGHT = 35

        self.RISK_WEIGHT = 30

    # -------------------------------------------------

    def calculate(
        self,
        trend_score,
        momentum_score,
        risk_score,
        direction,
    ):

        total_score = (
            trend_score +
            momentum_score +
            risk_score
        )

        result = {

            "score": total_score,

            "grade": self.get_grade(total_score),

            "status": self.get_status(total_score),

            "direction": direction,

            "breakdown": {

                "Trend": trend_score,

                "Momentum": momentum_score,

                "Risk": risk_score,

            }

        }

        return result

    # -------------------------------------------------

    def get_status(self, score):

        if score >= 90:
            return "READY"

        elif score >= 80:
            return "READY (Minor Concerns)"

        elif score >= 70:
            return "READY (High Risk)"

        elif score >= 60:
            return "WAIT"

        return "AVOID"

    # -------------------------------------------------

    def get_grade(self, score):

        if score >= 90:
            return "A+"

        elif score >= 80:
            return "A"

        elif score >= 70:
            return "B"

        elif score >= 60:
            return "C"

        return "D"
