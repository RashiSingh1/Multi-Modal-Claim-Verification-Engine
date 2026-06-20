import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import pandas as pd

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

claims = pd.read_csv("dataset/claims.csv")

paths = claims.iloc[0]["image_paths"].split(";")

for path in paths:

    print("\n------------------")
    print("Analyzing:", path)

    img = Image.open("dataset/" + path)

    response = model.generate_content([
        """
        You are an insurance damage assessor.

        Identify:
        - object type
        - damaged part
        - damage type
        - severity

        If no damage is visible, say:
        No visible damage detected.
        """,
        img
    ])

    print(response.text)