"""
=========================================================
Trade Decision Engine (TDE)

Dashboard Engine
Version : 3.0
=========================================================
"""

from research.engine_health import EngineHealth

from engine.gatekeeper import Gatekeeper
from engine.memory import DecisionMemory
from engine.conviction import ConvictionEngine

gatekeeper = Gatekeeper()
memory = DecisionMemory()
conviction_engine = ConvictionEngine()


class DashboardEngine:

    """
    Dashboard Engine

    Responsibilities

    • Build complete market dashboard
    • Analyze one stock
    • Analyze entire universe
    • Prepare watchlists
    • Produce market statistics
    """

    # ---------------------------------------------------------
    # Build Complete Dashboard
    # ---------------------------------------------------------

    def build(
        self,
        market_data,
        trade_engine,
        ema,
        macd,
        rsi
    ):

        dashboard = []

        health = EngineHealth()

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

        # -------------------------------------------------
        # Analyse Every Stock
        # -------------------------------------------------

        for ticker, df in market_data.items():

            stock = self.analyze_stock(

                ticker=ticker,

                df=df,

                trade_engine=trade_engine,

                ema=ema,

                macd=macd,

                rsi=rsi,

                health=health

            )

            dashboard.append(stock)

            trade = stock["trade"]

            summary[trade["status"]] += 1

            direction_summary[trade["direction"]] += 1

            confidence_summary[trade["confidence"]] += 1

            total_score += trade["score"]

        # -------------------------------------------------
        # Sort
        # -------------------------------------------------

        dashboard.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        # -------------------------------------------------
        # Watchlists
        # -------------------------------------------------

        buy_list = [

            stock

            for stock in dashboard

            if stock["direction"] == "LONG"

        ][:5]

        sell_list = [

            stock

            for stock in dashboard

            if stock["direction"] == "SHORT"

        ][:5]

        # -------------------------------------------------
        # Market Bias
        # -------------------------------------------------

        long_count = direction_summary["LONG"]
        short_count = direction_summary["SHORT"]

        if long_count > short_count:

            market_bias = "BUY"

        elif short_count > long_count:

            market_bias = "SELL"

        else:

            market_bias = "MIXED"

        # -------------------------------------------------
        # Market Score
        # -------------------------------------------------

        if dashboard:

            market_score = round(

                total_score / len(dashboard),

                1

            )

            best_trade = dashboard[0]

        else:

            market_score = 0

            best_trade = None

        # -------------------------------------------------
        # Diagnostics
        # -------------------------------------------------

        health.report()

        # -------------------------------------------------
        # Dashboard Intelligence
        # -------------------------------------------------

        return {

            "summary": summary,

            "market_score": market_score,

            "best_trade": best_trade,

            "direction_summary": direction_summary,

            "confidence_summary": confidence_summary,

            "market_bias": market_bias,

            "primary_watchlist": buy_list,

            "secondary_watchlist": sell_list,

            "stocks": dashboard

        }

    # =====================================================
    # Analyse One Stock
    # =====================================================

    def analyze_stock(

        self,

        ticker,

        df,

        trade_engine,

        ema,

        macd,

        rsi,

        health=None

    ):

        # --------------------------------------------
        # Indicator Engines
        # --------------------------------------------

        ema_result = ema.calculate(df)

        macd_result = macd.calculate(df)

        rsi_result = rsi.calculate(df)

        # --------------------------------------------
        # Trade Quality
        # --------------------------------------------

        trade = trade_engine.evaluate(

            ema_result,

            macd_result,

            rsi_result

        )

        # --------------------------------------------
        # Decision Memory
        # --------------------------------------------

        memory.record(

            symbol=ticker,

            consensus=trade["consensus"]["confidence_score"],

            trade_score=trade["score"],

            status=trade["status"],

            reason=", ".join(trade["evidence"])

        )

        history = memory.history(ticker)

        conviction = conviction_engine.evaluate(history)

        # --------------------------------------------
        # Engine Health
        # --------------------------------------------

        if health is not None:

            health.add_stock(

                trend_score=ema_result["decision"]["score"],

                momentum_score=macd_result["decision"]["score"],

                risk_score=rsi_result["decision"]["score"],

                final_score=trade["score"],

                status=trade["status"]

            )

        # --------------------------------------------
        # Price Information
        # --------------------------------------------

        latest = df.iloc[-1]

        previous = df.iloc[-2]

        price = float(latest["Close"])

        previous_price = float(previous["Close"])

        change = price - previous_price

        pct_change = (change / previous_price) * 100
    
        # --------------------------------------------
        # Dashboard Row
        # --------------------------------------------

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

            "conviction": conviction,

            "trade": trade,

            "df": df

        }

        return row

    # =====================================================
    # Analyse a Single Stock
    # =====================================================

    def analyze_single_stock(

        self,

        ticker,

        market_data_engine,

        trade_engine,

        ema,

        macd,

        rsi

    ):

        """
        Used by:

        • My Ideas
        • Manual Stock Analysis
        • Future Commit Trade Screen

        Returns exactly the same object that build()
        stores inside dashboard["stocks"].
        """

        ticker = ticker.upper().strip()

        try:

            df = market_data_engine.download_stock(ticker)

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

        if df is None:

            return {

                "success": False,

                "message": f"No data available for {ticker}"

            }

        if len(df) < 60:

            return {

                "success": False,

                "message": "Not enough candles available."

            }

        stock = self.analyze_stock(

            ticker=ticker,

            df=df,

            trade_engine=trade_engine,

            ema=ema,

            macd=macd,

            rsi=rsi

        )

        # --------------------------------------------
        # Metadata
        # --------------------------------------------

        stock["success"] = True

        stock["source"] = "Manual Analysis"

        stock["analysis_type"] = "My Ideas"

        stock["timestamp"] = df.index[-1]

        return stock
