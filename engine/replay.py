"""
=========================================================

Trade Decision Engine (TDE)

Replay Engine
Version : 1.0

Purpose
-------
Replays a historical trading session candle by candle.

The Replay Engine NEVER analyses the market.
It simply feeds historical data into the Pipeline
and stores the results.

=========================================================
"""

from datetime import time
import pandas as pd


class ReplayEngine:

    def __init__(self, pipeline, verbose=False):

        self.pipeline = pipeline
        self.verbose = verbose

    # -------------------------------------------------

    def log(self, message):

        if self.verbose:
            print(message)

    # -------------------------------------------------

    def run(

        self,

        symbol,

        df,

        start_time,

        end_time

    ):

        """
        Parameters
        ----------
        symbol : str

        df : DataFrame
            Historical OHLCV dataframe.
            Index must be DatetimeIndex.

        start_time : str
            Example : "09:30"

        end_time : str
            Example : "12:30"

        Returns
        -------
        list
            Complete replay timeline.
        """

        if df.empty:

            raise ValueError("Empty dataframe supplied.")

        if not isinstance(df.index, pd.DatetimeIndex):

            raise ValueError(
                "DataFrame index must be DatetimeIndex."
            )

        start = pd.to_datetime(start_time).time()
        end = pd.to_datetime(end_time).time()

        timeline = []

        # ---------------------------------------------

        replay_df = df.between_time(

            start.strftime("%H:%M"),

            end.strftime("%H:%M")

        )

        self.log(
            f"{len(replay_df)} replay candles selected."
        )

        # ---------------------------------------------

        for timestamp in replay_df.index:

            current_df = df.loc[:timestamp]

            self.log(

                f"Processing {timestamp}"

            )

            result = self.pipeline.evaluate(

                symbol=symbol,

                df=current_df

            )

            timeline.append(

                {

                    "timestamp": timestamp,

                    "time": timestamp.strftime("%H:%M"),

                    "decision":
                        result["decision"]["state"],

                    "trade_score":
                        result["trade_quality"]["score"],

                    "consensus":
                        result["consensus"]["consensus"],

                    "conviction":
                        result["conviction"]["context"],

                    "result":
                        result

                }

            )

        self.log(

            f"Replay completed."

        )

        return timeline
