import os
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/diskspace/TotalDisk')
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/diskspace/UsedDisk')
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/diskspace/FreeDisk')
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/diskspace/Diskusage')
