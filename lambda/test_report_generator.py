from risk_engine import calculate_risk
from mitre_mapper import map_attack
from ai_analyzer import analyze_incident
from report_generator import generate_report

incident = {
    "incident_id": "AGO-0001",
    "severity": "HIGH",
    "attack": "SQL Injection",
    "affected_resource": "AGO-Demo-Server",
    "status": "OPEN"
}

risk = calculate_risk(
    incident["severity"]
)

mitre = map_attack(
    incident["attack"]
)

ai = analyze_incident(
    incident
)

report = generate_report(
    incident,
    risk,
    mitre,
    ai
)

print(report)
