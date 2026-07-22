import json
import os
import boto3

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]

# Change this if your report is stored elsewhere
TRIVY_REPORT_KEY = "security-scans/trivy-report.json"


def load_trivy_results():

    summary = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "unknown": 0,
        "total": 0
    }

    local_file = "/tmp/trivy-report.json"

    try:

        # Download latest report from S3
        s3.download_file(
            BUCKET_NAME,
            TRIVY_REPORT_KEY,
            local_file
        )

        with open(local_file, "r") as f:
            report = json.load(f)

        for result in report.get("Results", []):

            for vuln in result.get("Vulnerabilities", []):

                severity = vuln.get("Severity", "").lower()

                if severity in summary:
                    summary[severity] += 1
                else:
                    summary["unknown"] += 1

                summary["total"] += 1

    except Exception as e:

        print(f"Trivy Reader Error: {e}")

    return summary
