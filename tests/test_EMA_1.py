from indicators import ema

result = ema.calculate(df)

print(result["decision"])
