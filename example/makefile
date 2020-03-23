.PHONY:

fullAutoSetup: buildAll setupDatabase

buildApiEngine:
	docker-compose build apiengine-svc

collectStatic:
	docker run --rm -t -v $(PWD):/tmp --entrypoint=./collectstatic.sh example_apiengine-svc:latest

buildWebServer: buildApiEngine
	docker-compose build webserver-svc

buildAll: buildApiEngine collectStatic buildWebServer

setupDatabase:
	docker-compose up -d
	docker exec -t example_apiengine-svc_1 python manage.py makemigrations
	docker exec -t example_apiengine-svc_1 python manage.py migrate
	docker exec -it example_apiengine-svc_1 python manage.py createsuperuser
	docker-compose kill

downAndClean:
	docker-compose down
	docker volume rm example_dbdata

tagImage:
	docker tag example_webserver-svc pk-hbr-hj-801.hj.vm/harborpj1/example/webserver
	docker tag example_apiengine-svc pk-hbr-hj-801.hj.vm/harborpj1/example/apiengine

pushToHarbor:
	docker push pk-hbr-hj-801.hj.vm/harborpj1/example/webserver
	docker push pk-hbr-hj-801.hj.vm/harborpj1/example/apiengine

runLocalDockerRegisty:
	sudo mkdir -p /mnt/nfs/docker-registory
	docker run -d --restart=always -p 5000:5000 -v /mnt/nfs/docker-registory:/var/lib/registry registry:latest
