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

    if "history_flags" not in row.columns:
        return "none"

    value = str(
        row.iloc[0]["history_flags"]
    )

    if value == "nan":
        return "none"

    return value

    row = history_df[
        history_df["user_id"] == user_id
    ]

    if len(row) == 0:
        return "none"

    return row.iloc[0]["history_flags"]