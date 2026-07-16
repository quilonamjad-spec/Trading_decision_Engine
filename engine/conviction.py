"""
=========================================================

Trade Decision Engine (TDE)

Conviction Engine
Version 1.0

Purpose
-------
Reads the recent Decision Memory and determines
whether confidence is improving, stable or weakening.

This module NEVER decides:

- Buy
- Sell
- Exit

It only reports how conviction is evolving.

=========================================================
"""

class ConvictionEngine:

    def __init__(self):

        pass

    # ----------------------------------------------------

    def evaluate(self, history):

        """
        history

        List returned by DecisionMemory.history(symbol)
        """

        # -----------------------------------------------
        # Not enough history
        # -----------------------------------------------

        if len(history) < 2:

            return {

                "current": None,

                "average": None,

                "direction": "Unknown",

                "strength": "Unknown",

                "persistence": 0,

                "change": 0,

                "message": "Insufficient history"

            }

        # -----------------------------------------------
        # Extract consensus history
        # -----------------------------------------------

        values = [

            item["consensus"]

            for item in history

        ]

        current = values[-1]

        previous = values[-2]

        average = round(

            sum(values) / len(values),

            2

        )

        change = round(

            current - previous,

            2

        )

        # -----------------------------------------------
        # Detect Direction
        # -----------------------------------------------

        if change > 2:

            direction = "Rising"

        elif change < -2:

            direction = "Falling"

        else:

            direction = "Stable"

        # -----------------------------------------------
        # Persistence
        #
        # Count how many consecutive
        # observations continue
        # the same trend.
        # -----------------------------------------------

        persistence = 1

        for i in range(len(values) - 1, 0, -1):

            diff = values[i] - values[i - 1]

            if direction == "Rising" and diff > 0:

                persistence += 1

            elif direction == "Falling" and diff < 0:

                persistence += 1

            elif direction == "Stable" and abs(diff) <= 2:

                persistence += 1

            else:

                break

        # -----------------------------------------------
        # Strength
        # -----------------------------------------------

        deviation = round(

            current - average,

            2

        )

        if abs(deviation) >= 15:

            strength = "Strong"

        elif abs(deviation) >= 7:

            strength = "Moderate"

        else:

            strength = "Weak"

        # -----------------------------------------------
        # Human readable explanation
        # -----------------------------------------------

        if direction == "Rising":

            message = (

                "Confidence has been improving "

                f"for {persistence} observations."

            )

        elif direction == "Falling":

            message = (

                "Confidence has been weakening "

                f"for {persistence} observations."

            )

        else:

            message = (

                "Confidence has remained stable."

            )

        # -----------------------------------------------

        return {

            "current": current,

            "average": average,

            "change": change,

            "direction": direction,

            "strength": strength,

            "persistence": persistence,

            "message": message

        }
