import streamlit as st

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Trade Decision Engine",

    page_icon="📈",

    layout="wide"

)

# ==========================================================
# UI
# ==========================================================

from ui.styles import load_css
from ui.dashboard import CommandCenter

# ==========================================================
# Data
# ==========================================================

from data.market_data import MarketDataEngine

# ==========================================================
# Indicator Experts
# ==========================================================

from indicators import ema
from indicators import macd
from indicators import rsi

# ==========================================================
# Engines
# ==========================================================

from engine.trade_quality import TradeQualityEngine
from engine.dashboard import DashboardEngine

# ==========================================================
# Load Styles
# ==========================================================

load_css()

# ==========================================================
# Title
# ==========================================================

#st.title("Trade Decision Engine")

#st.caption("AI Powered Trading Decision Support System")

#st.divider()

# ==========================================================
# Download Market Data
# ==========================================================

with st.spinner("Downloading market data..."):

    market = MarketDataEngine()

    market_data = market.download_watchlist()

# ==========================================================
# Initialize Engines
# ==========================================================

trade_engine = TradeQualityEngine()

dashboard_engine = DashboardEngine()

# ==========================================================
# Build Dashboard Intelligence
# ==========================================================

dashboard = dashboard_engine.build(

    market_data,

    trade_engine,

    ema,

    macd,

    rsi

)

# ==========================================================
# Render Command Center
# ==========================================================

command_center = CommandCenter()

command_center.render(dashboard)
