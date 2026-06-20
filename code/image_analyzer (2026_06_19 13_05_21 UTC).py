import os
import json
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_image(image_path):

    img = Image.open(image_path)

    prompt = """
    Analyze insurance damage image.

    Return ONLY JSON.

    {
        "object_type":"",
        "object_part":"",
        "damage_type":"",
        "severity":"",
        "damage_visible":true
    }
    """

    response = model.generate_content(
        [prompt, img]
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)