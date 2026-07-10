"""
EMA Engine Test
"""

from data.market_data import MarketDataEngine

from indicators.ema import calculate

print()

print("="*60)

print("EMA ENGINE TEST")

print("="*60)

engine = MarketDataEngine()

market = engine.download_watchlist()

print()

for ticker, df in market.items():

    result = calculate(df)

    print("-"*60)

    print(f"{ticker}")

    print(f"EMA5   : {result['ema5']}")

    print(f"EMA9   : {result['ema9']}")

    print(f"EMA20  : {result['ema20']}")

    print(f"EMA50  : {result['ema50']}")

    print(f"Alignment : {result['alignment']}")

print()

print("="*60)

print("EMA TEST PASSED")

print("="*60)
