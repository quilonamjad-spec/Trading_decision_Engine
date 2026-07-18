"""
=========================================================

Trade Decision Engine (TDE)

Decision Engine
Version 1.1 (Benchmark Build)

Purpose
-------
Converts Conviction + Trade Score into a trading decision.

This version is intended for Replay Benchmarking.
The goal is to verify that every decision state is reachable.

=========================================================
"""


class DecisionEngine:

    def __init__(self):
        pass

    # ----------------------------------------------------

    def evaluate(self, conviction, trade_score):

        immediate = conviction["immediate"]
        context = conviction["context"]
        velocity = conviction["velocity"]
        persistence = conviction["persistence"]

        # ----------------------------------------------------
        # EXIT (Highest Priority)
        # ----------------------------------------------------

        if (
            immediate == "Weakening"
            and context == "Persistent Weakening"
            and velocity == "Fast"
            and persistence >= 3
        ):

            return {

                "state": "EXIT",

                "confidence": "High",

                "recommendation":
                    "Exit the trade. Conviction has collapsed.",

                "reason":
                    "Rapid deterioration detected."

            }

        # ----------------------------------------------------
        # QUESTION
        # ----------------------------------------------------

        if (
            immediate == "Weakening"
            and context == "Persistent Weakening"
        ):

            return {

                "state": "QUESTION",

                "confidence": "Medium",

                "recommendation":
                    "Reassess the original trade thesis.",

                "reason":
                    "Conviction is weakening."

            }

        # ----------------------------------------------------
        # COMMIT
        # ----------------------------------------------------

        if (
            trade_score >= 85
            and immediate == "Improving"
        ):

            return {

                "state": "COMMIT",

                "confidence": "High",

                "recommendation":
                    "Strong opportunity. Execute / Stay with the trade.",

                "reason":
                    "Excellent Trade Quality with improving conviction."

            }

        # ----------------------------------------------------
        # CONFIRM
        # ----------------------------------------------------

        if (
            trade_score >= 70
            and immediate == "Improving"
        ):

            return {

                "state": "CONFIRM",

                "confidence": "Medium",

                "recommendation":
                    "Trade is strengthening. Wait for one more confirmation.",

                "reason":
                    "Trade quality is good and conviction is improving."

            }

        # ----------------------------------------------------
        # MONITOR
        # ----------------------------------------------------

        if trade_score >= 50:

            return {

                "state": "MONITOR",

                "confidence": "Medium",

                "recommendation":
                    "Continue monitoring the setup.",

                "reason":
                    "Average trade quality."

            }

        # ----------------------------------------------------
        # DISCOVER
        # ----------------------------------------------------

        return {

            "state": "DISCOVER",

            "confidence": "Low",

            "recommendation":
                "Continue observing before committing.",

            "reason":
                "Trade quality not yet sufficient."

        }
