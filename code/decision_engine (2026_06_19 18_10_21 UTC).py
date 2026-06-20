def make_decision(claim_issue, image_issue):

    claim_issue = str(claim_issue).lower()
    image_issue = str(image_issue).lower()

    if image_issue in ["none", "unknown"]:
        return (
            "not_enough_information",
            "No visible damage found"
        )

    similar_damage = {
        "crack": ["crack", "shattered"],
        "shattered": ["shattered", "crack"],
        "broken": ["broken", "broken_part"],
        "broken_part": ["broken", "broken_part"],
        "dent": ["dent"],
        "scratch": ["scratch"],
        "tear": ["tear", "torn_packaging"]
    }

    if image_issue in similar_damage.get(claim_issue, []):
        return (
            "supported",
            "Visible damage matches claim"
        )

    return (
        "contradicted",
        "Visible damage differs from claim"
    )