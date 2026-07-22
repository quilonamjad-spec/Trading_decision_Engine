import streamlit as st
import pandas as pd
import altair as alt


class SmartStockCard:

    @staticmethod
    def render(trade):

        score = trade["score"]

        # ---------------------------------
        # Score Color
        # ---------------------------------

        if score >= 90:
            score_color = "#16a34a"      # Green
        elif score >= 80:
            score_color = "#2563eb"      # Blue
        elif score >= 70:
            score_color = "#f59e0b"      # Orange
        else:
            score_color = "#dc2626"      # Red

        # ---------------------------------
        # Header
        # ---------------------------------

        st.markdown(f"""
        <div style="
            border:1px solid #444;
            border-radius:12px;
            padding:15px;
            background:#111827;
        ">
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([2,1])

        with c1:
            st.markdown(f"### {trade['ticker']}")

        with c2:
            st.metric(
                label="Price",
                value=f"₹ {trade['price']}"
            )

        # ---------------------------------
        # Hero Score
        # ---------------------------------

        st.markdown(
            f"""
            <h1 style="
            text-align:center;
            color:{score_color};
            margin-bottom:0px;">
            {score}/100
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center;font-size:18px;'>Trade Health</p>",
            unsafe_allow_html=True
        )

        # ---------------------------------
        # Decision Tiles
        # ---------------------------------

        a, b, c = st.columns(3)

        with a:
            st.metric(
                label="Status",
                value=trade["status"]
            )

        with b:
            st.metric(
                label="Direction",
                value=trade["direction"]
            )

        with c:
            st.metric(
                label="Confidence",
                value=trade["confidence"]
            )

        st.divider()

        # ---------------------------------
        # Evolution Graph
        # ---------------------------------

        df = pd.DataFrame(trade["evolution"])

        chart = (
            alt.Chart(df)
            .mark_line(point=True)
            .encode(
                x=alt.X("time:N", title=None),
                y=alt.Y(
                    "health:Q",
                    scale=alt.Scale(domain=[0,100]),
                    title=None
                )
            )
            .properties(height=130)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

        # ---------------------------------
        # Details
        # ---------------------------------

        with st.expander("Details"):

            st.write("### Current Price")
            st.write(f"₹ {trade['price']}")

            st.write("### Last Candle")
            st.info(trade["last_candle"])

            st.write("### Trade Score")
            st.progress(score / 100)

            st.write("### Raw Output")

            st.json(trade)

        st.markdown("</div>", unsafe_allow_html=True)
