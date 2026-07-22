# Risk Scoring Engine

RISK_MATRIX = {
    "LOW": {
        "score": 25,
        "level": "Low Risk",
        "priority": "P4"
    },
    "MEDIUM": {
        "score": 55,
        "level": "Medium Risk",
        "priority": "P3"
    },
    "HIGH": {
        "score": 85,
        "level": "High Risk",
        "priority": "P2"
    },
    "CRITICAL": {
        "score": 100,
        "level": "Critical Risk",
        "priority": "P1"
    }
}


def calculate_risk(severity):
    """
    Returns risk score, level and priority
    """

    severity = severity.upper()

    return RISK_MATRIX.get(
        severity,
        {
            "score": 0,
            "level": "Unknown",
            "priority": "Unknown"
        }
    )
