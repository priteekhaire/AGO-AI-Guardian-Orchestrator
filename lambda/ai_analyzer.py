import json
import os

from dotenv import load_dotenv
from google import genai

# Load .env for local development
load_dotenv()


def analyze_incident(incident):
    """
    Analyze a security incident using Google Gemini and
    return structured JSON.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a Senior SOC Analyst.

Analyze the following incident.

Incident:
{json.dumps(incident, indent=2)}

Return ONLY valid JSON.

Use exactly this format.

{{
    "executive_summary": "",
    "technical_analysis": "",
    "business_impact": "",
    "recommended_actions": [
        "",
        "",
        ""
    ]
}}

Do not include markdown.

Do not include explanation.

Return JSON only.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown fences if Gemini adds them
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        return json.loads(text)

    except Exception:
        return {
            "executive_summary": "Unable to parse AI response.",
            "technical_analysis": text,
            "business_impact": "Unknown",
            "recommended_actions": [
                "Review logs manually."
            ]
        }
