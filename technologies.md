# Technologies Used

This project uses several Azure-native services and supporting tools to build a complete log monitoring and security visibility pipeline. Each technology is listed with **what it is**, **why it’s used**, and **how it works** in the context of this project.

---

## 1. Azure Log Analytics Workspace
**What it is:**  
A centralized logging platform in Azure that stores and indexes logs from Azure resources, VMs, and on-prem systems.

**Why it’s used:**  
Log Analytics is the core of Azure’s monitoring ecosystem. It enables deep visibility into system, audit, and security events using Kusto Query Language (KQL).

**How it works:**  
Data is ingested from the Azure Monitor Agent and Diagnostic Settings, then stored in tables such as `Syslog`, `Heartbeat`, and `Perf`. KQL queries retrieve and filter data for investigation, dashboards, or alerting.

---

## 2. Azure Linux Virtual Machine (Ubuntu 22.04)
**What it is:**  
A compute instance running Ubuntu in Azure.

**Why it’s used:**  
Provides a real workload that generates system logs (SSH authentication, kernel logs, sudo events, service activity) that can be monitored for operational or security patterns.

**How it works:**  
The VM is deployed with an NSG for restricted access and the Azure Monitor Agent (AMA), which forwards system, syslog, and performance data to Log Analytics.

---

## 3. Azure Monitor Agent (AMA)
**What it is:**  
Azure’s current unified monitoring agent replacing the legacy OMS/LAD/Diagnostic Extensions.

**Why it’s used:**  
AMA is required for collecting Syslog and performance metrics from Azure VMs. It provides better security, consistency, and configuration than old agents.

**How it works:**  
The agent is installed as a VM extension. Data Collection Rules determine which log categories to send (e.g., auth logs, syslog facilities, performance counters). AMA streams data into the associated Log Analytics workspace.

---

## 4. Diagnostic Settings
**What it is:**  
A native Azure feature that routes platform logs and metrics to destinations like Log Analytics, Event Hub, or Storage.

**Why it's used:**  
Allows collection of Azure resource logs (compute, network, platform metrics) without needing custom agents. Used to forward Azure platform-level metrics and activities.

**How it works:**  
Once configured, Diagnostic Settings push logs/metrics to the workspace in near real-time using Azure Monitor’s ingestion pipeline.

---

## 5. Azure Monitor Query SDK (Python)
**What it is:**  
A Python library that communicates with Azure Monitor/Log Analytics to run KQL queries programmatically.

**Why it’s used:**  
Enables automation—Python scripts can detect events, extract log insights, perform alerting, or integrate with ticketing/email systems.

**How it works:**  
The script authenticates via Entra ID (device login or service principal), then executes KQL queries via `LogsQueryClient`. Results are parsed and optionally used to trigger an alert workflow.

---

## 6. Microsoft Entra ID (Azure AD)
**What it is:**  
Azure’s identity and access management service.

**Why it's used:**  
Provides authentication and authorization for Terraform, Log Analytics access, Python SDK login, and role assignments.

**How it works:**  
Terraform assigns the authenticated user (via their Entra object ID) the **Log Analytics Reader** role, enabling access to workspace queries. Python uses the same identity to query logs using Azure’s credential chain.

---
