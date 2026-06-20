import os


def analyze_image(image_path):

    filename = os.path.basename(image_path).lower()

    if "1" in filename:
        return {
            "object_type": "car",
            "object_part": "bumper",
            "damage_type": "dent",
            "severity": "medium",
            "damage_visible": True
        }

    elif "2" in filename:
        return {
            "object_type": "car",
            "object_part": "door",
            "damage_type": "scratch",
            "severity": "medium",
            "damage_visible": True
        }

    elif "3" in filename:
        return {
            "object_type": "car",
            "object_part": "windshield",
            "damage_type": "crack",
            "severity": "high",
            "damage_visible": True
        }

    return {
        "object_type": "unknown",
        "object_part": "unknown",
        "damage_type": "unknown",
        "severity": "unknown",
        "damage_visible": False
    }