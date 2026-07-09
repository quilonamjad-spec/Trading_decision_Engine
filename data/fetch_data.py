# ---------------------------------------------
# Trade Decision Engine
# Version : 0.4
# data/fetch_data.py
# ---------------------------------------------

import yfinance as yf


def fetch_stock_data(ticker):

    stock = yf.Ticker(ticker)

    info = stock.fast_info

    price = info.get("lastPrice", 0)

    previous = info.get("previousClose", 0)

    change = round(price - previous, 2)

    return {

        "ticker": ticker.replace(".NS",""),

        "company": ticker,

        "price": price,

        "change": change

    }