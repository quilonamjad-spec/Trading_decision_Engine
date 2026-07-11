import streamlit as st

from ui.styles import load_css
from ui.components.stock_card_v2 import StockCard

from indicators import ema
from indicators import macd
from indicators import rsi

from engine.trade_quality import TradeQualityEngine

from data.market_data import MarketDataEngine

st.set_page_config(
    page_title="TDE Prototype",
    layout="wide",
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
# Trade Quality Engine
# ------------------------------------

trade_engine = TradeQualityEngine()

card = StockCard()

# ------------------------------------
# Display Cards
# ------------------------------------

for ticker, df in market_data.items():

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    price = float(latest["Close"])

    change = price - float(previous["Close"])

    pct_change = (change / float(previous["Close"])) * 100

    # -------------------------------
    # Expert Engines
    # -------------------------------

    ema_result = ema.calculate(df)

    macd_result = macd.calculate(df)

    rsi_result = rsi.calculate(df)

    # -------------------------------
    # Trade Quality
    # -------------------------------

    trade = trade_engine.evaluate(

        ema_result,

        macd_result,

        rsi_result

    )

    # -------------------------------
    # Render Card
    # -------------------------------
    left, center, right = st.columns([1, 4, 1])
    
    with center:
        card.render(
    
            ticker=ticker.replace(".NS", ""),
    
            company=ticker,
    
            price=price,
    
            change=change,
    
            pct_change=pct_change,
    
            trade=trade,
    
            df=df
    
        )
    
        st.markdown("<br>", unsafe_allow_html=True)
