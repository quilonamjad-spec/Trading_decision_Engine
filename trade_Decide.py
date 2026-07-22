import streamlit as st

st.set_page_config(
    page_title="Trade Decision Engine",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "stocks" not in st.session_state:
    st.session_state.stocks = [
        {"ticker": "", "mode": "Intraday"}
    ]

#----
def analyze_stock(ticker):

    df = market.get_data(ticker)

    ema_result = ema.calculate(df)
    macd_result = macd.calculate(df)
    rsi_result = rsi.calculate(df)

    return trade_engine.evaluate(
        ema_result,
        macd_result,
        rsi_result
    )


# --------------------------------------------------
# ADD STOCK
# --------------------------------------------------

def add_stock():

    if len(st.session_state.stocks) < 4:

        st.session_state.stocks.append(
            {
                "ticker": "",
                "mode": "Intraday"
            }
        )


# --------------------------------------------------
# REMOVE STOCK
# --------------------------------------------------

def remove_stock(index):

    st.session_state.stocks.pop(index)

    if len(st.session_state.stocks) == 0:

        st.session_state.stocks.append(
            {
                "ticker": "",
                "mode": "Intraday"
            }
        )


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Trade Decision Engine")

st.caption(
    "Compare multiple trade opportunities side by side."
)

st.divider()

# --------------------------------------------------
# STOCK CARDS
# --------------------------------------------------

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

        st.button(
            "❌ Remove",
            key=f"remove_{i}",
            on_click=remove_stock,
            args=(i,)
        )

# --------------------------------------------------
# ADD BUTTON
# --------------------------------------------------

st.write("")

left, middle, right = st.columns([1,1,1])

with middle:

    st.button(
        "➕ Add Stock",
        use_container_width=True,
        on_click=add_stock
    )

st.divider()

# --------------------------------------------------
# ANALYZE
# --------------------------------------------------

if st.button(
    "🚀 Analyze",
    use_container_width=True
):

    results = []

for stock in st.session_state.stocks:

    ticker = stock["ticker"].strip()

    if ticker == "":
        continue

    try:

        result = analyze_stock(ticker)

        results.append({
            "ticker": ticker,
            "result": result
        })

    except Exception as e:

        st.error(f"{ticker} : {e}")

    st.write(st.session_state.stocks)
