# Compliance Mapping – Azure Log Monitoring Project

This project aligns with several key controls across major compliance frameworks.

---

## 🛡 NIST 800-53

| Control ID | Control Name                  | How This Project Satisfies It                                      |
|------------|-------------------------------|---------------------------------------------------------------------|
| AU-2       | Audit Events                  | Captures and stores Linux syslog via Diagnostic Settings.          |
| AU-6       | Audit Review, Analysis        | Uses KQL queries and Python SDK to analyze failed login attempts.  |
| AU-12      | Audit Generation              | Enables audit logging on VM resources automatically.               |
| SI-4       | Information System Monitoring | Monitors for anomalies (e.g., brute-force SSH attempts).           |

---

## ✅ ISO/IEC 27001

| Clause     | Control Name                     | Implementation Summary                                             |
|------------|----------------------------------|--------------------------------------------------------------------|
| A.12.4.1   | Event Logging                    | Syslog data collected into a centralized Log Analytics Workspace.  |
| A.12.4.3   | Administrator and Operator Logs  | Admin login attempts and system activity monitored.                |
| A.16.1.4   | Assessment of and Decision on Events | Alerts sent via email if anomalies exceed thresholds.         |

---

## ⚖️ CIS Controls v8

| Control ID | Description                          | Coverage                                                          |
|------------|--------------------------------------|-------------------------------------------------------------------|
| 8.2        | Collect Audit Logs                   | VM logs collected using Azure Monitor Diagnostic Settings.        |
| 8.7        | Retain Audit Logs                    | Logs retained in Log Analytics with configurable retention period.|
| 6.3        | Centralize Security Event Alerting   | Python script with email alerts when thresholds are exceeded.     |