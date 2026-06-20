import os
from dotenv import load_dotenv
import google.generativeai as genai
import pandas as pd

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

claims = pd.read_csv("dataset/claims.csv")

claim_text = claims.iloc[0]["user_claim"]

prompt = f"""
You are extracting insurance claims.

Return ONLY JSON.

Fields:
issue_type
object_part
claim_summary

Conversation:
{claim_text}
"""

response = model.generate_content(prompt)

print(response.text)