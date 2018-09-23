﻿# Disk - REST Server Service with Swagger

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

# Makefile Script details
## Server - 
Create the Make file which asssumes to have SwaggerCodegen (Swagger Codegen 2.3.1) downloaded, create the Server with Code and Virtual Environment. 

Execute the commands from the Makefile.

Prerequisite: store the path to swagger codegen jarfile in an environment variable named swagger_codegen

```SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar```

Command to generate swagger code run the command

```make service```

Command to run the code, execute the following

```make run```

Command to test the service is up and running on local machine 

```make test```

Command to remove swagger codegen files run the command, and clean the directory

```make clean```


## Execute on Server to verify - 
Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/TotalD 

Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/UsedD 

Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/FreeD 

Verify the server with URL - on any browser http://localhost:8080/cloudmesh/disk/Dusage 

Verify the server with URL - on any browser  http://localhost:8080/cloudmesh/disk/Mgmtusage

Verify the server with URL - on any browser  http://localhost:8080/cloudmesh/disk/Diocounter

## Execute with CURL - 
```curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/TotalD```

```curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/UsedD```

```curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/FreeD```

```curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Dusage```

```curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Mgmtusage```

```curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Diocounter```


# Docker - 

Create the Image and Container with following commands - build the image, container from Dockerfile and push it to Docker Hub - 

```docker build -t resourcediskdetail_swagger .```

```docker run -p 8080:8080 arisinha/resourcediskdetail_swagger```

```docker push arisinha/resourcediskdetail_swagger```

Pull the public Image and run with below commands -

```docker pull arisinha/resourcediskdetail_swagger```

```docker run -p 8080:8080 arisinha/resourcediskdetail_swagger```

﻿# Test Results - 
## Make Command Execution from Terminal and Browser - 

### From Terminal

![Alt](TestResultScreenshots/Screenshot_Make_Server_results1.png)

![Alt](TestResultScreenshots/Screenshot_Make_Server_results2.png)

### From Browser
* Total Disk
![Alt](TestResultScreenshots/ScreenshotWebTotalDisk.png)

* Used Disk
![Alt](TestResultScreenshots/ScreenshotWebUsedDisk.png)

* Free Disk
![Alt](TestResultScreenshots/ScreenshotWebFreeDisk.png)

* Disk Usage
![Alt](TestResultScreenshots/ScreenshotWebDiskUsage.png)

* Disk Partition
![Alt](TestResultScreenshots/ScreenshotfromBrowserDiskMgmt.png)

* Disk IO
![Alt](TestResultScreenshots/ScreenshotfromBrowserDiskIO.png)

## Docker Container Execution

Docker Build 
![Alt](TestResultScreenshots/DockerBuildCompletion.png)

Docker Start 
![Alt](TestResultScreenshots/DockerStartServer.png)

* Total Disk
![Alt](TestResultScreenshots/FromContainer_TotalDisk.png)

* Used Disk
![Alt](TestResultScreenshots/FromContainer_UsedDisk.png)

* Free Disk
![Alt](TestResultScreenshots/FromContainer_FreeDisk.png)

* Disk Usage
![Alt](TestResultScreenshots/FromContainer_DiskUsage.png)

* Disk Partition
![Alt](TestResultScreenshots/FromContainer_Diskpartition.png)

* Disk IO
![Alt](TestResultScreenshots/FromContainer_DiskIO.png)

## Kill The process running -

![Alt](TestResultScreenshots/KillProcess.png)
