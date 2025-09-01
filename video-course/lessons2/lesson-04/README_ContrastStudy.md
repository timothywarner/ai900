# Contrast Study: Good Data vs. Bad Data for AI-900

This repository contains **two CSV datasets** plus this **Markdown** guide. The purpose is to demonstrate:

1. A **good_data.csv** file that embodies **Microsoft’s Responsible AI Principles**:
   - **Anonymized IDs** instead of personal names.
   - **No direct PII** (no phone numbers, addresses, etc.).
   - Balanced distribution of features (several regions, a range of ages, consistent labeling).
   - Clearly defined **features** (all columns except the final) vs. **label** (the final column).

2. A **bad_data.csv** file that violates multiple best practices:
   - **FullName**, **StreetAddress**, **PhoneNumber** columns reveal sensitive PII.
   - Unnecessary or questionable columns like “Blacklisted.”
   - Inconsistent label values (Yes, No, Maybe, or empty).
   - Missing or out-of-range numeric values (e.g., PerformanceRating can be 0 or 6, or missing).
   - Skewed/uniform region (everything is “North”), leading to potential bias.
   - Disorganized, incomplete, or erroneous rows.

## Key Teaching Points

- **Responsible AI** demands that data be collected and labeled **fairly**, with **privacy** and **security** in mind, and with **transparent** usage of features vs. labels.
- The **good_data.csv** shows a standard tabular layout ready for typical **classification** tasks (predicting “PromotionEligible”), with data that can be **one-hot encoded** or used as-is in many ML pipelines.
- The **bad_data.csv** highlights the pitfalls: from personal information leaks to label ambiguity, missing values, and potential biases.

## How to Use

1. **Load** `good_data.csv` in tools such as:
   - Azure Machine Learning Studio
   - VS Code + Python (Pandas)
   - Databricks or Spark (for bigger scale)
   - GitHub Codespaces or local Jupyter Notebooks

2. **Inspect** how easy it is to parse and model the “good” dataset. Notice consistent numeric columns, no hidden PII, and a clear target label.

3. **Load** `bad_data.csv`:
   - Observe the errors, missing data, out-of-bound values, etc.
   - Discuss how to fix or remove these columns and how that might reduce bias or risk.

4. **Emphasize** Microsoft Responsible AI Principles—ask learners to spot each violation in `bad_data.csv` (privacy, fairness, reliability, etc.).

5. **Extend** the data or create new synthetic variants for advanced labs. Show how “cleaning” the bad data can be done, bridging best practices and real-world scenarios.

## Enjoy Teaching!

Use these files in your **AI-900** or general ML classes to illustrate the difference between “solid, responsibly sourced data” vs. “chaotic, risk-laden data” in a memorable, hands-on way.
