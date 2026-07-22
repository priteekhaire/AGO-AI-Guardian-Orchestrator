import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "models/gemini-3.5-flash"


def analyze_incident(incident):

    prompt = f"""
You are a Senior SOC Analyst.

Analyze this incident:

{incident}

Provide:

1. Executive Summary
2. Technical Analysis
3. Business Impact
4. MITRE ATT&CK Context
5. Recommended Actions
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text
