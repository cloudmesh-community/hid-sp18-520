# Project : Disk - REST Server Service Generation with Swagger

## Objective :

This REST API is intended to find the disk space and  usage from localhost.

## Steps for creating the Server and client (Manual Execution)
1. On Ubuntu - Create a file "diskspace.yaml" file to define the structure of the service. 
2. Execute the below code for Server Side Stub Code Generation and Implementation with swagger-codegen (swagger-codegen-cli-2.3.1.jar).
java -jar swagger-codegen-cli-2.3.1.jar generate \
-i ~/github/cloudmesh-community/hid-sp18-520/Swagger/diskspace.yaml \
-l python-flask \
-o ~/github/cloudmesh-community/hid-sp18-520/Swagger/server/disks/flaskConnexion \
-D supportPython2=true
3. Update the code under server/disks/flaskconnexion folder.

# Create the Makefile Script
## Server - 
Create the Make file which asssumes to have SwaggerCodegen (Swagger Codegen 2.3.1) downloaded, create the Server with Code and Virtual Environment. 

Execute the Make file - Makefile

prerequisite: store the path to swagger codegen jarfile in an environment variable named swagger_codegen

export swagger_codegen="path to swagger codegen jarfile"

Command to generate swagger code run the command
make

Command to run the code, execute the following

make run

Command to remove swagger codegen files run the command, and clean the directory

make clean


## Execute on Server to verify - 
Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/TotalDisk 

Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/UsedDisk 

Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/FreeDisk 

Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/Diskusage 


## Execute with CURL - 
curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/TotalDisk

curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/UsedDisk

curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/FreeDisk

curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Diskusage

