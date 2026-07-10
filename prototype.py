import streamlit as st

from ui.styles import load_css
from ui.components.stock_card import StockCard

from data.market_data import MarketDataEngine

st.set_page_config(
    page_title="TDE Prototype",
    layout="centered",
)

load_css()

# ------------------------------------
# Download Market Data
# ------------------------------------

market = MarketDataEngine()

market_data = market.download_watchlist()

# Take the first stock from the watchlist
ticker = list(market_data.keys())[0]

df = market_data[ticker]

# ------------------------------------
# Latest Price
# ------------------------------------

price = float(df["Close"].iloc[-1])

previous = float(df["Close"].iloc[-2])

change = price - previous

change_percent = (change / previous) * 100

# ------------------------------------
# Render Card
# ------------------------------------

card = StockCard()

card.render(
    ticker=ticker.replace(".NS", ""),
    company=ticker,
    price=price,
    change=change,
    change_percent=change_percent,
    trend="Bearish",
    momentum="Weakening",
    risk="Recovering",
    df=df,
)
