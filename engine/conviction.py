"""
=========================================================

Trade Decision Engine (TDE)

Conviction Engine
Version : 2.0

Purpose
-------
Analyses Decision Memory and reports
how conviction is evolving.

It NEVER decides whether to:

- Buy
- Sell
- Hold
- Exit

=========================================================
"""


class ConvictionEngine:

    def __init__(self, context_window=6):

        self.context_window = context_window

    # ----------------------------------------------------

    def evaluate(self, history):

        if len(history) < 2:

            return {

                "current": None,
                "previous": None,
                "average": None,

                "change": 0,

                "immediate": "Unknown",
                "context": "Insufficient History",

                "persistence": 0,

                "velocity": "Unknown",

                "message": "Need more observations."

            }

        # ------------------------------------------------
        # Extract consensus values
        # ------------------------------------------------

        values = [item["consensus"] for item in history]

        current = values[-1]
        previous = values[-2]

        average = round(sum(values) / len(values), 2)

        change = current - previous

        # ------------------------------------------------
        # Immediate Analysis
        # ------------------------------------------------

        if change >= 2:

            immediate = "Improving"

        elif change <= -2:

            immediate = "Weakening"

        else:

            immediate = "Stable"

        # ------------------------------------------------
        # Context Window
        # ------------------------------------------------

        window = values[-self.context_window:]

        rising = 0
        falling = 0
        flat = 0

        for i in range(1, len(window)):

            diff = window[i] - window[i - 1]

            if diff >= 2:

                rising += 1

            elif diff <= -2:

                falling += 1

            else:

                flat += 1

        # ------------------------------------------------
        # Context Decision
        # ------------------------------------------------

        if rising > falling and rising >= 3:

            context = "Persistent Improvement"

        elif falling > rising and falling >= 3:

            context = "Persistent Weakening"

        elif flat >= max(rising, falling):

            context = "Stable"

        else:

            context = "Mixed"

        # ------------------------------------------------
        # Persistence
        # ------------------------------------------------

        persistence = 1

        if immediate == "Improving":

            for i in range(len(window) - 1, 0, -1):

                if (window[i] - window[i - 1]) >= 2:

                    persistence += 1

                else:

                    break

        elif immediate == "Weakening":

            for i in range(len(window) - 1, 0, -1):

                if (window[i] - window[i - 1]) <= -2:

                    persistence += 1

                else:

                    break

        else:

            for i in range(len(window) - 1, 0, -1):

                if abs(window[i] - window[i - 1]) < 2:

                    persistence += 1

                else:

                    break

        # ------------------------------------------------
        # Velocity
        # ------------------------------------------------

        total_change = 0

        for i in range(1, len(window)):

            total_change += abs(window[i] - window[i - 1])

        avg_change = total_change / (len(window) - 1)

        if avg_change < 2:

            velocity = "Slow"

        elif avg_change < 5:

            velocity = "Moderate"

        else:

            velocity = "Fast"

        # ------------------------------------------------
        # Message
        # ------------------------------------------------

        message = (

            f"{immediate} | "

            f"{context} | "

            f"Velocity : {velocity}"

        )

        # ------------------------------------------------

        return {

            "current": current,

            "previous": previous,

            "average": average,

            "change": round(change, 2),

            "immediate": immediate,

            "context": context,

            "persistence": persistence,

            "velocity": velocity,

            "message": message

        }
