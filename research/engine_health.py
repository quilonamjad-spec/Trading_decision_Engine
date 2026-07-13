"""
====================================================

Trade Decision Engine (TDE)

Engine Health Monitor

Research Framework

====================================================
"""


class EngineHealth:

    def __init__(self):

        self.reset()

    # -------------------------------------------------

    def reset(self):

        self.total_stocks = 0

        self.trend_total = 0
        self.momentum_total = 0
        self.risk_total = 0

        self.final_total = 0

        self.ready = 0
        self.minor = 0
        self.wait = 0
        self.avoid = 0

    # -------------------------------------------------

    def add_stock(
        self,
        trend_score,
        momentum_score,
        risk_score,
        final_score,
        status
    ):

        self.total_stocks += 1

        self.trend_total += trend_score
        self.momentum_total += momentum_score
        self.risk_total += risk_score

        self.final_total += final_score

        status = status.lower()

        if "ready" in status and "minor" not in status:
            self.ready += 1

        elif "minor" in status:
            self.minor += 1

        elif "wait" in status:
            self.wait += 1

        else:
            self.avoid += 1

    # -------------------------------------------------

    def average(self, value):

        if self.total_stocks == 0:
            return 0

        return round(value / self.total_stocks, 2)

    # -------------------------------------------------

    def report(self):

        print()

        print("=" * 55)
        print("        TDE ENGINE HEALTH REPORT")
        print("=" * 55)

        print()

        print(f"Stocks Analysed : {self.total_stocks}")

        print()

        print("Expert Contribution")

        print(
            f"Trend      : {self.average(self.trend_total)} / 35"
        )

        print(
            f"Momentum   : {self.average(self.momentum_total)} / 35"
        )

        print(
            f"Risk       : {self.average(self.risk_total)} / 30"
        )

        print()

        print(
            f"Average Final Score : "
            f"{self.average(self.final_total)}"
        )

        print()

        print("Status Distribution")

        print(f"READY : {self.ready}")
        print(f"Minor : {self.minor}")
        print(f"WAIT  : {self.wait}")
        print(f"AVOID : {self.avoid}")

        print()

        print("=" * 55)

        print()

    # -------------------------------------------------

    def summary(self):

        return {

            "stocks": self.total_stocks,

            "trend_average": self.average(
                self.trend_total
            ),

            "momentum_average": self.average(
                self.momentum_total
            ),

            "risk_average": self.average(
                self.risk_total
            ),

            "average_score": self.average(
                self.final_total
            ),

            "ready": self.ready,

            "minor": self.minor,

            "wait": self.wait,

            "avoid": self.avoid

        }
