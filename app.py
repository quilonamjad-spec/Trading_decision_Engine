import streamlit as st

from data.market_data import MarketDataEngine
from engine.indicator_engine import IndicatorEngine
from ui.dashboard import Dashboard

st.set_page_config(
    page_title="Trade Decision Engine",
    layout="wide"
)

st.title("📈 Trade Decision Engine")
st.caption("Version 0.4")

# -------------------------------------

market = MarketDataEngine().download_watchlist()

analysis = IndicatorEngine().analyse_market(market)

dashboard = Dashboard()

# -------------------------------------

cols = st.columns(3)

i = 0

for ticker, result in analysis.items():

    with cols[i % 3]:

        dashboard.show_stock_card(
            ticker,
            result
        )

    i += 1
