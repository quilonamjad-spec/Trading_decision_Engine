import streamlit as st

from ui.styles import load_css
from ui.components.stock_card import StockCard

# Backend
from data.market_data import MarketDataEngine
from indicators.ema import EMAEngine

# ---------------------------------------------------
# Page
# ---------------------------------------------------

st.set_page_config(
    page_title="TDE Prototype",
    layout="centered",
)

load_css()

# ---------------------------------------------------
# Download Market Data
# ---------------------------------------------------

market = MarketDataEngine()

data = market.download_data(["SBIN.NS"])

df = data["SBIN.NS"]

# ---------------------------------------------------
# Calculate EMA20
# ---------------------------------------------------

ema = EMAEngine()

df = ema.calculate(df)

# ---------------------------------------------------
# Latest Values
# ---------------------------------------------------

price = df["Close"].iloc[-1]

previous = df["Close"].iloc[-2]

change = price - previous

change_percent = (change / previous) * 100

# ---------------------------------------------------
# Render Card
# ---------------------------------------------------

card = StockCard()

card.render(
    ticker="SBIN",
    company="State Bank of India",
    price=price,
    change=change,
    change_percent=change_percent,
    trend="Bearish",
    momentum="Weakening",
    risk="Recovering",
    df=df,                # <-- New parameter
)
