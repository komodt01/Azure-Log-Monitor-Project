# Lessons Learned

- Azure Monitor logs flow successfully into Log Analytics when the diagnostic setting is configured with the correct workspace.
- The Azure Monitor Python SDK (`azure-monitor-query`) uses `DefaultAzureCredential`, which can silently default to the wrong tenant/subscription in multi-tenant Azure setups.
- CLI context does not always align with SDK context — even if `az account show` confirms the right subscription.
- Workspace query failures (`PathNotFoundError`, `WorkspaceNotFoundError`) can occur even when the workspace clearly exists — often due to tenant mismatches.
- Switching tenants or using a personal Microsoft account can lead to inconsistent SDK results.
- KQL and the Log Analytics UI were reliable fallbacks for validation when programmatic methods failed.
