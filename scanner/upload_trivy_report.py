import os
import boto3

BUCKET_NAME = os.environ["BUCKET_NAME"]
FILE_NAME = "trivy-report.json"

s3 = boto3.client("s3")

s3.upload_file(
    FILE_NAME,
    BUCKET_NAME,
    f"security-scans/{FILE_NAME}"
)

print(f"✅ Trivy report uploaded to s3://{BUCKET_NAME}/security-scans/{FILE_NAME}")
