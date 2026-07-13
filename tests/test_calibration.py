from research.calibration_manager import CalibrationManager

config = CalibrationManager()

print()

print("Trend :", config.trend_weight)
print("Momentum :", config.momentum_weight)
print("Risk :", config.risk_weight)
print("Pattern :", config.pattern_weight)
print("Volume :", config.volume_weight)

print()

print("Penalty :", config.penalty_conflicting)

print()

print("Minimum Trend :", config.qualification_trend)
print("Consensus :", config.qualification_consensus)
