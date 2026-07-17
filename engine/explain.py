"""
=========================================================

Trade Decision Engine (TDE)

Explanation Engine
Version 1.0

Purpose
-------
Explains WHY the engine reached its decision.

This engine NEVER changes decisions.

=========================================================
"""


class ExplanationEngine:

    def __init__(self):

        pass

    # ----------------------------------------------------

    def explain(

        self,

        ema,

        macd,

        rsi,

        consensus,

        conviction,

        decision

    ):

        explanation = []

        # ------------------------------------------------
        # EMA
        # ------------------------------------------------

        explanation.append(

            f"Trend : {ema['decision']['reason']} "
            f"(Score {ema['decision']['score']})"

        )

        # ------------------------------------------------
        # MACD
        # ------------------------------------------------

        explanation.append(

            f"Momentum : {macd['decision']['reason']} "
            f"(Score {macd['decision']['score']})"

        )

        # ------------------------------------------------
        # RSI
        # ------------------------------------------------

        explanation.append(

            f"Risk : {rsi['decision']['reason']} "
            f"(Score {rsi['decision']['score']})"

        )

        # ------------------------------------------------
        # Consensus
        # ------------------------------------------------

        explanation.append(

            f"Consensus Score : {consensus:.1f}/100"

        )

        # ------------------------------------------------
        # Conviction
        # ------------------------------------------------

        explanation.append(

            f"Immediate : {conviction['immediate']}"

        )

        explanation.append(

            f"Context : {conviction['context']}"

        )

        explanation.append(

            f"Persistence : {conviction['persistence']} observations"

        )

        explanation.append(

            f"Velocity : {conviction['velocity']}"

        )

        # ------------------------------------------------
        # Final Decision
        # ------------------------------------------------

        explanation.append("")

        explanation.append(

            f"Decision : {decision['state']}"

        )

        explanation.append(

            decision["recommendation"]

        )

        explanation.append(

            f"Confidence : {decision['confidence']}"

        )

        return "\n".join(explanation)
