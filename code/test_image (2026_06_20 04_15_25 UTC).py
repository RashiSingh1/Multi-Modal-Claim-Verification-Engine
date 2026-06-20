import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import pandas as pd

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

claims = pd.read_csv("dataset/claims.csv")

path = claims.iloc[0]["image_paths"].split(";")[0]

img = Image.open("dataset/" + path)

prompt = """
You are an insurance damage assessor.

Carefully inspect this image.

Answer:

- What object is shown?
- Is any damage visible?
- If yes, what type of damage?
- Which part is affected?
- Confidence: High/Medium/Low

If no damage is visible, explicitly say:
'No visible damage detected'.
"""

response = model.generate_content(
    [prompt, img]
)

print(response.text)