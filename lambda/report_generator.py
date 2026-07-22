from datetime import datetime, UTC


def generate_report(
    incident,
    risk,
    mitre,
    ai_analysis
):
    """
    Generate a structured incident report.
    """

    report = {
        "report_generated_at": datetime.now(UTC).isoformat(),

        "incident": incident,

        "risk_assessment": {
            "risk_score": risk["score"],
            "risk_level": risk["level"],
            "priority": risk["priority"]
        },

        "mitre_attack": {
            "mitre_id": mitre["mitre_id"],
            "technique": mitre["technique"],
            "tactic": mitre["tactic"]
        },

        "ai_analysis": ai_analysis
    }

    return report
