echo "Install and Create the client server"
# Below code need to execute from swagger folder (same folder as server)
java -jar swagger-codegen-cli-2.3.1.jar generate \
-i diskinfo.yaml \
-l python \
-o client/disks \
-D supportPython2=true

echo "Install and Initiate the Virtual REST Client"
virtualenv RESTClient
source RESTClient/bin/activate
cd client/disks
pip install -r requirements.txt
python setup.py install

cd ../ClientBashFilesandScripts
# Execute the shell and python scripts to verify client (placed under ClientBashFilesandScripts folder)
