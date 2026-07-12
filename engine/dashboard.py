"""
=========================================================
Trade Decision Engine (TDE)

Dashboard Engine
Version : 1.0
=========================================================
"""


class DashboardEngine:

    """
    Creates a ranked dashboard from all
    Trade Quality results.
    """

    def build(self, market_data, trade_engine, ema, macd, rsi):

        dashboard = []

        for ticker, df in market_data.items():

            # -----------------------------
            # Expert Results
            # -----------------------------

            ema_result = ema.calculate(df)

            macd_result = macd.calculate(df)

            rsi_result = rsi.calculate(df)

            # -----------------------------
            # Trade Quality
            # -----------------------------

            trade = trade_engine.evaluate(

                ema_result,
                macd_result,
                rsi_result

            )

            # -----------------------------
            # Latest Price
            # -----------------------------

            latest = df.iloc[-1]
            previous = df.iloc[-2]

            price = float(latest["Close"])

            change = price - float(previous["Close"])

            pct_change = (
                change /
                float(previous["Close"])
            ) * 100

            # -----------------------------
            # Dashboard Row
            # -----------------------------

            dashboard.append({

                "ticker": ticker,

                "price": price,

                "change": change,

                "pct_change": pct_change,

                "score": trade["score"],

                "grade": trade["grade"],

                "status": trade["status"],

                "direction": trade["direction"],

                "confidence": trade["confidence"],

                "trade": trade,

                "df": df

            })

        # -----------------------------------
        # Highest Score First
        # -----------------------------------

        dashboard.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return dashboard
