# Introduction
This repo contains a Python script and files required to perform the following tasks:
1. Read a name from a file
2. Create an AAD group with the name from the previous step
3. In a filesystem in Azure Data Lake create a directory with the same name from step 1
4. Add 'r-x' permissions to the group from step 2 for the directory from step 3

# Pre-requisites
1. Azure account
2. Azure sp with AAD permissions and permissions to manage/create resources
3. Python 3+