
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

    # ==========================================================
    # Main Render
    # ==========================================================

    def render(self, dashboard):

        st.title("Trade Decision Engine")

        st.caption("AI Powered Trading Decision Support System")

        st.divider()

        # -----------------------------------
        # Market Overview
        # -----------------------------------

        self.morning_briefing(dashboard)

        st.divider()

        # -----------------------------------
        # Top Opportunities
        # -----------------------------------

        self.today_focus(dashboard)

        st.divider()

        self.keep_an_eye_on(dashboard)

        st.divider()

        # -----------------------------------
        # Ranked Opportunities
        # -----------------------------------

        self.stock_table(dashboard)

        # -----------------------------------
        # Decision Dialog
        # -----------------------------------

        if "selected_stock" in st.session_state:

            self.show_decision_dialog()
    # ==========================================================
    # Market Overview
    # ==========================================================

    def morning_briefing(self, dashboard):

        st.subheader("🌅 Good Morning")

        bias = dashboard.get("market_bias","MIXED")
        confidence = dashboard.get("market_score",0)

        if bias == "BUY":
            st.success(f"🟢 BUY DAY | Confidence : {confidence}/100")
        elif bias == "SELL":
            st.error(f"🔴 SELL DAY | Confidence : {confidence}/100")
        else:
            st.warning(f"🟡 MIXED DAY | Confidence : {confidence}/100")

        st.caption("Today's Focus contains the highest conviction opportunities. Keep an Eye On contains secondary opportunities.")

    # ==========================================================
    # Today's Focus
    # ==========================================================

    def today_focus(self, dashboard):

        st.subheader("🎯 Today's Focus")

        top5 = dashboard["stocks"][:5]
        cols = st.columns(5)

        for col, stock in zip(cols, top5):
            with col:
                with st.container(border=True):
                    ticker = stock["ticker"].replace(".NS","")
                    st.markdown(f"### {ticker}")
                    st.write(stock["status"])
                    st.markdown(f"## {stock['score']}/100")
                    if st.button("🔍 Analyze", key=f"focus_{ticker}"):
                        st.session_state["selected_stock"] = stock
                        st.rerun()

    # ==========================================================
    # Keep an Eye On
    # ==========================================================

    def keep_an_eye_on(self, dashboard):

        st.subheader("👀 Keep an Eye On")

        watch = dashboard["stocks"][5:10]
        if not watch:
            st.info("No secondary opportunities.")
            return

        cols = st.columns(min(5,len(watch)))

        for col, stock in zip(cols, watch):
            with col:
                with st.container(border=True):
                    st.markdown(f"**{stock['ticker'].replace('.NS','')}**")
                    st.caption(stock["status"])
                    st.write(f"{stock['score']}/100")

    # ==========================================================
    # Top 5 Opportunities
    # ==========================================================

    def top_opportunities(self, dashboard):

        st.subheader("🏆 Top 5 Opportunities")

        top5 = dashboard["stocks"][:5]

        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

        cols = st.columns(5)

        for col, medal, stock in zip(cols, medals, top5):

            with col:

                with st.container(border=True):

                    ticker = stock["ticker"].replace(".NS", "")

                    st.markdown(
                        f"<h4 style='text-align:center'>{medal} {ticker}</h4>",
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Status
                    # --------------------------

                    status = stock["status"]

                    if "READY" in status:
                        st.success(status)

                    elif "WAIT" in status:
                        st.warning(status)

                    else:
                        st.error(status)

                    # --------------------------
                    # Trade Score
                    # --------------------------

                    st.markdown(
                        f"""
                        <div style='text-align:center;
                                    font-size:28px;
                                    font-weight:bold;
                                    padding-top:5px;'>
                            {stock["score"]}/100
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Grade
                    # --------------------------

                    st.markdown(
                        f"""
                        <div style='text-align:center;
                                    color:#FFD54F;
                                    font-size:18px;
                                    font-weight:bold;'>
                            {stock["grade"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Stars
                    # --------------------------

                    st.markdown(
                        f"""
                        <div style='text-align:center;
                                    font-size:20px;
                                    padding-top:5px;
                                    padding-bottom:10px;'>
                            {stock["trade"]["stars"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # --------------------------
                    # Analyze Button
                    # --------------------------

                    if st.button(

                        "🔍 Analyze",

                        key=f"analyze_{ticker}"

                    ):

                        st.session_state["selected_stock"] = stock

                        st.rerun()

    # ==========================================================
    # Decision Card
    # ==========================================================

    def show_decision_dialog(self):

        if "selected_stock" not in st.session_state:
            return

        st.divider()

        st.subheader("📊 Decision Analysis")

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

     # ==========================================================
    # Ranked Opportunities
    # ==========================================================

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
