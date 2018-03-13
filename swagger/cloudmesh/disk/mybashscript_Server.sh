#!/bin/bash
echo "Download the Swagger Codegen 2.3.1 Jar file"
wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

echo "create REST service Server from the below Jar file"

java -jar swagger-codegen-cli-2.3.1.jar generate \
-i diskinfo.yaml \
-l python-flask \
-o server/disks/flaskConnexion \
-D supportPython2=true

echo "Copy default_controller(Code file)"
rm server/disks/flaskConnexion/swagger_server/controllers/default_controller.py
cp default_controller.py server/disks/flaskConnexion/swagger_server/controllers/default_controller.py

echo "Install and Initiate the Virtual REST server"
virtualenv RESTServer
source RESTServer/bin/activate
cd server/disks/flaskConnexion
pip install -r requirements.txt
python setup.py install
python -m swagger_server





