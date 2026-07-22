import json
import os
import boto3

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]
SEMGREP_KEY = "security-scans/semgrep-report.json"


def load_semgrep_results():

    summary = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "info": 0,
        "total": 0
    }

    try:

        local_file = "/tmp/semgrep-report.json"

        s3.download_file(
            BUCKET_NAME,
            SEMGREP_KEY,
            local_file
        )

        with open(local_file, "r") as f:
            report = json.load(f)

        for finding in report.get("results", []):

            severity = (
                finding.get("extra", {})
                .get("severity", "INFO")
                .lower()
            )

            if severity in summary:
                summary[severity] += 1
            else:
                summary["info"] += 1

            summary["total"] += 1

    except Exception as e:
        print(f"Semgrep Reader Error: {e}")

    return summary
