echo "Install and Create the client server"
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
