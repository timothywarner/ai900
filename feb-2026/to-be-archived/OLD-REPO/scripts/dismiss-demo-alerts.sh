#!/bin/bash

# Script to bulk dismiss Dependabot alerts for demo/sample code
# This uses GitHub CLI (gh) to dismiss alerts

echo "This script will help dismiss Dependabot alerts for demo code"
echo "Make sure you have GitHub CLI installed and authenticated"
echo ""

# Paths containing demo/sample code
DEMO_PATHS=(
    "apps/"
    "demos/"
    "docs/archive/lessons/"
)

echo "Fetching Dependabot alerts..."

# Get all open Dependabot alerts
alerts=$(gh api \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /repos/timothywarner/ai900/dependabot/alerts?state=open&per_page=100)

# Parse alerts and filter by path
echo "$alerts" | jq -r '.[] | select(.dependency.manifest_path | test("apps/|demos/|docs/archive/lessons/")) | .number' | while read -r alert_number; do
    echo "Dismissing alert #$alert_number (demo code)..."
    
    gh api \
      --method PATCH \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      /repos/timothywarner/ai900/dependabot/alerts/$alert_number \
      -f state='dismissed' \
      -f dismissed_reason='used_in_tests' \
      -f dismissed_comment='Demo/sample code for educational purposes only - not production code'
done

echo "Done! Remaining alerts should only be for root dependencies."