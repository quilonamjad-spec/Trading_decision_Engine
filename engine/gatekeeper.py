"""
====================================================

Trade Decision Engine (TDE)

Gatekeeper

Version 1.0

Purpose:
Decides whether a stock deserves further evaluation.

====================================================
"""


class Gatekeeper:

    def __init__(self):
        pass

    # -------------------------------------------------

    def qualify(self, ema_result, macd_result, rsi_result):

        reasons = []

        qualified = True

        # -----------------------------------------
        # Rule 1
        # Trend and Momentum must agree
        # -----------------------------------------

        ema_direction = ema_result["decision"]["direction"]
        macd_direction = macd_result["decision"]["direction"]

        if ema_direction != macd_direction:

            qualified = False

            reasons.append(
                "Trend and Momentum are not aligned"
            )

        # -----------------------------------------
        # Rule 2
        # Reject High Risk setups
        # -----------------------------------------

        risk = rsi_result["decision"]["risk"]

        if risk == "High":

            qualified = False

            reasons.append(
                "RSI indicates High Risk"
            )

        # -----------------------------------------
        # Build Result
        # -----------------------------------------

        if qualified:

            return {

                "qualified": True,

                "status": "PASS",

                "reason": "All gatekeeper rules satisfied"

            }

        return {

            "qualified": False,

            "status": "FAIL",

            "reason": " | ".join(reasons)

        }
