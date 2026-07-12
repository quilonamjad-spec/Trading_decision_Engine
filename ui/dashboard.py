import streamlit as st
import pandas as pd
from ui.components.stock_card_v2 import StockCard

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

        self.top_opportunities(dashboard)

        st.divider()

        self.market_direction(dashboard)

        st.divider()

        self.stock_table(dashboard)
        if "selected_stock" in st.session_state:

            st.divider()
        
            st.header("📊 Decision Card")
        
            stock = st.session_state["selected_stock"]
        
            self.card.render(
        
                ticker=stock["ticker"].replace(".NS",""),
        
                company=stock["ticker"],
        
                price=stock["price"],
        
                change=stock["change"],
        
                pct_change=stock["pct_change"],
        
                trade=stock["trade"],
        
                df=stock["df"]
        
            )
        
        st.divider()
        
        self.card = StockCard()

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

  def top_opportunities(self, dashboard):

    st.subheader("🏆 Top 5 Opportunities")

    top5 = dashboard["stocks"][:5]

    for stock in top5:

        with st.container(border=True):

            c1, c2, c3, c4, c5 = st.columns([3,2,2,2,2])

            with c1:

                st.subheader(stock["ticker"])

            with c2:

                st.metric(

                    "Score",

                    f"{stock['score']}/100"

                )

            with c3:

                st.metric(

                    "Status",

                    stock["status"]

                )

            with c4:

                st.metric(

                    "Direction",

                    stock["direction"]

                )

            with c5:

                if st.button(

                    "▶ Analyze",

                    key=f"analyse_{stock['ticker']}"

                ):

                    st.session_state["selected_stock"] = stock

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
