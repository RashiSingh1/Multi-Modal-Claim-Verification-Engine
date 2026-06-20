# Multi-Modal Claim Verification Engine

AI-powered insurance claim verification system that analyzes claim conversations, submitted images, user history, and evidence requirements to determine whether a damage claim is supported, contradicted, or lacks sufficient evidence.

## Features

* Claim information extraction from user conversations
* Image-based damage analysis
* Evidence validation against predefined requirements
* User risk assessment using claim history
* Automated claim decision generation
* Severity estimation
* Supporting image identification
* Modular and extensible architecture

## Project Structure

```text
code/
├── main.py
├── claim_parser.py
├── image_analyzer.py
├── evidence_checker.py
├── decision_engine.py
├── risk_engine.py

evaluation/
└── evaluation_report.md
```

## Workflow

1. Parse user claim
2. Analyze submitted images
3. Evaluate evidence quality
4. Assess user risk indicators
5. Generate claim decision
6. Produce structured output

## Output Fields

* evidence_standard_met
* risk_flags
* issue_type
* object_part
* claim_status
* supporting_image_ids
* severity

## Technologies Used

* Python
* Pandas
* CSV Processing
* Rule-Based Decision Systems

## Use Case

Designed for automated insurance-style damage claim verification across:

* Cars
* Laptops
* Packages

## Author

Rashi Kumari
