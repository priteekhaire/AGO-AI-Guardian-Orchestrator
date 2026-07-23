# 🚀 AGO – AI Guardian Orchestrator

<div align="center">

### AI-Powered Serverless Security Orchestration & Incident Response Platform

Automating Vulnerability Analysis • Software Supply Chain Security • AI-Assisted Incident Response • Cloud Security

<br>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![AWS](https://img.shields.io/badge/AWS-Serverless-orange?style=for-the-badge&logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)
![GitHub](https://img.shields.io/badge/Open%20Source-Project-success?style=for-the-badge&logo=github)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)
![SBOM](https://img.shields.io/badge/SBOM-Syft-green?style=for-the-badge)
![SAST](https://img.shields.io/badge/SAST-Semgrep-purple?style=for-the-badge)
![SCA](https://img.shields.io/badge/SCA-Trivy-blueviolet?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Workflow](#-workflow)
- [Technology Stack](#-technology-stack)
- [AWS Services Used](#-aws-services-used)
- [Security Tools Used](#-security-tools-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

# 📌 Project Overview

**AGO (AI Guardian Orchestrator)** is an AI-powered **Serverless Security Orchestration and Incident Response Platform** designed to automate vulnerability analysis, software supply chain assessment, AI-assisted incident reporting, and security notifications in cloud-native environments.

Modern DevSecOps pipelines rely on multiple security tools to identify vulnerabilities and insecure coding practices. While these tools effectively generate findings, security analysts still spend considerable time manually reviewing reports, prioritizing risks, mapping attacker techniques, and preparing incident documentation.

AGO automates this workflow using an event-driven AWS architecture. It collects security scan reports, performs automated risk analysis, maps findings to the MITRE ATT&CK framework, generates AI-powered incident summaries, and sends real-time notifications to security teams.

The platform demonstrates how **Cloud Security**, **DevSecOps**, **Software Supply Chain Security**, and **Artificial Intelligence** can work together to improve security operations while reducing manual effort.

---

# ❗ Problem Statement

Organizations frequently use multiple security scanners during software development and deployment. Each tool focuses on a different aspect of security and produces its own report.

For example:

- Trivy detects vulnerabilities in container images and dependencies.
- Semgrep identifies insecure coding patterns.
- Syft generates a Software Bill of Materials (SBOM).

Although these tools are powerful, security analysts must still perform several manual tasks before remediation can begin.

Typical manual workflow:

- Read multiple JSON scan reports
- Review hundreds of vulnerabilities
- Identify critical findings
- Prioritize remediation
- Map vulnerabilities to attacker techniques
- Prepare incident reports
- Notify security teams

This process increases the **Mean Time To Respond (MTTR)**, introduces human error, and slows incident response.

---

# 💡 Solution

AGO automates the complete vulnerability analysis workflow using an event-driven serverless architecture.

Instead of manually reviewing multiple reports, the platform automatically:

- Collects security scan reports
- Parses Trivy, Semgrep, and SBOM outputs
- Performs software supply chain analysis
- Calculates vulnerability risk scores
- Maps findings to the MITRE ATT&CK framework
- Uses Google Gemini AI to generate incident summaries
- Creates structured incident reports
- Stores reports in Amazon S3
- Sends real-time notifications using Amazon SNS

This significantly reduces manual effort while providing consistent, repeatable, and scalable security operations.

---

# ✨ Key Features

## ☁️ Cloud-Native Architecture

- Event-driven AWS serverless architecture
- Fully containerized AWS Lambda deployment
- Automated orchestration using AWS Step Functions

---

## 🔐 Vulnerability Management

- Container vulnerability analysis
- Software Composition Analysis (SCA)
- Software Bill of Materials (SBOM)
- Static Application Security Testing (SAST)
- Risk scoring and prioritization

---

## 🤖 AI-Powered Incident Analysis

- AI-generated incident summaries
- Security recommendations
- Executive-level reporting
- Context-aware vulnerability explanations

---

## ⚔️ Threat Intelligence

- MITRE ATT&CK mapping
- Vulnerability categorization
- Severity analysis
- Security posture assessment

---

## ⚡ Automation

- Automated workflow execution
- Serverless event processing
- AI-assisted reporting
- Real-time email notifications
- Cloud-native orchestration

---

## 📊 Reporting

- JSON Incident Reports
- Executive Summary
- Risk Assessment
- AI Recommendations
- Security Findings
- MITRE ATT&CK Mapping

---
# 🏗️ Architecture

> **High-Level System Architecture**

<p align="center">
  <img src="architecture/architecture-diagram.png" width="95%">
</p>

AGO follows an **event-driven serverless architecture** where security scan reports are automatically processed without requiring manual intervention. The platform integrates multiple AWS services and security tools to analyze vulnerabilities, prioritize risks, generate AI-assisted incident reports, and notify security teams.

The architecture is designed around three core principles:

- **Automation** – Eliminate repetitive manual security tasks.
- **Scalability** – Process security findings using serverless AWS services.
- **Intelligence** – Enhance incident analysis using AI and MITRE ATT&CK mapping.

---

# 🔄 Workflow

The following workflow illustrates how AGO processes security scan reports from ingestion to incident notification.

```text
                 Security Scan Reports
          (Trivy | Syft | Semgrep)
                        │
                        ▼
                Amazon S3 Bucket
                        │
                        ▼
             Amazon EventBridge Rule
                        │
                        ▼
            AWS Step Functions Workflow
                        │
                        ▼
          AWS Lambda (Container Image)
                        │
     ┌──────────────────┼───────────────────┐
     │                  │                   │
     ▼                  ▼                   ▼
 Trivy Reader      Syft Reader      Semgrep Reader
     │                  │                   │
     └──────────────────┼───────────────────┘
                        │
                        ▼
                 Risk Engine Module
                        │
                        ▼
              MITRE ATT&CK Mapping
                        │
                        ▼
            Google Gemini AI Analysis
                        │
                        ▼
          Incident Report Generator
                        │
        ┌───────────────┴──────────────┐
        ▼                              ▼
 Amazon S3                     Amazon SNS
 Incident Report              Email Notification
```

---

# ⚙️ End-to-End Execution Flow

### Step 1 — Security Scanning

Security scanning tools analyze the application and generate JSON reports.

Generated reports include:

- Trivy Vulnerability Report
- Syft SBOM Report
- Semgrep SAST Report

These reports are uploaded to Amazon S3.

---

### Step 2 — Event Detection

Amazon EventBridge continuously monitors the S3 bucket.

Whenever a new scan report is uploaded:

- EventBridge detects the event.
- The configured rule is triggered.
- AWS Step Functions execution begins.

No manual execution is required.

---

### Step 3 — Workflow Orchestration

AWS Step Functions coordinate the complete workflow.

Instead of executing everything in a single script, Step Functions manage the execution sequence and ensure every stage completes successfully before proceeding to the next step.

This improves:

- Reliability
- Visibility
- Error handling
- Scalability

---

### Step 4 — Lambda Execution

AWS Lambda downloads the uploaded scan reports from Amazon S3.

The Lambda function executes several independent modules:

- Trivy Reader
- Syft Reader
- Semgrep Reader
- Risk Engine
- MITRE Mapper
- AI Analyzer
- Report Generator

Each module performs a specific responsibility.

---

### Step 5 — Vulnerability Analysis

The platform extracts:

- Vulnerabilities
- Package information
- Dependency metadata
- Severity
- Source code findings

Information from all scanners is combined into a single security assessment.

---

### Step 6 — Risk Assessment

The Risk Engine evaluates the collected findings.

Risk calculation considers:

- Severity
- Number of vulnerabilities
- Package importance
- Software supply chain exposure

The result is a consolidated security risk assessment.

---

### Step 7 — MITRE ATT&CK Mapping

Detected vulnerabilities are mapped to relevant MITRE ATT&CK techniques.

This helps security teams understand:

- How attackers could exploit weaknesses.
- Which attack techniques are relevant.
- Which defensive controls should be prioritized.

---

### Step 8 — AI Analysis

Google Gemini analyzes the complete security findings.

The AI generates:

- Executive Summary
- Technical Summary
- Business Impact
- Remediation Recommendations
- Overall Incident Description

The AI does not replace security scanners—it provides context and prioritization.

---

### Step 9 — Incident Report Generation

The Report Generator combines all collected information into a structured incident report.

The report includes:

- Executive Summary
- Vulnerability Details
- Risk Score
- MITRE ATT&CK Mapping
- AI Analysis
- Recommendations
- Timestamp

The report is stored in Amazon S3.

---

### Step 10 — Notification

After report generation:

Amazon SNS automatically sends an email notification containing the incident summary.

Security analysts receive immediate notification without manually checking dashboards.

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|-------------|----------|
| **AWS Lambda** | Executes the complete incident analysis workflow in a serverless environment. |
| **Amazon EventBridge** | Detects new scan reports uploaded to S3 and triggers the workflow automatically. |
| **AWS Step Functions** | Orchestrates and coordinates the entire processing pipeline. |
| **Amazon S3** | Stores scan reports and generated incident reports. |
| **Amazon SNS** | Sends email notifications after incident processing. |
| **Amazon ECR** | Stores the Docker container image used by AWS Lambda. |
| **Amazon CloudWatch** | Collects execution logs, debugging information, and monitoring metrics. |
| **AWS IAM** | Provides secure permission management between AWS services. |

---

# 🛡️ Security Tools Used

| Tool | Purpose |
|------|----------|
| **Trivy** | Detects vulnerabilities in container images, operating system packages, and software dependencies. |
| **Syft** | Generates a Software Bill of Materials (SBOM) for software supply chain visibility. |
| **Semgrep** | Performs Static Application Security Testing (SAST) by identifying insecure coding patterns. |
| **Google Gemini AI** | Generates AI-assisted incident summaries and remediation recommendations. |

---

# 🤖 AI Integration

AGO integrates **Google Gemini AI** to enhance security analysis.

Rather than manually interpreting large vulnerability reports, Gemini generates:

- Executive Summary
- Technical Explanation
- Security Recommendations
- Business Impact Assessment
- Prioritized Remediation Steps

The AI assists security analysts by transforming raw vulnerability data into actionable security insights while reducing manual analysis time.

---

# 💻 Technology Stack

## Cloud

- AWS Lambda
- Amazon S3
- Amazon EventBridge
- AWS Step Functions
- Amazon SNS
- Amazon ECR
- Amazon CloudWatch
- AWS IAM

---

## Security

- Trivy
- Syft
- Semgrep
- MITRE ATT&CK

---

## AI

- Google Gemini API

---

## Programming

- Python
- Docker
- JSON
- Boto3

---

## Development

- Git
- GitHub

---

# 📂 Project Structure

The project is organized into modular components, making it easy to understand, maintain, and extend.

```text
AGO-AI-Guardian-Orchestrator/
│
├── architecture/
│   ├── architecture-diagram.png
│   └── workflow-diagram.png
│
├── lambda_package/
│   ├── lambda_function.py
│   ├── ai_analyzer.py
│   ├── mitre_mapper.py
│   ├── report_generator.py
│   ├── risk_engine.py
│   ├── trivy_reader.py
│   ├── syft_reader.py
│   ├── semgrep_reader.py
│   └── requirements.txt
│
├── scanner/
│   ├── trivy-report.json
│   ├── sbom.json
│   └── semgrep-report.json
│
├── screenshots/
│   ├── step-functions/
│   ├── lambda/
│   ├── s3/
│   ├── eventbridge/
│   ├── cloudwatch/
│   ├── sns/
│   ├── ecr/
│   └── local/
│
├── README.md
└── LICENSE
```

---

# 🧩 Project Modules

Each module performs a dedicated task within the incident response pipeline.

| Module | Description |
|----------|-------------|
| **lambda_function.py** | Entry point for AWS Lambda. Coordinates the entire workflow. |
| **trivy_reader.py** | Parses Trivy vulnerability reports and extracts security findings. |
| **syft_reader.py** | Reads SBOM reports generated by Syft and extracts software component information. |
| **semgrep_reader.py** | Parses Semgrep SAST reports to identify insecure coding patterns. |
| **risk_engine.py** | Calculates the overall security risk score based on collected findings. |
| **mitre_mapper.py** | Maps vulnerabilities to MITRE ATT&CK techniques for better threat understanding. |
| **ai_analyzer.py** | Sends security findings to Google Gemini and generates AI-powered analysis. |
| **report_generator.py** | Generates the final structured incident report in JSON format. |

---

# ⚙️ Core Workflow

The following modules execute sequentially:

```text
Scan Reports
      │
      ▼
Lambda Function
      │
      ▼
Read Reports
      │
      ▼
Risk Calculation
      │
      ▼
MITRE Mapping
      │
      ▼
AI Analysis
      │
      ▼
Incident Report
      │
      ▼
Amazon S3
      │
      ▼
Amazon SNS
```

---

# 🚀 Getting Started

## Prerequisites

Before running the project, ensure the following are installed and configured.

### Software

- Python 3.11+
- Docker Desktop / Docker Engine
- Git
- AWS CLI
- AWS Account

### Python Packages

```bash
pip install -r requirements.txt
```

---

# 🔐 AWS Services Required

The following AWS services should be configured before deployment.

- Amazon S3
- AWS Lambda
- Amazon EventBridge
- AWS Step Functions
- Amazon SNS
- Amazon ECR
- Amazon CloudWatch
- AWS IAM

---

# 📦 Docker Deployment

Build the Lambda container image.

```bash
docker build -t ago-ai-lambda .
```

Tag the Docker image.

```bash
docker tag ago-ai-lambda:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/ago-ai-lambda:latest
```

Push the image to Amazon ECR.

```bash
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/ago-ai-lambda:latest
```

Deploy the container image to AWS Lambda.

---

# ▶️ Running the Workflow

The execution process follows these steps:

1. Generate security reports using Trivy, Syft, and Semgrep.
2. Upload the generated reports to Amazon S3.
3. EventBridge detects the upload event.
4. AWS Step Functions start execution.
5. Lambda downloads the reports.
6. Security findings are analyzed.
7. Risk score is calculated.
8. MITRE ATT&CK mapping is performed.
9. Google Gemini generates an incident summary.
10. Incident report is uploaded to Amazon S3.
11. Amazon SNS sends an email notification.

---

# 📤 Generated Outputs

AGO automatically produces the following outputs.

| Output | Description |
|----------|-------------|
| **SBOM Report** | Complete software component inventory generated using Syft. |
| **Trivy Report** | Container and dependency vulnerability analysis. |
| **Semgrep Report** | Static code analysis findings. |
| **Incident Report** | AI-generated security incident summary with recommendations. |
| **Email Notification** | Automated alert sent to security analysts through Amazon SNS. |

---

# 📈 Security Capabilities

AGO provides the following security capabilities:

✅ Software Bill of Materials (SBOM)

✅ Software Composition Analysis (SCA)

✅ Static Application Security Testing (SAST)

✅ Vulnerability Prioritization

✅ AI-assisted Incident Analysis

✅ MITRE ATT&CK Mapping

✅ Risk Scoring

✅ Automated Security Reporting

✅ Cloud-Native Serverless Processing

✅ Real-Time Security Notifications

---

# 📄 Sample Incident Report

The generated incident report contains:

- Executive Summary
- Risk Score
- Severity Distribution
- MITRE ATT&CK Techniques
- Vulnerability Details
- AI Analysis
- Recommended Actions
- Timestamp
- Security Summary

The report is stored in Amazon S3 and can be used by security teams for further investigation.

---
# 📸 Screenshots

## 🏗️ System Architecture

<p align="center">
<img src="architecture/architecture-diagram.png" width="95%">
</p>

---

## 🔄 AWS Step Functions

The Step Functions workflow orchestrates the complete incident response pipeline.

<p align="center">
<img src="screenshots/step-functions/workflow.png" width="90%">
</p>

<p align="center">
<img src="screenshots/step-functions/state-machine-definition.png" width="90%">
</p>

<p align="center">
<img src="screenshots/step-functions/execution-history.png" width="90%">
</p>

---

## ⚡ AWS Lambda

Lambda executes the complete incident analysis pipeline.

<p align="center">
<img src="screenshots/lambda/overview.png" width="90%">
</p>

---

## 📦 Amazon S3

Amazon S3 stores:

- Security Scan Reports
- SBOM Reports
- AI Generated Incident Reports

<p align="center">
<img src="screenshots/s3/bucket.png" width="90%">
</p>

<p align="center">
<img src="screenshots/s3/incident-report.png" width="90%">
</p>

---

## 📅 Amazon EventBridge

EventBridge automatically detects uploaded reports and starts the workflow.

<p align="center">
<img src="screenshots/eventbridge/rule.png" width="90%">
</p>

---

## 🐳 Amazon ECR

Amazon ECR stores the Docker image deployed to AWS Lambda.

<p align="center">
<img src="screenshots/ecr/repository.png" width="90%">
</p>

<p align="center">
<img src="screenshots/ecr/image-details.png" width="90%">
</p>

---

## 📊 Amazon CloudWatch

CloudWatch provides monitoring and execution logs for debugging and auditing.

<p align="center">
<img src="screenshots/cloudwatch/execution-logs.png" width="90%">
</p>

---

## 📧 Amazon SNS

Amazon SNS sends automated notifications after incident processing.

<p align="center">
<img src="screenshots/sns/topic.png" width="90%">
</p>

<p align="center">
<img src="screenshots/sns/email-notification.png" width="90%">
</p>

---

# 🎯 Key Learning Outcomes

Through this project I gained practical experience in:

- AWS Serverless Computing
- Cloud Security Architecture
- Event-Driven Application Design
- Docker Containerization
- Software Supply Chain Security
- Vulnerability Management
- Static Application Security Testing (SAST)
- Software Composition Analysis (SCA)
- Software Bill of Materials (SBOM)
- MITRE ATT&CK Framework
- AI-assisted Incident Analysis
- Incident Response Automation
- DevSecOps
- Security Orchestration
- Cloud-native Application Design

---

# 🚀 Future Enhancements

The project can be extended with several enterprise-grade capabilities.

### Security

- AWS GuardDuty Integration
- AWS Security Hub Integration
- Amazon Inspector Integration
- Multi-Cloud Security Support
- SIEM Integration
- Automated Remediation

### DevSecOps

- GitHub Actions CI/CD
- Jenkins Pipeline
- Kubernetes Support
- Helm Charts
- Terraform Deployment

### AI

- AI Chat Assistant
- Threat Hunting Recommendations
- AI-powered Root Cause Analysis
- Intelligent Risk Prediction

### Reporting

- Interactive Dashboard
- Real-time Analytics
- PDF Report Generation
- Executive Security Dashboard

---

# 📚 References

AWS Documentation

- https://docs.aws.amazon.com/

Trivy

- https://trivy.dev/

Syft

- https://github.com/anchore/syft

Semgrep

- https://semgrep.dev/

MITRE ATT&CK

- https://attack.mitre.org/

Google Gemini API

- https://ai.google.dev/

Docker

- https://www.docker.com/

---

# 👨‍💻 Author

## Pritee Khaire 

Cybersecurity Engineer | DevSecOps | Cloud Security | AWS | Docker | Security Automation


---

# 💡 Design Decisions

Several architectural decisions were made while developing AGO.

### Why AWS Lambda?

- No server management
- Automatic scaling
- Pay-per-use pricing
- Easy integration with AWS services

---

### Why Docker?

- Consistent execution environment
- Easy dependency management
- Simplified deployment
- Supports larger Lambda packages

---

### Why Amazon S3?

- Durable object storage
- Stores security reports
- Stores generated incident reports
- Easy integration with EventBridge

---

### Why EventBridge?

- Event-driven execution
- Eliminates manual triggering
- Native AWS integration

---

### Why Step Functions?

- Workflow orchestration
- Better error handling
- Execution visibility
- Modular workflow management

---

### Why Amazon SNS?

- Instant notifications
- Email integration
- Reliable message delivery

---

### Why Amazon ECR?

- Secure Docker image storage
- Native Lambda container support
- Version management

---

# 🔐 Security Considerations

The project follows several cloud security best practices.

- Principle of Least Privilege (IAM)
- Serverless architecture reduces attack surface
- Docker container isolation
- Centralized logging using CloudWatch
- Automated vulnerability analysis
- Secure storage using Amazon S3
- Event-driven execution
- AI-assisted prioritization
- Software Supply Chain visibility

---

# 🙌 Acknowledgements

This project was built using several excellent open-source tools and cloud services.

- Amazon Web Services (AWS)
- Google Gemini API
- Trivy
- Syft
- Semgrep
- MITRE ATT&CK Framework
- Docker
- Python Community







