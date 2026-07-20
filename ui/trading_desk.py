import streamlit as st
import pandas as pd


def draw_header(data):
    st.subheader(f"📡 {data['ticker']}")


def draw_score(data):
    col1, col2 = st.columns([1, 3])

    with col1:
        st.metric("Trade Quality", f"{data['score']}/100")

    with col2:
        st.write("")
        st.write(f"**Last Updated:** {data['last_update']}")


def draw_trend_chart(data):
    st.markdown("### Confidence & Consensus")

    df = pd.DataFrame({
        "Confidence": data["confidence"],
        "Consensus": data["consensus"]
    })

    st.line_chart(df)


def draw_reasons(data):
    st.markdown("### Reason")

    for reason in data["reasons"]:
        st.write(f"• {reason}")


def draw_recommendation(data):
    st.markdown("### Recommendation")

    st.success(data["recommendation"])

    st.write(data["message"])


def draw_trading_desk(data):

    draw_header(data)

    draw_score(data)

    st.divider()

    draw_trend_chart(data)

    st.divider()

    draw_reasons(data)

    st.divider()

    draw_recommendation(data)
