# Multi-Modal Claim Verification Engine

An AI-powered insurance claim verification system that analyzes claim conversations, submitted images, user history, and evidence requirements to determine whether a damage claim is **supported**, **contradicted**, or **lacks sufficient evidence**.

Automates a process that is traditionally manual, slow, and inconsistent across reviewers — combining conversational parsing, image analysis, and rule-based decisioning into a single end-to-end verification pipeline.

## Background

Developed as a submission for HackerRank Orchestrate — [June] 2026 Edition, where it cleared the AI Judge evaluation round.

## Problem Statement

Insurance claim verification typically relies on manual review of user-submitted evidence, conversation history, and policy requirements — a process prone to inconsistency, delay, and human error. This engine automates that pipeline, producing structured, auditable claim decisions.

## Features

- Claim information extraction from unstructured user conversations
- Image-based damage analysis and severity estimation
- Evidence validation against predefined coverage requirements
- User risk assessment based on historical claim behavior
- Automated, explainable claim decision generation
- Supporting image identification, mapped to specific claim issues
- Modular, extensible architecture for adding new claim categories

## Architecture

```text
code/
├── main.py               # Entry point — orchestrates the verification pipeline
├── claim_parser.py       # Extracts structured claim data from conversations
├── image_analyzer.py     # Analyzes submitted images for damage evidence
├── evidence_checker.py   # Validates evidence against requirements
├── decision_engine.py    # Produces final claim decision
├── risk_engine.py        # Computes user risk indicators
evaluation/
└── evaluation_report.md  # Evaluation methodology and results
```

## Workflow

1. Parse the user's claim conversation into structured fields
2. Analyze submitted images for damage type, location, and severity
3. Evaluate evidence quality against category-specific requirements
4. Assess user risk indicators from claim history
5. Generate a claim decision with supporting rationale
6. Produce structured, machine-readable output

## Output Schema

| Field | Description |
|---|---|
| `evidence_standard_met` | Whether submitted evidence meets the required standard |
| `risk_flags` | Risk indicators derived from user history |
| `issue_type` | Category of reported damage |
| `object_part` | Specific part or component affected |
| `claim_status` | Final outcome: supported/contradicted / insufficient evidence |
| `supporting_image_ids` | Images used as evidence for the decision |
| `severity` | Estimated severity of the reported damage |

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, CSV pipelines
- **Decision Logic:** Rule-based decision systems
- **AI/LLM:** Gemini API

## Use Cases

Built for automated damage-claim verification across:
- Vehicles
- Electronics (laptops, devices)
- Shipped packages

## Author

**Rashi Kumari**
