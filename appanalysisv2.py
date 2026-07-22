import streamlit as st

from decision_engine import analyze_stock


# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Trade Decision Engine",
    page_icon="📊",
    layout="wide"
)


# ======================================================
# SESSION STATE
# ======================================================

if "stocks" not in st.session_state:
    st.session_state.stocks = [
        {
            "ticker": "",
            "mode": "Intraday"
        }
    ]

if "results" not in st.session_state:
    st.session_state.results = []


# ======================================================
# FUNCTIONS
# ======================================================

MAX_STOCKS = 4


def add_stock():

    if len(st.session_state.stocks) < MAX_STOCKS:

        st.session_state.stocks.append(
            {
                "ticker": "",
                "mode": "Intraday"
            }
        )


def remove_stock(index):

    st.session_state.stocks.pop(index)

    if len(st.session_state.stocks) == 0:

        st.session_state.stocks.append(
            {
                "ticker": "",
                "mode": "Intraday"
            }
        )


# ======================================================
# TITLE
# ======================================================

st.title("📊 Trade Decision Engine")

st.caption(
    "Compare multiple trade opportunities side by side."
)

st.divider()


# ======================================================
# STOCK INPUT CARDS
# ======================================================

cols = st.columns(len(st.session_state.stocks))

for i, col in enumerate(cols):

    with col:

        st.subheader(f"Stock {i+1}")

        st.session_state.stocks[i]["ticker"] = st.text_input(
            "Ticker",
            value=st.session_state.stocks[i]["ticker"],
            key=f"ticker_{i}"
        )

        st.session_state.stocks[i]["mode"] = st.selectbox(
            "Analyze As",
            [
                "Intraday",
                "Swing",
                "Positional"
            ],
            key=f"mode_{i}"
        )

        if len(st.session_state.stocks) > 1:

            st.button(
                "❌ Remove",
                key=f"remove_{i}",
                on_click=remove_stock,
                args=(i,)
            )


# ======================================================
# ADD STOCK BUTTON
# ======================================================

st.write("")

c1, c2, c3 = st.columns([1,1,1])

with c2:

    if len(st.session_state.stocks) < MAX_STOCKS:

        st.button(
            "➕ Add Stock",
            use_container_width=True,
            on_click=add_stock
        )


st.divider()


# ======================================================
# ANALYZE
# ======================================================

if st.button(
    "🚀 Analyze",
    use_container_width=True
):

    st.session_state.results = []

    progress = st.progress(0)

    total = len(st.session_state.stocks)

    completed = 0

    for stock in st.session_state.stocks:

        ticker = stock["ticker"].strip()

        if ticker == "":
            continue

        try:

            result = analyze_stock(ticker)

            st.session_state.results.append(result)

        except Exception as e:

            st.error(f"{ticker} : {e}")

        completed += 1

        progress.progress(completed / total)

    progress.empty()


# ======================================================
# RESULTS
# ======================================================

if len(st.session_state.results):

    st.divider()

    st.header("Trade Decisions")

    cols = st.columns(len(st.session_state.results))
    from ui.smart_card import SmartStockCard

    for col, trade in zip(cols, st.session_state.results):

        with col:

            SmartStockCard.render(trade)

            st.metric(
                "Trade Health",
                f'{trade["score"]}/100'
            )

            #st.write("### Status")
            #st.success(trade["status"])

           # st.write("### Direction")
            #st.info(trade["direction"])

            #st.write("### Confidence")
            #st.write(trade["confidence"])

            #st.write("### Current Price")
            #st.write(f"₹ {trade['price']}")

            #st.write("### Last Candle")
            #st.caption(trade["last_candle"])

            #import pandas as pd
            #import altair as alt

            st.write("### 📈 Engine Evolution")

            df = pd.DataFrame(trade["evolution"])

            chart = (
                alt.Chart(df)
                .mark_line(point=True)
                .encode(
                    x=alt.X("time:N", title="Time"),
                    y=alt.Y("health:Q", scale=alt.Scale(domain=[0, 100]), title="Trade Health")
                )
                .properties(height=220)
            )

            st.altair_chart(chart, use_container_width=True)
            st.button(
                "📊 View Details",
                key=f"details_{trade['ticker']}"
            )
