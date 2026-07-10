import streamlit as st

from ui.styles import load_css
from ui.components.stock_card import StockCard

st.set_page_config(
    page_title="TDE Prototype",
    layout="centered",
)

load_css()

card = StockCard()

card.render(
    ticker="SBIN",
    company="State Bank of India",
    price=1022.60,
    change=-4.60,
    change_percent=-0.45,
    trend="Bearish",
    momentum="Weakening",
    risk="Recovering",
)
