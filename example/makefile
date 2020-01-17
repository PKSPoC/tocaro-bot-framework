.PHONY:

pre:
	sudo apt install libpq-dev

buildApiEngine:
	docker-compose build apiengine-svc

collectStatic:
	rm -rf apiengine/collected_static
	rm -rf webserver/collected_static
	env PIPENV_PIPFILE=apiengine/Pipfile pipenv run python apiengine/manage.py collectstatic
	mv apiengine/collected_static webserver/

setupDatabase: up
	docker exec example_database-svc_1 psql -U postgres -c "CREATE ROLE harukabot WITH LOGIN PASSWORD 'harukabot';"
	docker exec example_database-svc_1 psql -U postgres -c "CREATE DATABASE harukabot;"
	docker exec example_apiengine-svc_1 python manage.py makemigrations
	docker exec example_apiengine-svc_1 python manage.py migrate

buildWebServer: collectStatic
	docker-compose build webserver-svc

buildAll: buildApiEngine collectStatic buildWebServer

up:
	docker-compose up -d

