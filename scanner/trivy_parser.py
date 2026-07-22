import json


def parse_trivy_report(report_path="trivy-report.json"):

    with open(report_path, "r") as f:
        report = json.load(f)

    summary = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "unknown": 0,
        "packages_scanned": 0,
        "total_vulnerabilities": 0
    }

    for result in report.get("Results", []):

        summary["packages_scanned"] += 1

        vulnerabilities = result.get("Vulnerabilities", [])

        summary["total_vulnerabilities"] += len(vulnerabilities)

        for vuln in vulnerabilities:

            severity = vuln.get("Severity", "").lower()

            if severity in summary:
                summary[severity] += 1

    return summary


if __name__ == "__main__":

    data = parse_trivy_report()

    print("\n========== Trivy Summary ==========")

    for key, value in data.items():
        print(f"{key:25}: {value}")
