import os
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/TotalDisk')
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/UsedDisk')
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/FreeDisk')
os.system('curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Diskusage')
