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
        # Morning Briefing
        # -----------------------------------
    
        self.morning_briefing(dashboard)
    
        st.divider()
    
        # -----------------------------------
        # Top Opportunities
        # -----------------------------------
    
        self.top_opportunities(dashboard)
    
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
        # Morning Briefing
        # ==========================================================
        
        def morning_briefing(self, dashboard):
        
            st.subheader("🌅 Good Morning")
        
            bias = dashboard["market_bias"]
            score = dashboard["market_score"]
        
            if bias == "BUY":
                st.success(f"🟢 BUY DAY   |   Confidence {score}/100")
        
            elif bias == "SELL":
                st.error(f"🔴 SELL DAY   |   Confidence {score}/100")
        
            else:
                st.warning(f"🟡 MIXED DAY   |   Confidence {score}/100")

        # ======================================================
        # Market Score
        # ======================================================

        with score_col:

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

                    label="Overall Score",

                    value=f"{score}/100"

                )

                st.markdown(
                    f"""
                    <div style='text-align:center;
                                font-size:18px;
                                font-weight:bold;
                                padding-top:8px;'>
                        {health}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # ======================================================
        # Market Summary
        # ======================================================

        with summary_col:

            with st.container(border=True):

                st.subheader("📊 Market Summary")

                summary = dashboard["summary"]

                c1, c2, c3 = st.columns(3)

                with c1:

                    st.metric("🟢 READY", summary["READY"])

                    st.metric("🔵 WAIT", summary["WAIT"])

                with c2:

                    st.metric("🟡 Minor", summary["READY (Minor Concerns)"])

                with c3:

                    st.metric("🟠 High Risk", summary["READY (High Risk)"])

                    st.metric("🔴 AVOID", summary["AVOID"])

        # ======================================================
        # Market Direction
        # ======================================================

        with direction_col:

            with st.container(border=True):

                st.subheader("🧭 Market Direction")

                direction = dashboard["direction_summary"]

                st.metric(

                    "📈 LONG",

                    direction["LONG"]

                )

                st.metric(

                    "📉 SHORT",

                    direction["SHORT"]

                )

                st.metric(

                    "➖ NEUTRAL",

                    direction["NEUTRAL"]

                )
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
