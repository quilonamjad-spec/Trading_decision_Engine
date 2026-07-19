import streamlit as st

from data.market_data import MarketDataEngine

from engine.dashboard import DashboardEngine

from engine.trade_quality import TradeQualityEngine

from ui.decision_summary import draw_decision_summary

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
if "selected_stock" not in st.session_state:
    st.session_state.selected_stock = None
if "dashboard" not in st.session_state:
    st.session_state.dashboard = None

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
           
    if st.session_state.dashboard:

        st.success("Market Analysis Complete ✅")
    
        draw_market_summary(
            universe,
            st.session_state.dashboard
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

    st.divider()

    draw_top_opportunities(
        dashboard["primary_watchlist"]
    )

    st.divider()

    draw_watchlist(
        dashboard["secondary_watchlist"]
    )
    

def draw_opportunity_card(stock):

    with st.container(border=True):

        col1, col2 = st.columns([4, 1])

        with col1:
            st.subheader(stock["ticker"])

            st.write(f"**{stock['direction']}** • {stock['status']}")

            st.caption(
                f"Grade: {stock['grade']} | Confidence: {stock['confidence']}"
            )

        with col2:
            st.metric(
                "Score",
                f"{stock['score']}/100"
            )

        if st.button(
            "📊 View Analysis",
            key=f"analysis_{stock['ticker']}"
        ):
            st.session_state.selected_stock = stock
            st.rerun()
        

def draw_top_opportunities(primary_watchlist):

    st.subheader("🏆 Today's Opportunities")

    for stock in primary_watchlist:
        draw_opportunity_card(stock)

         if (
            st.session_state.selected_stock
            and
            st.session_state.selected_stock["ticker"] == stock["ticker"]
         ):
            draw_decision_summary(
                st.session_state.selected_stock
            )
            
def draw_watchlist(secondary_watchlist):

    st.subheader("👀 Keep an Eye On")

    for stock in secondary_watchlist:
        st.write(f"• {stock['ticker']}")

    # ==========================================================
    # Application Entry Point
    # ==========================================================
    
main()
