"""
===========================================================
Trade Decision Engine
Core Analysis Engine
===========================================================
"""

from data.market_data import MarketDataEngine

from engine import ema
from engine import macd
from engine import rsi
from engine.trade_quality import TradeQualityEngine


# --------------------------------------------------------
# Initialize Engines (created once)
# --------------------------------------------------------

market = MarketDataEngine()
trade_engine = TradeQualityEngine()


# --------------------------------------------------------
# Analyze One Stock
# --------------------------------------------------------

def analyze_stock(ticker: str, mode: str = "Intraday"):

    ticker = ticker.strip().upper()

    if ticker == "":
        raise ValueError("Ticker cannot be empty")

    if not ticker.endswith(".NS"):
        ticker += ".NS"

    # ------------------------------------
    # Download Market Data
    # ------------------------------------

    df = market.get_data(ticker)

    if df is None or df.empty:
        raise Exception(f"No market data found for {ticker}")

    # ------------------------------------
    # Run Indicators
    # ------------------------------------

    ema_result = ema.calculate(df)

    macd_result = macd.calculate(df)

    rsi_result = rsi.calculate(df)

    # ------------------------------------
    # Trade Quality
    # ------------------------------------

    trade = trade_engine.evaluate(
        ema_result,
        macd_result,
        rsi_result
    )

    # ------------------------------------
    # Additional Information
    # ------------------------------------

    trade["ticker"] = ticker
    trade["mode"] = mode

    trade["price"] = round(
        float(df["Close"].iloc[-1]),
        2
    )

    trade["last_candle"] = str(df.index[-1])

    trade["candles"] = len(df)

    return trade


# --------------------------------------------------------
# Analyze Multiple Stocks
# --------------------------------------------------------

def analyze_multiple(stocks):

    """
    stocks =
    [
        {"ticker":"SBIN","mode":"Intraday"},
        {"ticker":"BEL","mode":"Swing"}
    ]
    """

    results = []

    for stock in stocks:

        ticker = stock.get("ticker", "").strip()

        if ticker == "":
            continue

        mode = stock.get("mode", "Intraday")

        try:

            results.append(
                analyze_stock(
                    ticker=ticker,
                    mode=mode
                )
            )

        except Exception as e:

            results.append({
                "ticker": ticker,
                "error": str(e)
            })

    evolution = build_evolution(df, trade_engine)

    return {
        "decision": result,
        "evolution": evolution
    }
#-------
from datetime import datetime


def build_evolution(df, trade_engine):
    """
    Build Trade Health evolution throughout the day.

    Evaluates the engine every 3 candles (15 minutes on a 5-minute chart)
    and records only Trade Health for now.
    """

    evolution = []

    MIN_CANDLES = 30      # Wait until indicators are stable
    STEP = 3              # Every 15 minutes

    for i in range(MIN_CANDLES, len(df) + 1, STEP):

        partial_df = df.iloc[:i]

        # Existing indicator calculations
        ema_result = trade_engine.ema.calculate(partial_df)
        macd_result = trade_engine.macd.calculate(partial_df)
        rsi_result = trade_engine.rsi.calculate(partial_df)

        # Existing trade quality calculation
        result = trade_engine.evaluate(
            ema_result,
            macd_result,
            rsi_result
        )

        evolution.append({
            "time": partial_df.index[-1].strftime("%H:%M"),
            "health": result["trade_health"]
        })

    return evolution
    trade = analyze_stock("SBIN.NS")
    
    print("\nEngine Evolution\n")
    
    for row in trade["evolution"]:
        print(row)
