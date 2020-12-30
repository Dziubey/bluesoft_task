import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.identity import ClientSecretCredential
from azure.graphrbac import GraphRbacManagementClient
from azure.graphrbac.models import GroupCreateParameters
from azure.storage.filedatalake import DataLakeServiceClient

import subprocess

# Retrieve the IDs and secret to use with ServicePrincipalCredentials
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
tenant_id = os.environ["AZURE_TENANT_ID"]
client_id = os.environ["AZURE_CLIENT_ID"]
client_secret = os.environ["AZURE_CLIENT_SECRET"]

# Create credentials object that will be used for authentication
creds = ServicePrincipalCredentials(tenant=tenant_id, client_id=client_id, secret=client_secret)

# Read the group name from file
f = open("groups.txt")
group_name = f.readline()

# Create rbac credentials object
rbac_creds = ServicePrincipalCredentials(tenant = tenant_id, client_id = client_id, secret = client_secret, resource="https://graph.windows.net")

# Create graphrbac client used to create the aad group
graphrbac_client = GraphRbacManagementClient(
    rbac_creds,
    tenant_id
    )

# Create aad group
group = GroupCreateParameters(display_name=group_name, mail_nickname="GroupMail-at-microsoft.com")
graphrbac_client.groups.create(group)

# Change permissions of the bash script used to retrieve aad group ID
os.chmod('./script.sh', 0o755)
rc = subprocess.call("./script.sh")

# Retrieve the aad group ID from file
f = open("groupid.txt")
group_id = str(f.readline())

# Create storage account credentials
storage_creds = ClientSecretCredential(tenant_id = tenant_id, client_id = client_id, client_secret = client_secret)

# Perform the data lake tasks
dl_service_client = DataLakeServiceClient(account_url="https://bluesofttaskdd.dfs.core.windows.net/", credential=storage_creds)

file_system_client = dl_service_client.get_file_system_client(file_system='file-system')
file_system_client.create_directory(group_name)

directory_client = file_system_client.get_directory_client(group_name)
directory_client.set_access_control(acl=f"default:group:{group_id}:r-x")

