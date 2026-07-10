from data.market_data import MarketDataEngine
from indicators.ema import calculate

print()
print("=" * 70)
print("EMA ENGINE V2 TEST")
print("=" * 70)

engine = MarketDataEngine()

market = engine.download_watchlist()

for ticker, df in market.items():

    result = calculate(df)

    print()
    print("-" * 70)
    print(ticker)
    print("-" * 70)

    print("\nVALUES")

    print(f"Price   : {result['values']['price']}")
    print(f"EMA5    : {result['values']['ema5']}")
    print(f"EMA9    : {result['values']['ema9']}")
    print(f"EMA20   : {result['values']['ema20']}")
    print(f"EMA50   : {result['values']['ema50']}")

    print("\nANALYSIS")

    print(f"Alignment        : {result['analysis']['alignment']}")
    print(f"Price Position   : {result['analysis']['price_vs_ema20']}")
    print(f"Long Trend       : {result['analysis']['price_vs_ema50']}")
    print(f"Distance EMA20   : {result['analysis']['distance_ema20_pct']} %")
    print(f"Distance EMA50   : {result['analysis']['distance_ema50_pct']} %")

print()
print("=" * 70)
print("EMA V2 TEST PASSED")
print("=" * 70)
