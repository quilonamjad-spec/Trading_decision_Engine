import streamlit as st

from data.market_data import MarketDataEngine

from engine.dashboard import DashboardEngine

from engine.trade_quality import TradeQualityEngine

from indicators import ema
from indicators import macd
from indicators import rsi

market_engine = MarketDataEngine()

dashboard_engine = DashboardEngine()

trade_engine = TradeQualityEngine()



# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Market Scanner",
    page_icon="📈",
    layout="wide"
)


# ==========================================================
# Header
# ==========================================================

def draw_header():

    st.title("📈 Market Scanner")
    st.caption("Find today's highest quality trading opportunities.")


# ==========================================================
# Controls
# ==========================================================

def draw_controls():

    col1, col2 = st.columns([3, 1])

    with col1:

        universe = st.selectbox(
            "Select Universe",
            [
                "Nifty 50",
                "Nifty 100",
                "Nifty 500"
            ],
            index=2
        )

    with col2:

        st.write("")
        st.write("")

        scan = st.button(
            "🚀 Scan Market",
            use_container_width=True
        )

    return universe, scan


# ==========================================================
# Results Placeholder
# ==========================================================

def draw_placeholder():

    st.divider()

    st.info(
        "Press 'Scan Market' to analyse today's opportunities."
    )


# ==========================================================
# Main
# ==========================================================

def main():

    draw_header()

    universe, scan = draw_controls()

    if scan:

        with st.spinner("Scanning market..."):

            # -----------------------------------------
            # Download Market Data
            # -----------------------------------------

            market_data = market_engine.download_watchlist()

            # -----------------------------------------
            # Analyse Market
            # -----------------------------------------

            dashboard = dashboard_engine.build(

                market_data=market_data,

                trade_engine=trade_engine,

                ema=ema,

                macd=macd,

                rsi=rsi

            )

        st.success("Market Analysis Complete ✅")

        draw_market_summary(
            universe,
            dashboard
        )

    else:

        draw_placeholder()

    # ==========================================================
    # Market Summary
    # ==========================================================
    
    def draw_market_summary(universe, dashboard):
    
        st.divider()
    
        st.subheader("📊 Market Summary")
    
        col1, col2, col3, col4 = st.columns(4)
    
        with col1:
    
            st.metric(
                "Market Bias",
                dashboard["market_bias"]
            )
    
        with col2:
    
            st.metric(
                "Market Score",
                f"{dashboard['market_score']}/100"
            )
    
        with col3:
    
            st.metric(
                "Stocks Analysed",
                len(dashboard["stocks"])
            )
    
        with col4:
    
            best = dashboard["best_trade"]
    
            if best:
    
                st.metric(
                    "Best Trade",
                    best["ticker"].replace(".NS", "")
                )
    
        st.caption(f"Universe : {universe}")

    # ==========================================================
    # Application Entry Point
    # ==========================================================
    
main()
