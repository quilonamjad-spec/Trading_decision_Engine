"""
=========================================================

Trade Decision Engine (TDE)

Consensus Engine
Version : 1.0

=========================================================
"""


class ConsensusEngine:

    def __init__(self):

        self.weights = {
            "High": 3,
            "Medium": 2,
            "Low": 1
        }

        self.maximum_score = 9

    # -------------------------------------------------

    def evaluate(
        self,
        ema_result,
        macd_result,
        rsi_result
    ):

        trend = ema_result["decision"]
        momentum = macd_result["decision"]
        risk = rsi_result["decision"]

        # ---------------------------------------------
        # Confidence Score
        # ---------------------------------------------

        confidence_total = (

            self.weights.get(
                trend["confidence"], 1
            )

            +

            self.weights.get(
                momentum["confidence"], 1
            )

            +

            self.weights.get(
                risk["confidence"], 1
            )

        )

        multiplier = round(

            confidence_total /

            self.maximum_score,

            2

        )

        # ---------------------------------------------
        # Direction Agreement
        # ---------------------------------------------

        directions = [

            trend["direction"],

            momentum["direction"],

            risk["direction"]

        ]

        long_votes = directions.count("LONG")

        short_votes = directions.count("SHORT")

        if long_votes == 3 or short_votes == 3:

            agreement = "Strong"

        elif long_votes == 2 or short_votes == 2:

            agreement = "Moderate"

        else:

            agreement = "Weak"

        # ---------------------------------------------
        # Result
        # ---------------------------------------------

        return {

            "agreement": agreement,

            "confidence_score": confidence_total,

            "multiplier": multiplier,

            "reason":

                f"{agreement} consensus | "

                f"Confidence "

                f"{confidence_total}/9"

        }
