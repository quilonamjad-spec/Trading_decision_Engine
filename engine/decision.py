"""
=========================================================

Trade Decision Engine (TDE)

Decision Engine
Version 1.0

Purpose
-------
Converts Conviction into a trading decision.

This module performs NO calculations.

It simply interprets the Conviction Engine.

=========================================================
"""


class DecisionEngine:

    def __init__(self):

        pass

    # ----------------------------------------------------

    def evaluate(self, conviction):

        immediate = conviction["immediate"]

        context = conviction["context"]

        velocity = conviction["velocity"]

        persistence = conviction["persistence"]

        # -----------------------------------------
        # COMMIT
        # -----------------------------------------

        if (

            immediate == "Improving"

            and context == "Persistent Improvement"

        ):

            return {

                "state": "COMMIT",

                "confidence": "High",

                "recommendation":

                    "Strong conviction. Stay with the trade.",

                "reason":

                    "Conviction is improving consistently."

            }

        # -----------------------------------------
        # CONFIRM
        # -----------------------------------------

        if (

            immediate == "Improving"

            and context == "Stable"

        ):

            return {

                "state": "CONFIRM",

                "confidence": "Medium",

                "recommendation":

                    "Trade is improving. Wait for confirmation.",

                "reason":

                    "Positive improvement detected."

            }

        # -----------------------------------------
        # MONITOR
        # -----------------------------------------

        if (

            immediate == "Stable"

            and context == "Stable"

        ):

            return {

                "state": "MONITOR",

                "confidence": "Medium",

                "recommendation":

                    "No action required. Continue monitoring.",

                "reason":

                    "Conviction remains stable."

            }

        # -----------------------------------------
        # QUESTION
        # -----------------------------------------

        if (

            immediate == "Weakening"

            and context == "Persistent Weakening"

            and velocity != "Fast"

        ):

            return {

                "state": "QUESTION",

                "confidence": "Medium",

                "recommendation":

                    "Reassess the original trade thesis.",

                "reason":

                    "Conviction is weakening."

            }

        # -----------------------------------------
        # EXIT
        # -----------------------------------------

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

        # -----------------------------------------
        # DISCOVER
        # -----------------------------------------

        return {

            "state": "DISCOVER",

            "confidence": "Low",

            "recommendation":

                "Continue observing before committing.",

            "reason":

                "Insufficient conviction."

        }
