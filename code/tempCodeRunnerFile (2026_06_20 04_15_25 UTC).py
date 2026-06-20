import pandas as pd

from claim_parser import extract_claim
from image_analyzer import analyze_image
from risk_engine import get_risk_flags
from decision_engine import make_decision
from evidence_checker import check_evidence


def main():

    claims_df = pd.read_csv("dataset/claims.csv")

    results = []

    total = len(claims_df)

    for index, row in claims_df.iterrows():

        print(f"Processing {index + 1}/{total}")

        user_id = row["user_id"]
        claim_text = row["user_claim"]
        claim_object = row["claim_object"]
        image_paths = row["image_paths"].split(";")

        try:

            claim_data = extract_claim(claim_text)

            best_image_result = None
            supporting_image = "none"

            for img_path in image_paths:

                full_path = "dataset/" + img_path

                try:

                    image_result = analyze_image(full_path)

                    if image_result.get("damage_visible", False):

                        best_image_result = image_result
                        supporting_image = (
                            img_path.split("/")[-1]
                            .replace(".jpg", "")
                            .replace(".png", "")
                        )

                        break

                except Exception as image_error:

                    print(
                        f"Image error: {img_path}",
                        image_error
                    )

            risk_flags = get_risk_flags(user_id)

            if best_image_result is None:

                results.append({

                    "user_id": user_id,
                    "image_paths": row["image_paths"],
                    "user_claim": claim_text,
                    "claim_object": claim_object,

                    "evidence_standard_met": "false",
                    "evidence_standard_met_reason":
                    "No image contained reviewable damage evidence",

                    "risk_flags": risk_flags,

                    "issue_type": "unknown",
                    "object_part": "unknown",

                    "claim_status":
                    "not_enough_information",

                    "claim_status_justification":
                    "No visible damage found in submitted images",

                    "supporting_image_ids": "none",

                    "valid_image": "false",

                    "severity": "unknown"
                })

                continue

            evidence_met, evidence_reason = check_evidence(
                claim_object,
                claim_data,
                best_image_result
            )

            claim_issue = claim_data.get(
                "issue_type",
                "unknown"
            )

            image_issue = best_image_result.get(
                "damage_type",
                "unknown"
            )

            claim_status, justification = make_decision(
                claim_issue,
                image_issue
            )

            results.append({

                "user_id": user_id,
                "image_paths": row["image_paths"],
                "user_claim": claim_text,
                "claim_object": claim_object,

                "evidence_standard_met":
                str(evidence_met).lower(),

                "evidence_standard_met_reason":
                evidence_reason,

                "risk_flags":
                risk_flags,

                "issue_type":
                image_issue,

                "object_part":
                best_image_result.get(
                    "object_part",
                    "unknown"
                ),

                "claim_status":
                claim_status,

                "claim_status_justification":
                justification,

                "supporting_image_ids":
                supporting_image,

                "valid_image":
                "true",

                "severity":
                best_image_result.get(
                    "severity",
                    "unknown"
                )
            })

        except Exception as e:

            print(
                f"Claim processing failed: {user_id}",
                e
            )

            results.append({

                "user_id": user_id,
                "image_paths": row["image_paths"],
                "user_claim": claim_text,
                "claim_object": claim_object,

                "evidence_standard_met": "false",

                "evidence_standard_met_reason":
                str(e),

                "risk_flags":
                "none",

                "issue_type":
                "unknown",

                "object_part":
                "unknown",

                "claim_status":
                "not_enough_information",

                "claim_status_justification":
                "Claim processing failed",

                "supporting_image_ids":
                "none",

                "valid_image":
                "false",

                "severity":
                "unknown"
            })

    output_df = pd.DataFrame(results)

    output_df.to_csv(
        "output.csv",
        index=False
    )

    print("\nDone!")
    print("output.csv generated")


if __name__ == "__main__":
    main()