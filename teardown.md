# Teardown Guide

To fully remove all resources and prevent charges:

1. Destroy the infrastructure:
    ```bash
    terraform destroy -var-file="terraform.tfvars"
    ```

2. Confirm that the following are deleted:
   - Resource Group
   - VM, NIC, NSG, VNet
   - Log Analytics Workspace

3. Check the Azure Portal to ensure no lingering resources remain.

4. Optionally, delete the Terraform state files:
    ```bash
    rm -rf .terraform terraform.tfstate* crash.log
    ```