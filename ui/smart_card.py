import streamlit as st
import pandas as pd
import altair as alt


class SmartStockCard:

    # =====================================
    # STATUS BADGE
    # =====================================

    @staticmethod
    def status_badge(status):

        text = status.upper()

        if "READY" in text:
            bg = "#14532d"
            fg = "#86efac"
            icon = "🟢"

        elif "AVOID" in text:
            bg = "#7f1d1d"
            fg = "#fecaca"
            icon = "🔴"

        elif "WAIT" in text:
            bg = "#78350f"
            fg = "#fde68a"
            icon = "🟡"

        else:
            bg = "#374151"
            fg = "white"
            icon = "⚪"

        if "(" in text:
            text = text.split("(")[0].strip()

        st.markdown(
            f"""
            <div style="
                background:{bg};
                color:{fg};
                padding:10px;
                border-radius:8px;
                text-align:center;
                font-weight:bold;
                font-size:18px;
            ">
                {icon} {text}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================
    # DIRECTION BADGE
    # =====================================

    @staticmethod
    def direction_badge(direction):

        direction = direction.upper()

        if direction == "LONG":
            bg = "#1d4ed8"
            fg = "white"
            icon = "📈"

        elif direction == "SHORT":
            bg = "#7e22ce"
            fg = "white"
            icon = "📉"

        else:
            bg = "#374151"
            fg = "white"
            icon = "➖"

        st.markdown(
            f"""
            <div style="
                background:{bg};
                color:{fg};
                padding:10px;
                border-radius:8px;
                text-align:center;
                font-weight:bold;
                font-size:18px;
            ">
                {icon} {direction}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================
    # CONFIDENCE BADGE
    # =====================================

    @staticmethod
    def confidence_badge(confidence):

        confidence = confidence.upper()

        if confidence == "HIGH":
            bg = "#14532d"
            fg = "#bbf7d0"

        elif confidence == "MEDIUM":
            bg = "#78350f"
            fg = "#fde68a"

        else:
            bg = "#7f1d1d"
            fg = "#fecaca"

        st.markdown(
            f"""
            <div style="
                background:{bg};
                color:{fg};
                padding:10px;
                border-radius:8px;
                text-align:center;
                font-weight:bold;
                font-size:18px;
            ">
                {confidence}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================
    # MAIN RENDER
    # =====================================

    @staticmethod
    def render(trade):

        score = trade["score"]

        # Trade Health Colour

        if score >= 90:
            score_color = "#16a34a"

        elif score >= 80:
            score_color = "#2563eb"

        elif score >= 70:
            score_color = "#f59e0b"

        else:
            score_color = "#ef4444"

        # -----------------------------
        # Header
        # -----------------------------

        c1, c2 = st.columns([2, 1])

        with c1:
            st.markdown(f"## {trade['ticker']}")

        with c2:
            st.metric(
                "Price",
                f"₹ {trade['price']}"
            )

        # -----------------------------
        # Hero Score
        # -----------------------------

        st.markdown(
            f"""
            <h1 style="
                text-align:center;
                color:{score_color};
                margin-bottom:0;
            ">
                {score}/100
            </h1>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='text-align:center;font-size:20px;'>Trade Health</div>",
            unsafe_allow_html=True,
        )

        st.write("")

        # -----------------------------
        # Status Row
        # -----------------------------

        c1, c2, c3 = st.columns(3)

        with c1:
            st.caption("Status")
            SmartStockCard.status_badge(trade["status"])

        with c2:
            st.caption("Direction")
            SmartStockCard.direction_badge(trade["direction"])

        with c3:
            st.caption("Confidence")
            SmartStockCard.confidence_badge(trade["confidence"])

        st.write("")

        # -----------------------------
        # Evolution Graph
        # -----------------------------

        df = pd.DataFrame(trade["evolution"])

        chart = (
            alt.Chart(df)
            .mark_line(point=True)
            .encode(
                x=alt.X("time:N", title=None),
                y=alt.Y(
                    "health:Q",
                    scale=alt.Scale(domain=[0, 100]),
                    title=None,
                ),
            )
            .properties(height=140)
        )

        st.altair_chart(chart, use_container_width=True)

        # -----------------------------
        # Details
        # -----------------------------

        with st.expander("Details"):

            st.write(f"### Current Price : ₹ {trade['price']}")

            st.write(f"### Last Candle")
            st.info(trade["last_candle"])

            st.write("### Trade Health")
            st.progress(score / 100)

            st.write("### Raw Engine Output")

            st.json(trade)
