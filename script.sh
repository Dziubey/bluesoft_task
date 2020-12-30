#!/bin/sh

group_name=$(head -n 1 groups.txt)

az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID

group=$(az ad group show --group $group_name)
id=$(echo $group | jq -r '.objectId')
echo $id >> "groupid.txt"
truncate -s -1 "groupid.txt"