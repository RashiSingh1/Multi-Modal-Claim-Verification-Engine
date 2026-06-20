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

    row = row.iloc[0]

    flags = []

    history_flag = str(
        row["history_flags"]
    ).strip()

    if (
        history_flag.lower() != "none"
        and history_flag != ""
    ):
        flags.append(history_flag)

    if row["rejected_claim"] >= 3:
        flags.append(
            "manual_review_required"
        )

    if row["last_90_days_claim_count"] >= 5:
        flags.append(
            "high_claim_frequency"
        )

    if len(flags) == 0:
        return "none"

    return ";".join(flags)