#!/bin/bash
echo "Verify the service as below to fetch the disk usage details on LocalHost"

echo "Verify the server with URL - http://localhost:8080/cloudmesh/disk/TotalDisk on any browser"
echo "Verify the server with URL - http://localhost:8080/cloudmesh/disk/UsedDisk on any browser"
echo "Verify the server with URL - http://localhost:8080/cloudmesh/disk/FreeDisk on any browser"
echo "Verify the server with URL - http://localhost:8080/cloudmesh/disk/Diskusage on any browser"

echo "Execute the CURL command"

curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/TotalDisk
curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/UsedDisk
curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/FreeDisk
curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Diskusage
