import os
import json
import time
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env first
load_dotenv()

# Check API key
api_key = os.getenv("GEMINI_API_KEY")

print("API Key Found:", api_key is not None)

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_image(image_path):

    img = Image.open(image_path)

    prompt = """
    Analyze insurance damage image.

    Return ONLY valid JSON.

    {
        "object_type":"",
        "object_part":"",
        "damage_type":"",
        "severity":"",
        "damage_visible":true
    }
    """

    for attempt in range(3):

        try:

            response = model.generate_content(
                [prompt, img]
            )

            text = response.text.strip()

            text = text.replace(
                "```json",
                ""
            )

            text = text.replace(
                "```",
                ""
            )

            return json.loads(text)

        except Exception as e:

            print(
                f"Gemini Error (Attempt {attempt+1}):",
                e
            )

            if "429" in str(e):

                print(
                    "Quota exceeded. Waiting..."
                )

                time.sleep(10)

            else:
                break

    return {
        "object_type": "unknown",
        "object_part": "unknown",
        "damage_type": "unknown",
        "severity": "unknown",
        "damage_visible": False
    }