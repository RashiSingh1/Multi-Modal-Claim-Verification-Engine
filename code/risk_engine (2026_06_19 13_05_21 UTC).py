import pandas as pd

history_df = pd.read_csv(
    "dataset/user_history.csv"
)


def get_risk_flags(user_id):

    row = history_df[
        history_df["user_id"] == user_id
    ]

    if len(row) == 0:
        return "none"

    return row.iloc[0]["history_flags"]