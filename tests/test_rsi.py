from data.market_data import MarketDataEngine
from indicators.rsi import calculate

print()
print("=" * 70)
print("RSI ENGINE V1 TEST")
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

    print(f"RSI : {result['values']['rsi']}")

    print("\nANALYSIS")

    print(f"Zone : {result['analysis']['zone']}")
    print(f"Risk : {result['analysis']['risk']}")

print()
print("=" * 70)
print("RSI TEST PASSED")
print("=" * 70)
