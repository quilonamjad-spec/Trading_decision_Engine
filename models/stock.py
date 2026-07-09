from dataclasses import dataclass

@dataclass
class Stock:
    rank: int
    ticker: str
    company: str
    price: float
    recommendation: str
    score: int
    trend: str
    momentum: str
    volume: str