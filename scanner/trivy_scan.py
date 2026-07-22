import subprocess

IMAGE_NAME = "ago-ai-lambda:latest"

def run_trivy():
    command = [
        "sudo",
        "trivy",
        "image",
        "--format",
        "json",
        "-o",
        "trivy-report.json",
        IMAGE_NAME,
    ]

    subprocess.run(command, check=True)
    print("✅ Trivy scan completed successfully.")

if __name__ == "__main__":
    run_trivy()
