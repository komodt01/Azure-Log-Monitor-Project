output "log_analytics_workspace_id" {
  value = azurerm_log_analytics_workspace.main.id
}

output "vm_public_ip" {
  value = azurerm_public_ip.main.ip_address
}