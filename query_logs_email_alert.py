from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
from datetime import timedelta
import smtplib
from email.message import EmailMessage

workspace_id = "<your-workspace-id>"

query = '''
Syslog
| where Facility == "authpriv"
| where SeverityLevel == "err"
| summarize FailedSSH=count() by HostName
'''

THRESHOLD = 5
EMAIL_FROM = "your-alert@example.com"
EMAIL_TO = "security-team@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your-smtp-user"
SMTP_PASSWORD = "your-smtp-password"

def send_email_alert(host, count):
    msg = EmailMessage()
    msg["Subject"] = f"SSH Login Anomaly on {host}"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content(f"Detected {count} failed SSH logins on {host} within the past hour.")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        print(f"Alert sent for {host}")

def main():
    credential = DefaultAzureCredential()
    client = LogsQueryClient(credential)
    response = client.query_workspace(
        workspace_id=workspace_id,
        query=query,
        timespan=timedelta(hours=1)
    )

    if response.tables:
        for row in response.tables[0].rows:
            host, count = row[0], row[1]
            print(f"{host}: {count} failed logins")
            if count >= THRESHOLD:
                send_email_alert(host, count)
    else:
        print("No data returned or error occurred.")

if __name__ == "__main__":
    main()