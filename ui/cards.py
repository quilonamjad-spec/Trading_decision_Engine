# --------------------------------------------
# Trade Decision Engine
# Version : 0.3
# ui/cards.py
# --------------------------------------------

import streamlit as st


# ---------------------------------------------------------
# ICONS
# ---------------------------------------------------------

RANK_ICONS = {
    1: "🥇",
    2: "🥈",
    3: "🥉"
}

RECOMMENDATION_ICON = {
    "BUY": "🟢",
    "WAIT": "🟡",
    "SELL": "🔴"
}

TREND_ICON = {
    "Bullish": "🟢",
    "Bearish": "🔴",
    "Sideways": "🟡",
    "Neutral": "⚪"
}

MOMENTUM_ICON = {
    "Strong": "🟢",
    "Weak": "🔴",
    "Neutral": "⚪"
}

VOLUME_ICON = {
    "High": "🟢",
    "Above Avg": "🟢",
    "Average": "🟡",
    "Below Avg": "🔴",
    "Low": "🔴"
}


# ---------------------------------------------------------
# STAR RATING
# ---------------------------------------------------------

def get_rating(score):

    if score >= 90:
        return "★★★★★"

    elif score >= 75:
        return "★★★★☆"

    elif score >= 60:
        return "★★★☆☆"

    elif score >= 40:
        return "★★☆☆☆"

    else:
        return "★☆☆☆☆"


# ---------------------------------------------------------
# STOCK CARD
# ---------------------------------------------------------

def stock_card(stock):

    rank = stock["rank"]

    ticker = stock["ticker"]

    company = stock["company"]

    recommendation = stock["recommendation"]

    score = stock["score"]

    price = stock["price"]

    change = stock["change"]

    trend = stock["trend"]

    momentum = stock["momentum"]

    volume = stock["volume"]

    rank_icon = RANK_ICONS.get(rank, str(rank))

    recommendation_icon = RECOMMENDATION_ICON[recommendation]

    with st.container(border=True):

        # -------------------------------------

        st.subheader(f"{rank_icon} {ticker}")

        st.caption(company)

        # -------------------------------------

        left, right = st.columns([2,1])

        with left:

            st.markdown(
                f"## {recommendation_icon} {recommendation}"
            )

        with right:

            st.metric(
                "Score",
                f"{score}%"
            )

        # -------------------------------------

        st.progress(score/100)

        # -------------------------------------

        st.metric(

            "Current Price",

            f"₹ {price:.2f}",

            change

        )

        st.divider()

        # -------------------------------------

        st.write(

            f"Trend : {TREND_ICON[trend]} **{trend}**"

        )

        st.write(

            f"Momentum : {MOMENTUM_ICON[momentum]} **{momentum}**"

        )

        st.write(

            f"Volume : {VOLUME_ICON[volume]} **{volume}**"

        )

        st.divider()

        st.markdown(

            f"### {get_rating(score)}"

        )

        if score >= 90:

            st.success("Excellent Setup")

        elif score >= 75:

            st.success("Good Opportunity")

        elif score >= 60:

            st.warning("Watch Carefully")

        elif score >= 40:

            st.warning("Weak Setup")

        else:

            st.error("Avoid")