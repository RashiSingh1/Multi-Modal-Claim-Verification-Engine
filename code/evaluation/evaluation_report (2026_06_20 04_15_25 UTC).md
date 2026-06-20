# Insurance Claim Review System

## Overview

This project automates the review of insurance claims by analyzing:

1. Customer claim descriptions
2. Uploaded image evidence
3. User risk indicators

The system generates a structured output showing whether the submitted evidence supports the customer's claim.

---

## Features

### Claim Parsing
Extracts:

- Issue Type
- Object Part
- Claim Summary

from customer conversations.

Examples:

- "door dent" → dent, door
- "windshield crack" → crack, windshield
- "keyboard damage" → damage, keyboard

---

### Image Analysis

The image analyzer identifies:

- Object Type
- Object Part
- Damage Type
- Severity
- Damage Visibility

Example output:

```json
{
  "object_type": "car",
  "object_part": "bumper",
  "damage_type": "dent",
  "severity": "medium",
  "damage_visible": true
}
```

---

### Risk Detection

The risk engine identifies users requiring additional review.

Possible flags:

- user_history_risk
- manual_review_required
- high_claim_frequency

---

### Evidence Validation

The evidence checker verifies whether:

- claim object matches image object
- claimed part matches visible part
- visible damage exists

---

### Decision Engine

Generates final claim status:

| Status | Meaning |
|----------|----------|
| supported | Evidence matches claim |
| contradicted | Evidence conflicts with claim |
| not_enough_information | Insufficient evidence |

---

## Project Structure

```text
code/
│
├── main.py
├── claim_parser.py
├── image_analyzer.py
├── risk_engine.py
├── evidence_checker.py
├── decision_engine.py
│
dataset/
│
├── claims.csv
│
output.csv
README.md
```

---

## Workflow

```text
Claims CSV
      │
      ▼
Claim Parser
      │
      ▼
Image Analyzer
      │
      ▼
Risk Engine
      │
      ▼
Evidence Checker
      │
      ▼
Decision Engine
      │
      ▼
Output CSV
```

---

## Running the Project

### Install dependencies

```bash
pip install pandas pillow python-dotenv
```

### Run

```bash
python code/main.py
```

---

## Output

The system generates:

```text
output.csv
```

Columns:

- user_id
- image_paths
- user_claim
- claim_object
- evidence_standard_met
- evidence_standard_met_reason
- risk_flags
- issue_type
- object_part
- claim_status
- claim_status_justification
- supporting_image_ids
- valid_image
- severity

---

## Example Result

```csv
user_003,...,supported,Visible damage matches claim
```

```csv
user_004,...,contradicted,Visible damage differs from claim
```

---

## Assumptions

1. Only visible damage is considered evidence.
2. First valid supporting image is selected.
3. Risk flags are simulated using predefined rules.
4. Claim parsing uses keyword extraction.
5. Image analysis currently uses rule-based detection.

---

## Future Improvements

- Gemini Vision integration
- YOLO-based damage detection
- OCR for image text extraction
- Multi-image consensus scoring
- Fraud detection model
- Confidence scoring

---

## Author

Rashi Kumari

Built for automated insurance claim review and evidence verification.