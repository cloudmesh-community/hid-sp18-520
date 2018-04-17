SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=diskinfo.yaml
FLASKDIR=server/disks/flaskConnexion

service: 
	sudo wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate  -i $(YAML)  -l python-flask  -o $(FLASKDIR)  -D supportPython2=true

	#cp -r data $(FLASKDIR)
	rm $(FLASKDIR)/swagger_server/controllers/default_controller.py
	cp -r default_controller.py $(FLASKDIR)/swagger_server/controllers

run: 
	cd $(FLASKDIR) && pip install -r requirements.txt && \
	sudo python setup.py install && python -m swagger_server

test:
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/TotalDisk
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/UsedDisk
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/FreeDisk
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Diskusage
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Mgmtusage
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/Diskiocounter

		            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9


container:
	rm $(FLASKDIR)/Dockerfile
	cp -r Dockerfile $(FLASKDIR)/
	cd $(FLASKDIR); sudo docker build -t arisinha/resourcediskdetail_swagger .; docker run -p 8080:8080 arisinha/resourcediskdetail_swagger;


docker-push:
	docker push arisinha/resourcediskdetail_swagger

docker-start:
	docker pull arisinha/resourcediskdetail_swagger
	docker run -p 8080:8080 arisinha/resourcediskdetail_swagger

docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

