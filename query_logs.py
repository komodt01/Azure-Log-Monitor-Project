from azure.identity import AzureCliCredential
from azure.monitor.query import LogsQueryClient
from datetime import timedelta

# Replace with your actual Log Analytics Workspace ID
workspace_id = "<your-workspace-id>"

# KQL query to get failed SSH login attempts
query = '''
Syslog
| where Facility == "authpriv"
| where SeverityLevel == "err"
| summarize count() by HostName
'''

def main():
    credential = AzureCliCredential()
    client = LogsQueryClient(credential)

    response = client.query_workspace(
        workspace_id = "/subscriptions/7d939770-deef-433d-9283-5bd5eb79aeaf/resourceGroups/log-auto-rg/providers/Microsoft.OperationalInsights/workspaces/log-auto-ws",
        query=query,
        timespan=timedelta(hours=1)
    )

    if response.tables:
        for table in response.tables:
            for row in table.rows:
                print(row)
    else:
        print("No results found or error occurred.")

if __name__ == "__main__":
    main()
