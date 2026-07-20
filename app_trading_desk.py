import streamlit as st

from engine.trading_desk_engine import TradingDeskEngine
from ui.trading_desk import draw_trading_desk


st.set_page_config(
    page_title="Trading Desk",
    page_icon="📡",
    layout="wide"
)

st.title("Trading Desk")

from datetime import datetime

engine = TradingDeskEngine()

ticker = "SBIN"      # Temporary
analysis_datetime = datetime.now()   # Temporary

data = engine.analyze(
    ticker,
    analysis_datetime
)

draw_trading_desk(data)
