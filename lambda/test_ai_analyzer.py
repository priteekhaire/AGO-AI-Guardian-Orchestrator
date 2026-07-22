import json

from ai_analyzer import analyze_incident

incident = {
    "incident_id": "AGO-0001",
    "severity": "HIGH",
    "attack": "SQL Injection",
    "risk_score": 85,
    "risk_level": "High Risk",
    "priority": "P2",
    "mitre_id": "T1190",
    "technique": "Exploit Public-Facing Application",
    "affected_resource": "AGO-Demo-Server",
    "status": "OPEN"
}

analysis = analyze_incident(incident)

print(json.dumps(analysis, indent=4))
