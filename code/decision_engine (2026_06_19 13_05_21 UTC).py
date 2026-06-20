def make_decision(
    claim_issue,
    image_issue
):

    claim_issue = str(claim_issue).lower()
    image_issue = str(image_issue).lower()

    if image_issue == "none":
        return (
            "not_enough_information",
            "No visible damage found"
        )

    if claim_issue in image_issue:
        return (
            "supported",
            "Image supports claim"
        )

    return (
        "contradicted",
        "Visible damage differs from claim"
    )