import streamlit as st
import pandas as pd


class CommandCenter:

    """
    =========================================================
    Trade Decision Engine

    Command Center UI
    =========================================================
    """

    def render(self, dashboard):

        st.title("🚀 Trade Decision Engine")
        st.caption("Command Center")

        st.divider()

        self.market_score(dashboard)

        st.divider()

        self.market_summary(dashboard)

        st.divider()

        self.best_trade(dashboard)

        st.divider()

        self.market_direction(dashboard)

        st.divider()

        self.stock_table(dashboard)

    # =====================================================
    # Market Score
    # =====================================================

    def market_score(self, dashboard):

        st.metric(

            label="Market Score",

            value=f"{dashboard['market_score']}/100"

        )

    # =====================================================
    # Summary
    # =====================================================

    def market_summary(self, dashboard):

        st.subheader("📊 Market Summary")

        summary = dashboard["summary"]

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric("🟢 READY",
                  summary["READY"])

        c2.metric("🟡 Minor",
                  summary["READY (Minor Concerns)"])

        c3.metric("🟠 High Risk",
                  summary["READY (High Risk)"])

        c4.metric("🔵 WAIT",
                  summary["WAIT"])

        c5.metric("🔴 AVOID",
                  summary["AVOID"])

    # =====================================================
    # Best Trade
    # =====================================================

    def best_trade(self, dashboard):

        trade = dashboard["best_trade"]

        st.subheader("🏆 Today's Best Opportunity")

        c1, c2, c3 = st.columns(3)

        c1.metric(

            "Ticker",

            trade["ticker"]

        )

        c2.metric(

            "Score",

            f"{trade['score']}/100"

        )

        c3.metric(

            "Status",

            trade["status"]

        )

    # =====================================================
    # Direction Summary
    # =====================================================

    def market_direction(self, dashboard):

        direction = dashboard["direction_summary"]

        st.subheader("🧭 Market Direction")

        c1, c2, c3 = st.columns(3)

        c1.metric("LONG",
                  direction["LONG"])

        c2.metric("SHORT",
                  direction["SHORT"])

        c3.metric("NEUTRAL",
                  direction["NEUTRAL"])

    # =====================================================
    # Ranking Table
    # =====================================================

    def stock_table(self, dashboard):

        st.subheader("📈 Ranked Opportunities")

        rows = []

        for stock in dashboard["stocks"]:

            rows.append({

                "Ticker": stock["ticker"],

                "Score": stock["score"],

                "Grade": stock["grade"],

                "Status": stock["status"],

                "Direction": stock["direction"],

                "Confidence": stock["confidence"]

            })

        df = pd.DataFrame(rows)

        st.dataframe(

            df,

            use_container_width=True,

            hide_index=True

        )
