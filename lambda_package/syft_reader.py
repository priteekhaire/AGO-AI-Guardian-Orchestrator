import json
import os
import boto3

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]
SBOM_KEY = "security-scans/sbom.json"


def load_sbom_results():

    summary = {
        "generated": False,
        "format": "CycloneDX",
        "packages": 0
    }

    try:

        local_file = "/tmp/sbom.json"

        s3.download_file(
            BUCKET_NAME,
            SBOM_KEY,
            local_file
        )

        with open(local_file, "r") as f:
            sbom = json.load(f)

        summary["generated"] = True

        components = sbom.get("components", [])
        summary["packages"] = len(components)

        metadata = sbom.get("metadata", {})

        if metadata.get("component"):
            summary["image"] = metadata["component"].get("name", "Unknown")

    except Exception as e:
        print(f"SBOM Reader Error: {e}")

    return summary
