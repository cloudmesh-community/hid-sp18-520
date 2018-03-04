echo "Verify the service as below to fetch the disk usage details on LocalHost"

echo "Verify the server with URL - http://localhost:8080/diskspace/TotalDisk on any browser"
echo "Verify the server with URL - http://localhost:8080/diskspace/UsedDisk on any browser"
echo "Verify the server with URL - http://localhost:8080/diskspace/FreeDisk on any browser"
echo "Verify the server with URL - http://localhost:8080/diskspace/Diskusage on any browser"

echo "Execute the CURL command"

curl -H "Content-Type: application/json" http://localhost:8080/diskspace/TotalDisk
curl -H "Content-Type: application/json" http://localhost:8080/diskspace/UsedDisk
curl -H "Content-Type: application/json" http://localhost:8080/diskspace/FreeDisk
curl -H "Content-Type: application/json" http://localhost:8080/diskspace/Diskusage


