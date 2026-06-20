def check_evidence(
    claim_object,
    claim_data,
    image_result
):

    if not image_result.get("damage_visible", False):
        return (
            False,
            "Damage not visible"
        )

    claim_part = claim_data.get(
        "object_part",
        "unknown"
    )

    image_part = image_result.get(
        "object_part",
        "unknown"
    )

    if (
        claim_part != "unknown"
        and image_part != "unknown"
        and claim_part != image_part
    ):
        return (
            False,
            "Wrong object part visible"
        )

    return (
        True,
        "Minimum evidence requirement satisfied"
    )