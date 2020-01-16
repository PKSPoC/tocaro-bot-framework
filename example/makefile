.PHONY:


buildApiEngine:
	docker-compose build apiengine

collectStatic:
	rm -rf apiengine/collected_static
	env PIPENV_PIPFILE=apiengine/Pipfile pipenv run python apiengine/manage.py collectstatic
	mv apiengine/collected_static webserver/

setupDatabase:
	docker exec example_database_1 psql -U postgres -c "CREATE ROLE harukabot WITH LOGIN PASSWORD 'harukabot';"
	docker exec example_database_1 psql -U postgres -c "CREATE DATABASE harukabot;"
	docker exec example_api-engine_1 python manage.py makemigrations
	docker exec example_api-engine_1 python manage.py migrate

buildWebServer: collectstatic
	docker-compose build front-web

