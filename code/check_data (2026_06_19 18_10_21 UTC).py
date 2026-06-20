import pandas as pd

print("USER HISTORY")
print(pd.read_csv("dataset/user_history.csv").head())

print("\nEVIDENCE REQUIREMENTS")
print(pd.read_csv("dataset/evidence_requirements.csv").head())