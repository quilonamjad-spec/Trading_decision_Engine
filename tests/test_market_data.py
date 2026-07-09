from data.market_data import MarketDataEngine

engine = MarketDataEngine()

market = engine.download_watchlist()

print()

print("=" * 60)

print("DOWNLOAD SUMMARY")

print("=" * 60)

for ticker, df in market.items():

    print(f"{ticker}")

    print(df.tail())

    print()
