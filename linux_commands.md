# Linux Commands Used

```bash
# Update package list
sudo apt update

# Install stress utility to generate CPU load
sudo apt install stress -y

# Run stress test (1 CPU core for 15 seconds)
stress --cpu 1 --timeout 15

# Check running processes
top

# View system uptime
uptime

# View system info
uname -a

# (Optional) Check log agent service logs
journalctl -u walinuxagent

# Exit SSH session
exit
```
