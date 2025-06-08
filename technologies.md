# Technologies Used

## 1. Azure Log Analytics
**What it is**: A central logging service that collects, indexes, and queries logs from Azure resources.

**Why it's used**: Provides real-time visibility and advanced querying using KQL for system and security events.

**How it works**: Logs are ingested via diagnostic settings and stored in a workspace. You query logs using Kusto Query Language (KQL).

---

## 2. Azure Linux Virtual Machine
**What it is**: A compute instance running Ubuntu 22.04 in Azure.

**Why it's used**: Simulates SSH login behavior and generates logs for monitoring.

**How it works**: It sends syslog and performance data to Log Analytics via diagnostic settings.

---

## 3. Diagnostic Settings
**What it is**: A feature that routes logs/metrics from Azure resources to destinations like Log Analytics.

**Why it's used**: Enables collection of VM logs without needing agents.

**How it works**: Once configured, logs are forwarded in near real-time to the workspace.

---

## 4. Azure Monitor Query SDK (Python)
**What it is**: A Python SDK to query Log Analytics data programmatically.

**Why it's used**: Allows automated detection, filtering, and custom logic for alerting or ticketing.

**How it works**: Authenticates via Entra ID and sends KQL queries using the `LogsQueryClient`.

---

## 5. Entra ID (Azure AD)
**What it is**: Azure’s cloud-based identity provider.

**Why it's used**: Provides authentication for users and apps, and handles RBAC for workspace access.

**How it works**: Terraform grants your user (or SPN) `Log Analytics Reader` permission using its object ID.