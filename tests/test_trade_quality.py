from engine.trade_quality import TradeQualityEngine


engine = TradeQualityEngine()

result = engine.calculate(

    trend_score=32,

    momentum_score=28,

    risk_score=24,

    direction="LONG"

)

print(result)
