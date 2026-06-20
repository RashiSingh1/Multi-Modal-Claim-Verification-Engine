def extract_claim(claim_text):

    text = claim_text.lower()

    issue_type = "unknown"
    object_part = "unknown"

    damage_keywords = {
        "scratch": "scratch",
        "scratched": "scratch",
        "dent": "dent",
        "dented": "dent",
        "crack": "crack",
        "cracked": "crack",
        "broken": "broken",
        "shattered": "shattered",
        "tear": "tear",
        "torn": "tear"
    }

    for key, value in damage_keywords.items():
        if key in text:
            issue_type = value
            break

    parts = [
        "bumper",
        "door",
        "hood",
        "windshield",
        "screen",
        "keyboard",
        "trackpad",
        "corner",
        "box",
        "package",
        "lid"
    ]

    for part in parts:
        if part in text:
            object_part = part
            break

    return {
        "issue_type": issue_type,
        "object_part": object_part,
        "claim_summary": claim_text
    }