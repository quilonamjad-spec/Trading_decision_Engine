"""
=========================================================
Trade Decision Engine (TDE)

Dashboard Engine
Version : 2.0
=========================================================
"""
from research.engine_health import EngineHealth

class DashboardEngine:

    """
    Builds the Market Dashboard from all
    Trade Quality results.
    """

    def build(self, market_data, trade_engine, ema, macd, rsi):

        dashboard = []
        health = EngineHealth()

        # ----------------------------------------
        # Dashboard Summary
        # ----------------------------------------

        summary = {

            "READY": 0,

            "READY (Minor Concerns)": 0,

            "READY (High Risk)": 0,

            "WAIT": 0,

            "AVOID": 0

        }

        direction_summary = {

            "LONG": 0,

            "SHORT": 0,

            "NEUTRAL": 0

        }

        confidence_summary = {

            "High": 0,

            "Medium": 0,

            "Low": 0

        }

        total_score = 0

        # ----------------------------------------
        # Process Every Stock
        # ----------------------------------------

        for ticker, df in market_data.items():

            # ------------------------------------
            # Indicator Engines
            # ------------------------------------

            ema_result = ema.calculate(df)

            macd_result = macd.calculate(df)

            rsi_result = rsi.calculate(df)

            # ------------------------------------
            # Trade Quality
            # ------------------------------------

            trade = trade_engine.evaluate(

                ema_result,

                macd_result,

                rsi_result
            )
                # ------------------------------------
                # Engine Health Monitor
                # ------------------------------------
                
                health.add_stock(
                
                    trend_score=ema_result["decision"]["score"],
                
                    momentum_score=macd_result["decision"]["score"],
                
                    risk_score=rsi_result["decision"]["score"],
                
                    final_score=trade["score"],
                
                    status=trade["status"]
                
                )

            )

            # ------------------------------------
            # Latest Price
            # ------------------------------------

            latest = df.iloc[-1]

            previous = df.iloc[-2]

            price = float(latest["Close"])

            change = price - float(previous["Close"])

            pct_change = (

                change /
                float(previous["Close"])

            ) * 100

            # ------------------------------------
            # Dashboard Row
            # ------------------------------------

            row = {

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

            }

            dashboard.append(row)

            # ------------------------------------
            # Update Summary
            # ------------------------------------

            summary[trade["status"]] += 1

            direction_summary[trade["direction"]] += 1

            confidence_summary[trade["confidence"]] += 1

            total_score += trade["score"]

        # ----------------------------------------
        # Sort Dashboard
        # ----------------------------------------

        dashboard.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        # ----------------------------------------
        # Market Statistics
        # ----------------------------------------

        market_score = round(

            total_score / len(dashboard),

            1

        )

        best_trade = dashboard[0]
        # ----------------------------------------
        # Engine Diagnostics
        # ----------------------------------------
        
        health.report()

        # ----------------------------------------
        # Return Dashboard Intelligence
        # ----------------------------------------

        return {

            "summary": summary,

            "market_score": market_score,

            "best_trade": best_trade,

            "direction_summary": direction_summary,

            "confidence_summary": confidence_summary,

            "stocks": dashboard

        }
