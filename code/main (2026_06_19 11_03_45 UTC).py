from PIL import Image
import pandas as pd

claims = pd.read_csv("dataset/claims.csv")

path = claims.iloc[0]["image_paths"].split(";")[0]

print("Image Path:", path)

img = Image.open("dataset/" + path)

print("Image Size:", img.size)