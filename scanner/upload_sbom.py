import os
import boto3

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]
FILE_NAME = "sbom.json"

s3.upload_file(
    FILE_NAME,
    BUCKET_NAME,
    f"security-scans/{FILE_NAME}"
)

print(f"Uploaded {FILE_NAME} to s3://{BUCKET_NAME}/security-scans/")
