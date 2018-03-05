# Project : Disk Space - REST Service Generation with Swagger

## Objective :

This REST API is intended to find the disk space and  usage from localhost.

## Steps for creating the Server and client
1. On Ubuntu - Create a file "diskspace.yaml" file to define the structure of the service. 
2. Execute the below code for Server Side Stub Code Generation and Implementation with swagger-codegen (swagger-codegen-cli-2.3.1.jar).
java -jar swagger-codegen-cli-2.3.1.jar generate \
-i ~/github/cloudmesh-community/hid-sp18-520/Swagger/diskspace.yaml \
-l python-flask \
-o ~/github/cloudmesh-community/hid-sp18-520/Swagger/server/disks/flaskConnexion \
-D supportPython2=true
3. Update the code under server/disks/flaskconnexion folder.
4. Install and Run the REST Service and create the server - virtualenv environment.
5. Execute the below code for Installing and generating Client side code - virtualenv environment.
java -jar swagger-codegen-cli-2.3.1.jar generate \
-i ~/github/cloudmesh-community/hid-sp18-520/Swagger/diskspace.yaml \
-l python \
-o ~/github/cloudmesh-community/hid-sp18-520/Swagger/client/disks \
-D supportPython2=true

# Create the Bash Shell Script
## Server - 
Create the Bash Shell scripts which will download the Swagger Codegen 2.3.1 and create the Server with Code and Virtual Environment. 

Execute the bash script - mybashscript_Server.sh

## Client - 
Create the Bash Shell scripts which will download the Swagger Codegen 2.3.1 and create the Client with Code and Virtual Environment. 

Execute the bash script - mybashscript_Client.sh

## Execute on Server to verify - 
Verify the server with URL - on any browser http://localhost:8080/diskspace/TotalDisk 

Verify the server with URL - on any browser http://localhost:8080/diskspace/UsedDisk 

Verify the server with URL - on any browser http://localhost:8080/diskspace/FreeDisk 

Verify the server with URL - on any browser http://localhost:8080/diskspace/Diskusage 

## Execute with CURL - 

curl -H "Content-Type: application/json" http://localhost:8080/diskspace/TotalDisk

curl -H "Content-Type: application/json" http://localhost:8080/diskspace/UsedDisk

curl -H "Content-Type: application/json" http://localhost:8080/diskspace/FreeDisk

curl -H "Content-Type: application/json" http://localhost:8080/diskspace/Diskusage

## Execute with Client to verify - 

Create and Execute the "disk_test_script_clientDU.sh", calling to verify Disk Usage.

Create and Execute the "disk_test_script_clientFS.sh", calling to verify Free Disk.

Create and Execute the "disk_test_script_clientTS.sh", calling to verify Total Disk.

Create and Execute the "disk_test_script_clientUS.sh", calling to verify Used Disk.



