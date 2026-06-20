import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_claim(claim_text):

    prompt = f"""
    Extract insurance claim information.

    Return ONLY valid JSON.

    {{
        "issue_type":"",
        "object_part":"",
        "claim_summary":""
    }}

    Claim:
    {claim_text}
    """

    response = model.generate_content(prompt)

    text = response.text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)