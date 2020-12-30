# Introduction
This repo contains a Python script and files required to perform the following tasks:
1. Read a name from a file
2. Create an AAD group with the name from the previous step
3. In a filesystem in Azure Data Lake create a directory with the same name from step 1
4. Add 'r-x' permissions to the group from step 2 for the directory from step 3

# Pre-requisites
1. Azure account
2. Azure sp with AAD permissions and permissions to manage/create resources
3. SP credentials exported as environment variables
4. Python 3+ with pip and venv
5. Storage account configured as a data lake
6. File system created in the storage account

# Steps
1. Clone the repo
2. Update the groups.txt file with your aad group name (follow Azure group naming convention)
3. Create virtual environment by runnning 'python3 -m venv ENV_NAME
4. Activate venv by running 'source ENV_NAME/bin/activate
5. Install required packages by running 'pip install -r required_packages.txt'
6. Execute the Python script
7. Verify the group and directory has been created, and permissions added successfully (you can use the Azure storage explorer for this)