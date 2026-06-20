import pandas as pd

requirements_df = pd.read_csv(
    "dataset/evidence_requirements.csv"
)


def check_evidence(
    claim_object,
    image_result
):

    damage_visible = image_result.get(
        "damage_visible",
        False
    )

    if not damage_visible:
        return (
            False,
            "Damage not visible in image"
        )

    return (
        True,
        "Visible image evidence available"
    )