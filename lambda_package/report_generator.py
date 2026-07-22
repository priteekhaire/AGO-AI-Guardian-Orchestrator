from datetime import datetime, UTC


def generate_report(
    incident,
    risk,
    mitre,
    ai_analysis,
    trivy_results=None,
    sbom_results=None,
    semgrep_results=None
):
    """
    Generate a comprehensive AI-powered security incident report.
    """

    if trivy_results is None:
        trivy_results = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "unknown": 0,
            "total": 0
        }

    if sbom_results is None:
        sbom_results = {
            "generated": False,
            "format": "CycloneDX",
            "packages": 0,
            "image": "Unknown"
        }

    if semgrep_results is None:
        semgrep_results = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
            "total": 0
        }

    report = {

        "report_generated_at": datetime.now(UTC).isoformat(),

        "platform": "AGO - AI Guardian Orchestrator",

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

        "security_scans": {

            "trivy": {

                "critical": trivy_results.get("critical", 0),
                "high": trivy_results.get("high", 0),
                "medium": trivy_results.get("medium", 0),
                "low": trivy_results.get("low", 0),
                "unknown": trivy_results.get("unknown", 0),
                "total": trivy_results.get("total", 0)
            },

            "sbom": {

                "generated": sbom_results.get("generated", False),
                "format": sbom_results.get("format", "CycloneDX"),
                "packages": sbom_results.get("packages", 0),
                "image": sbom_results.get("image", "Unknown")
            },

            "semgrep": {

                "critical": semgrep_results.get("critical", 0),
                "high": semgrep_results.get("high", 0),
                "medium": semgrep_results.get("medium", 0),
                "low": semgrep_results.get("low", 0),
                "info": semgrep_results.get("info", 0),
                "total": semgrep_results.get("total", 0)
            }

        },

        "ai_analysis": ai_analysis
    }

    return report
