# Security Policy

## Scope

This repository contains educational materials and demo code for the Microsoft Azure AI Fundamentals (AI-900) certification course. 

### Production Code
- Root directory dependencies only
- GitHub Actions workflows
- Main documentation

### Demo/Sample Code (Not Production)
The following directories contain demo and sample code for educational purposes only and are NOT intended for production use:
- `/apps/` - Demo applications
- `/demos/` - Course demonstrations
- `/docs/archive/lessons/` - Archived lesson materials
- `/assets/` - Sample data files

## Reporting Security Vulnerabilities

For vulnerabilities in:
- **Root dependencies**: Please report immediately
- **Demo/sample code**: These are educational examples only and vulnerabilities are expected in older samples

## Dependabot Configuration

Dependabot is configured to:
- Monitor root directory dependencies only
- Ignore all demo and sample code subdirectories
- Create PRs only for direct production dependencies

To bulk dismiss alerts for demo code, maintainers can use GitHub's security tab to dismiss alerts in bulk by selecting multiple alerts and choosing "Dismiss" with reason "Used in tests" or "No bandwidth to fix".