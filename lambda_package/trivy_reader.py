import json
import os
import boto3

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]
TRIVY_REPORT_KEY = "security-scans/trivy-report.json"


def load_trivy_results():
    """
    Download the latest Trivy report from S3 and summarize vulnerabilities.
    """

    summary = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "unknown": 0,
        "total": 0
    }

    try:
        local_path = "/tmp/trivy-report.json"

        s3.download_file(
            BUCKET_NAME,
            TRIVY_REPORT_KEY,
            local_path
        )

        with open(local_path, "r") as file:
            report = json.load(file)

        for result in report.get("Results", []):

            for vuln in result.get("Vulnerabilities", []):

                severity = vuln.get("Severity", "").lower()

                if severity in summary:
                    summary[severity] += 1
                else:
                    summary["unknown"] += 1

                summary["total"] += 1

        print("Trivy Summary:", summary)

    except Exception as e:
        print(f"[ERROR] Trivy Reader: {e}")

    return summary
