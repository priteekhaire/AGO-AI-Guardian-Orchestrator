from risk_engine import calculate_risk

severities = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
    "UNKNOWN"
]

for severity in severities:
    print("=" * 40)
    print("Severity :", severity)
    print(calculate_risk(severity))
