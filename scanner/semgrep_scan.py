import subprocess

SOURCE_DIR = "../"
OUTPUT_FILE = "semgrep-report.json"

command = [
    "semgrep",
    "--config=auto",
    "--json",
    "--output",
    OUTPUT_FILE,
    SOURCE_DIR
]

print("Running Semgrep Scan...")

subprocess.run(command, check=True)

print(f"Semgrep report saved to {OUTPUT_FILE}")
