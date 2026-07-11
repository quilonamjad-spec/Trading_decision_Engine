"""
=========================================================
Trade Decision Engine (TDE)

Trade Quality Engine
Version : 2.0
=========================================================
"""


class TradeQualityEngine:

    """
    Combines outputs from all expert engines
    into one Trade Quality Score.
    """

    def __init__(self):

        self.MAX_SCORE = 100

    # -------------------------------------------------

    def evaluate(
        self,
        ema_result,
        macd_result,
        rsi_result,
    ):

        # -----------------------------------------
        # Extract Expert Decisions
        # -----------------------------------------

        trend = ema_result["decision"]

        momentum = macd_result["decision"]

        risk = rsi_result["decision"]

        # -----------------------------------------
        # Score
        # -----------------------------------------

        total_score = (

            trend["score"]

            + momentum["score"]

            + risk["score"]

        )

        # -----------------------------------------
        # Direction
        # -----------------------------------------

        directions = [

            trend["direction"],

            momentum["direction"],

            risk["direction"]

        ]

        direction = self.get_majority_direction(directions)

        # -----------------------------------------
        # Confidence
        # -----------------------------------------

        confidence = self.get_majority_confidence(

            [

                trend["confidence"],

                momentum["confidence"],

                risk["confidence"]

            ]

        )

        # -----------------------------------------
        # Final Result
        # -----------------------------------------

        return {

            "score": total_score,

            "grade": self.get_grade(total_score),

            "status": self.get_status(total_score),

            "direction": direction,

            "confidence": confidence,

            "breakdown": {

                "Trend": trend["score"],

                "Momentum": momentum["score"],

                "Risk": risk["score"]

            },

            "evidence": [

                trend["reason"],

                momentum["reason"],

                risk["reason"]

            ]

        }

    # -------------------------------------------------

    def get_majority_direction(self, directions):

        long_votes = directions.count("LONG")

        short_votes = directions.count("SHORT")

        if long_votes > short_votes:

            return "LONG"

        elif short_votes > long_votes:

            return "SHORT"

        return "NEUTRAL"

    # -------------------------------------------------

    def get_majority_confidence(self, confidence):

        high = confidence.count("High")

        medium = confidence.count("Medium")

        low = confidence.count("Low")

        if high >= 2:

            return "High"

        elif medium >= 2:

            return "Medium"

        return "Low"

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
