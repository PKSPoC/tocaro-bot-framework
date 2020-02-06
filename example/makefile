.PHONY:

pre:
	sudo apt install libpq-dev

buildApiEngine:
	docker-compose build apiengine-svc

collectStatic:
	docker run --rm -t -v $PWD:/tmp --entrypoint=./collectstatic.sh example_apiengine-svc:latest

setupDatabase: up
	docker exec example_database-svc_1 psql -U postgres -c "CREATE ROLE harukabot WITH LOGIN PASSWORD 'harukabot';"
	docker exec example_database-svc_1 psql -U postgres -c "CREATE DATABASE harukabot;"
	docker exec example_apiengine-svc_1 python manage.py makemigrations
	docker exec example_apiengine-svc_1 python manage.py migrate

buildWebServer: buildApiEngine 
	docker-compose build webserver-svc

buildAll: buildApiEngine collectStatic buildWebServer

up:
	docker-compose up -d

tagLocalImage:
	docker tag example_webserver-svc localhost:5000/harukabot/webserver
	docker tag example_apiengine-svc localhost:5000/harukabot/apiengine

pushToLocalDockerResistry:
	docker push localhost:5000/harukabot/webserver
	docker push localhost:5000/harukabot/apiengine

runLocalDockerRegisty:
	sudo mkdir -p /mnt/nfs/docker-registory
	docker run -d --restart=always -p 5000:5000 -v /mnt/nfs/docker-registory:/var/lib/registry registry:latest

