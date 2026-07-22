import json
import uuid
import os
import boto3

from risk_engine import calculate_risk
from mitre_mapper import map_attack
from ai_analyzer import analyze_incident
from report_generator import generate_report

from trivy_reader import load_trivy_results
from syft_reader import load_sbom_results
from semgrep_reader import load_semgrep_results

# AWS Clients
s3 = boto3.client("s3")
sns = boto3.client("sns")

# Environment Variables
BUCKET_NAME = os.environ["BUCKET_NAME"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]


def lambda_handler(event, context):
    """
    AI Guardian Orchestrator
    Main Lambda Handler
    """

    # ------------------------------------
    # Parse EventBridge Event
    # ------------------------------------
    detail = event.get("detail", event)

    attack = detail.get("attack", "Unknown")
    severity = detail.get("severity", "LOW")

    incident = {
        "attack": attack,
        "severity": severity,
        "source_ip": detail.get("source_ip", "Unknown"),
        "target": detail.get("target", "Unknown"),
        "timestamp": detail.get("timestamp", "Unknown"),
        "payload": detail.get("payload", "")
    }

    print("[INFO] Security Incident Received")

    # ------------------------------------
    # Risk Assessment
    # ------------------------------------
    risk = calculate_risk(severity)

    # ------------------------------------
    # MITRE ATT&CK Mapping
    # ------------------------------------
    mitre = map_attack(attack)

    # ------------------------------------
    # AI Analysis (Gemini)
    # ------------------------------------
    ai_analysis = analyze_incident(incident)

    # ------------------------------------
    # Trivy Scan Summary
    # ------------------------------------
    trivy_results = load_trivy_results()

    # ------------------------------------
    # SBOM Summary
    # ------------------------------------
    sbom_results = load_sbom_results()

    # ------------------------------------
    # Semgrep Summary
    # ------------------------------------
    semgrep_results = load_semgrep_results()

    # ------------------------------------
    # Generate Final Report
    # ------------------------------------
    report = generate_report(
        incident=incident,
        risk=risk,
        mitre=mitre,
        ai_analysis=ai_analysis,
        trivy_results=trivy_results,
        sbom_results=sbom_results,
        semgrep_results=semgrep_results
    )

    report_json = json.dumps(report, indent=4)

    filename = f"incident-{uuid.uuid4()}.json"

    # ------------------------------------
    # Upload Report to S3
    # ------------------------------------
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=report_json,
        ContentType="application/json"
    )

    print(f"[INFO] Report uploaded to S3: {filename}")

    # ------------------------------------
    # SNS Notification
    # ------------------------------------
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="AI Guardian Orchestrator - Security Incident",
        Message=report_json
    )

    print("[INFO] SNS Notification Sent")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Incident processed successfully",
            "report": filename
        })
    }
