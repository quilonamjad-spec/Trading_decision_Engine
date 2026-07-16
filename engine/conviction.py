"""
=========================================================

Trade Decision Engine (TDE)

Conviction Engine
Version : 1.0

Purpose:
Tracks whether the confidence behind a trading
decision is improving or deteriorating.

=========================================================
"""


class ConvictionEngine:

    def __init__(self):

        pass

    # -------------------------------------------------

    def evaluate(

        self,

        previous_consensus,

        current_consensus

    ):

        previous = previous_consensus["multiplier"]

        current = current_consensus["multiplier"]

        difference = round(

            current - previous,

            2

        )

        # ---------------------------------------------

        if difference >= 0.05:

            trend = "Increasing"

            recommendation = "Increase Confidence"

        elif difference >= -0.02:

            trend = "Stable"

            recommendation = "Continue Holding"

        elif difference >= -0.10:

            trend = "Weakening"

            recommendation = "Reduce Confidence"

        else:

            trend = "Broken"

            recommendation = "Exit Candidate"

        # ---------------------------------------------

        return {

            "previous": previous,

            "current": current,

            "change": difference,

            "trend": trend,

            "recommendation": recommendation,

            "reason":

                f"Consensus changed "

                f"from {previous:.2f} "

                f"to {current:.2f}"

        }
