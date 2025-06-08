# Azure Log Monitor Project (Terraform)

## Overview
This project provisions a Log Analytics monitoring stack in Azure using Terraform.
It includes:
- A Linux virtual machine (Ubuntu)
- A Network Security Group (NSG)
- A Log Analytics Workspace
- Diagnostic settings wired to capture metrics
- KQL query experimentation via Python and SDK

## Technologies Used
- Azure Monitor & Log Analytics
- Azure Linux VM
- Terraform
- Azure CLI
- Python SDK (`azure-monitor-query`)
- Diagnostic Settings & Azure Monitor Agent

## Lessons Learned
See `lessonslearned.md` for in-depth edge case notes and pitfalls with SDK authentication and subscription handling.

## How to Run
1. Initialize: `terraform init`
2. Plan: `terraform plan`
3. Apply: `terraform apply`
4. SSH into VM, run stress test
5. Monitor logs via Portal or Python

## Cleanup
Use `terraform destroy` or refer to the included teardown script.
