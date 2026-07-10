from data.market_data import MarketDataEngine
from indicators.macd import calculate

print()
print("=" * 70)
print("MACD ENGINE V2 TEST")
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

    print(f"MACD        : {result['values']['macd']}")
    print(f"Signal      : {result['values']['signal']}")
    print(f"Histogram   : {result['values']['histogram']}")

    print("\nANALYSIS")

    print(f"Momentum Bias : {result['analysis']['momentum_bias']}")
    print(f"Momentum      : {result['analysis']['histogram_state']}")
    print(f"Strength      : {result['analysis']['strength']}")

print()
print("=" * 70)
print("MACD V2 TEST PASSED")
print("=" * 70)
