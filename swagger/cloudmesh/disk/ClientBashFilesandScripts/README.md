# Project : Disk - RESTCLIENT Service Generation with Swagger

## Objective :

This REST API is intended to find the disk space and  usage from localhost.

## Steps for creating the client
1. On Ubuntu - Once you have created the Server service using Swagger Codegen. 
2. Execute the below code for Installing and generating Client side code - virtualenv environment.
java -jar swagger-codegen-cli-2.3.1.jar generate \
-i ~/github/cloudmesh-community/hid-sp18-520/Swagger/diskspace.yaml \
-l python \
-o ~/github/cloudmesh-community/hid-sp18-520/Swagger/client/disks \
-D supportPython2=true

## Client - 
Execute the bash script - mybashscript_Client.sh

## Execute with Client to verify - 

Create and Execute the "python disk_test_script_clientDU.py", calling to verify Disk Usage.

Create and Execute the "python disk_test_script_clientFS.py", calling to verify Free Disk.

Create and Execute the "python disk_test_script_clientTS.py", calling to verify Total Disk.

Create and Execute the "python disk_test_script_clientUS.py", calling to verify Used Disk.
