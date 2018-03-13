# assumes swager_codegen environment variable contains
# the path to swagger codegen jarfile

SWAGGER=${swagger_codegen}
SPEC=diskinfo.yaml

all: generate requirements run
	@echo "DONE"

generate:
	$(SWAGGER) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/disks/flaskConnexion \
		-D supportPython2=true
	cp default_controller.py server/disks/flaskConnexion/swagger_server/controllers/  

run:
	cd server/disks/flaskConnexion/ &&\
	python -m swagger_server

requirements:
	pip install -r requirements.txt
	cd server/disks/flaskConnexion; pip install -r requirements.txt

clean:
	rm -rf server/
