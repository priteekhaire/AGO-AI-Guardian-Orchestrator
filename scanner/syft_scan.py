import subprocess

IMAGE_NAME = "ago-ai-lambda:latest"
OUTPUT_FILE = "sbom.json"


def generate_sbom():
    print(f"Generating SBOM for {IMAGE_NAME}...")

    command = [
        "syft",
        IMAGE_NAME,
        "-o",
        "cyclonedx-json",
    ]

    with open(OUTPUT_FILE, "w") as outfile:
        subprocess.run(command, stdout=outfile, check=True)

    print(f"SBOM saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_sbom()
