"""
MACD Engine Test
"""

from data.market_data import MarketDataEngine
from indicators.macd import calculate

print()
print("=" * 60)
print("MACD ENGINE TEST")
print("=" * 60)

engine = MarketDataEngine()

market = engine.download_watchlist()

print()

for ticker, df in market.items():

    result = calculate(df)

    print("-" * 60)

    print(ticker)

    print()

    print("Values")

    print(f"MACD      : {result['values']['macd']}")
    print(f"Signal    : {result['values']['signal']}")
    print(f"Histogram : {result['values']['histogram']}")

    print()

    print("Analysis")

    print(f"Trend      : {result['analysis']['trend']}")
    print(f"Cross      : {result['analysis']['cross']}")
    print(f"Histogram  : {result['analysis']['histogram_direction']}")
    print(f"Momentum   : {result['analysis']['momentum']}")

print()
print("=" * 60)
print("MACD TEST PASSED")
print("=" * 60)
