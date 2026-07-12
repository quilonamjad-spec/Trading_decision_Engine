import streamlit as st
import pandas as pd

from ui.components.stock_card_v2 import StockCard


class CommandCenter:

    """
    ============================================================
    Trade Decision Engine

    Command Center v2.0
    ============================================================
    """

    def __init__(self):

        self.card = StockCard()

    # ============================================================
    # Main Render
    # ============================================================

    def render(self, dashboard):

        st.title("Trade Decision Engine")

        st.caption("AI Powered Trading Decision Support System")

        st.divider()

        self.market_overview(dashboard)

        st.divider()

        self.top_opportunities(dashboard)

        st.divider()

        self.stock_table(dashboard)

        # -----------------------------
        # Decision Dialog
        # -----------------------------

        if "selected_stock" in st.session_state:

            self.show_decision_dialog()

    # ============================================================
    # Market Overview
    # ============================================================

    def market_overview(self, dashboard):

        col1, col2, col3 = st.columns(3)

        # ------------------------------------
        # Market Score
        # ------------------------------------

        with col1:

            with st.container(border=True):

                st.subheader("📈 Market Score")

                score = dashboard["market_score"]

                if score >= 90:
                    health = "🟢 Excellent"

                elif score >= 80:
                    health = "🟢 Strong"

                elif score >= 70:
                    health = "🟡 Good"

                elif score >= 60:
                    health = "🟠 Weak"

                else:
                    health = "🔴 Poor"

                st.metric(

                    "Overall",

                    f"{score}/100"

                )

                st.success(health)

        # ------------------------------------
        # Market Summary
        # ------------------------------------

        with col2:

            with st.container(border=True):

                st.subheader("📊 Market Summary")

                summary = dashboard["summary"]

                st.metric(

                    "🟢 READY",

                    summary["READY"]

                )

                st.metric(

                    "🟡 Minor",

                    summary["READY (Minor Concerns)"]

                )

                st.metric(

                    "🟠 High Risk",

                    summary["READY (High Risk)"]

                )

                st.metric(

                    "🔵 WAIT",

                    summary["WAIT"]

                )

                st.metric(

                    "🔴 AVOID",

                    summary["AVOID"]

                )

        # ------------------------------------
        # Market Direction
        # ------------------------------------

        with col3:

            with st.container(border=True):

                st.subheader("🧭 Market Direction")

                direction = dashboard["direction_summary"]

                st.metric(

                    "LONG",

                    direction["LONG"]

                )

                st.metric(

                    "SHORT",

                    direction["SHORT"]

                )

                st.metric(

                    "NEUTRAL",

                    direction["NEUTRAL"]

                )

    # ============================================================
    # Top Opportunities
    # ============================================================

    def top_opportunities(self, dashboard):

        st.subheader("🏆 Top 5 Opportunities")

        top5 = dashboard["stocks"][:5]

        cols = st.columns(5)

        medals = [

            "🥇",

            "🥈",

            "🥉",

            "4️⃣",

            "5️⃣"

        ]

        for col, medal, stock in zip(cols, medals, top5):

            with col:

                with st.container(border=True):

                    st.markdown(

                        f"### {medal} {stock['ticker'].replace('.NS','')}"

                    )

                    status = stock["status"]

                    if "READY" in status:
                    
                        st.success(status)
                    
                    elif "WAIT" in status:
                    
                        st.warning(status)
                    
                    else:
                    
                        st.error(status)

                    st.markdown(

                        f"## {stock['score']}/100"

                    )

                    st.markdown(

                        f"**{stock['grade']}**"

                    )

                     st.markdown(

                        f"<h3 style='text-align:center'>{stock['trade']['stars']}</h3>",
                    
                        unsafe_allow_html=True
                    
                    )

                    if st.button(

                        "📊 Analyze",

                        key=f"analyse_{stock['ticker']}"

                    ):

                        st.session_state["selected_stock"] = stock

                        st.rerun()

        # ============================================================
        # Decision Dialog
        # ============================================================
        
        @st.dialog("📊 Decision Analysis", width="large")
        def show_decision_dialog(self):
        
            stock = st.session_state["selected_stock"]
        
            self.card.render(
        
                ticker=stock["ticker"].replace(".NS", ""),
        
                company=stock["ticker"],
        
                price=stock["price"],
        
                change=stock["change"],
        
                pct_change=stock["pct_change"],
        
                trade=stock["trade"],
        
                df=stock["df"]
        
            )
        
        
        # ============================================================
        # Ranked Opportunities
        # ============================================================
        
        def stock_table(self, dashboard):
        
            st.subheader("📈 Ranked Opportunities")
        
            rows = []
        
            for stock in dashboard["stocks"]:
        
                rows.append({
        
                    "Ticker": stock["ticker"].replace(".NS", ""),
        
                    "Score": stock["score"],
        
                    "Grade": stock["grade"],
        
                    "Status": stock["status"],
        
                    "Direction": stock["direction"],
        
                    "Confidence": stock["confidence"]
        
                })
        
            df = pd.DataFrame(rows)
        
            st.dataframe(
        
                df,
        
                hide_index=True,
        
                use_container_width=True
        
            )
