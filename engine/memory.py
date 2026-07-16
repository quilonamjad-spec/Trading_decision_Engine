"""
=========================================================

Trade Decision Engine (TDE)

Decision Memory
Version 1.0

Purpose:
Stores the recent decision history of every stock.

The Memory Engine DOES NOT make decisions.
It only remembers.

=========================================================
"""

from collections import deque
from datetime import datetime


class DecisionMemory:

    def __init__(self, max_history=12):

        # Last N observations
        self.max_history = max_history

        # Memory for every stock
        self.memory = {}

    # -----------------------------------------------------

    def record(

        self,

        symbol,

        consensus,

        trade_score,

        status,

        reason=""

    ):

        """
        Store one observation.
        """

        if symbol not in self.memory:

            self.memory[symbol] = deque(maxlen=self.max_history)

        self.memory[symbol].append(

            {

                "time": datetime.now(),

                "consensus": consensus,

                "trade_score": trade_score,

                "status": status,

                "reason": reason

            }

        )

    # -----------------------------------------------------

    def history(self, symbol):

        """
        Return complete history.
        """

        if symbol not in self.memory:

            return []

        return list(self.memory[symbol])

    # -----------------------------------------------------

    def latest(self, symbol):

        """
        Return latest observation.
        """

        history = self.history(symbol)

        if not history:

            return None

        return history[-1]

    # -----------------------------------------------------

    def previous(self, symbol):

        """
        Return previous observation.
        """

        history = self.history(symbol)

        if len(history) < 2:

            return None

        return history[-2]

    # -----------------------------------------------------

    def clear(self, symbol=None):

        """
        Clear memory.
        """

        if symbol:

            self.memory.pop(symbol, None)

        else:

            self.memory.clear()

    # -----------------------------------------------------

    def size(self, symbol):

        """
        Number of observations.
        """

        return len(self.history(symbol))
