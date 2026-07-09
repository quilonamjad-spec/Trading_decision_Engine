import streamlit as st

from ui.cards import stock_card
from ui.styles import load_css

from utils.watchlist import load_watchlist
from data.fetch_data import fetch_stock_data


st.set_page_config(
    page_title="Trade Decision Engine",
    page_icon="📈",
    layout="wide"
)

load_css()

st.title("📈 Trade Decision Engine")

st.caption("Professional Multi Stock Scanner")

st.divider()

watchlist = load_watchlist()

stocks=[]

for i,ticker in enumerate(watchlist):

    live = fetch_stock_data(ticker)

    stock = {

        "rank":i+1,

        "ticker":live["ticker"],

        "company":live["company"],

        "price":live["price"],

        "change":f'{live["change"]:+.2f}',

        # Dummy Values (Next Version)

        "recommendation":"WAIT",

        "score":50,

        "trend":"Neutral",

        "momentum":"Neutral",

        "volume":"Average",

        "ema":"Neutral",

        "macd":"Neutral"

    }

    stocks.append(stock)

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric("Stocks",len(stocks))

with col2:

    st.metric("Data Source","Yahoo")

with col3:

    st.metric("Status","LIVE")

with col4:

    st.metric("Version","0.4")

st.divider()

cols=st.columns(3)

for i,stock in enumerate(stocks):

    with cols[i%3]:

        stock_card(stock)