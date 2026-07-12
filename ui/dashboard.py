import streamlit as st
import pandas as pd

from ui.components.stock_card_v2 import StockCard


class CommandCenter:

    """
    ============================================================
    Trade Decision Engine
    Command Center
    ============================================================
    """

    def __init__(self):

        self.card = StockCard()

    # ============================================================
    # Main Render
    # ============================================================

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

        # ------------------------------------
        # Decision Card
        # ------------------------------------

        if "selected_stock" in st.session_state:

            st.divider()

            st.header("📊 Decision Card")

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
    # Market Score
    # ============================================================

    def market_score(self, dashboard):

        st.metric(

            label="Market Score",

            value=f"{dashboard['market_score']}/100"

        )

    # ============================================================
    # Market Summary
    # ============================================================

    def market_summary(self, dashboard):

        st.subheader("📊 Market Summary")

        summary = dashboard["summary"]

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:

            st.metric(

                "🟢 READY",

                summary["READY"]

            )

        with c2:

            st.metric(

                "🟡 Minor",

                summary["READY (Minor Concerns)"]

            )

        with c3:

            st.metric(

                "🟠 High Risk",

                summary["READY (High Risk)"]

            )

        with c4:

            st.metric(

                "🔵 WAIT",

                summary["WAIT"]

            )

        with c5:

            st.metric(

                "🔴 AVOID",

                summary["AVOID"]

            )

    # ============================================================
    # Top Opportunities
    # ============================================================

    def top_opportunities(self, dashboard):

        st.subheader("🏆 Top 5 Opportunities")

        top5 = dashboard["stocks"][:5]

        medals = [

            "🥇",

            "🥈",

            "🥉",

            "4️⃣",

            "5️⃣"

        ]

        for medal, stock in zip(medals, top5):

            with st.container(border=True):

                c1, c2, c3, c4, c5 = st.columns([3, 2, 2, 2, 2])

                with c1:

                    st.markdown(

                        f"### {medal} {stock['ticker']}"

                    )

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

                    st.metric(

                        "Confidence",

                        stock["confidence"]

                    )

                    if st.button(

                        "▶ Analyze",

                        key=f"analyse_{stock['ticker']}"

                    ):

                        st.session_state["selected_stock"] = stock

    # ============================================================
    # Market Direction
    # ============================================================

    def market_direction(self, dashboard):

        st.subheader("🧭 Market Direction")

        direction = dashboard["direction_summary"]

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(

                "LONG",

                direction["LONG"]

            )

        with c2:

            st.metric(

                "SHORT",

                direction["SHORT"]

            )

        with c3:

            st.metric(

                "NEUTRAL",

                direction["NEUTRAL"]

            )

    # ============================================================
    # Ranked Opportunities
    # ============================================================

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
