from PIL import Image
import pandas as pd

claims = pd.read_csv("dataset/claims.csv")

paths = claims.iloc[0]["image_paths"].split(";")

for p in paths:
    img = Image.open("dataset/" + p)
    img.show()