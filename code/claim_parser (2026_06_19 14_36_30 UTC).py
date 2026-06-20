def extract_claim(claim_text):

    text = claim_text.lower()

    issue_type = "unknown"
    object_part = "unknown"

    # damage types
    if "crack" in text or "cracked" in text:
        issue_type = "crack"

    elif "dent" in text or "dented" in text:
        issue_type = "dent"

    elif "scratch" in text or "scratched" in text:
        issue_type = "scratch"

    elif "broken" in text:
        issue_type = "broken"

    elif "shattered" in text:
        issue_type = "shattered"

    elif "tear" in text or "torn" in text:
        issue_type = "tear"

    # object parts
    parts = [
        "screen",
        "bumper",
        "door",
        "hood",
        "windshield",
        "keyboard",
        "trackpad",
        "box",
        "package",
        "corner",
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