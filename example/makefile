.PHONY: const hardclean apps/static


buildFrontWeb:
	docker-compose build front-web

buildApiEngine:
	docker-compose build api-engine

setupDatabase:
	docker exec example_database_1 psql -U postgres -c "CREATE ROLE harukabot WITH LOGIN PASSWORD 'harukabot';"
	docker exec example_database_1 psql -U postgres -c "CREATE DATABASE harukabot;"
	docker exec example_api-engine_1 python manage.py makemigrations
	docker exec example_api-engine_1 python manage.py migrate



const: dbstart web/static log
	docker-compose build
	docker exec example_db_1 psql -U postgres -c "CREATE ROLE haukabot WITH LOGIN PASSWORD 'haukabot';"
	docker exec dbconst psql -U postgres -c "CREATE DATABASE harukabot;"
	docker kill dbconst
	docker-compose up -d
	docker exec -i tdsemi_apps_1 ./manage.py migrate

web/static: apps/static
	cp -r ./apps/static $@

log:
	mkdir $@
	./fluentd.sh

dbdata:
	mkdir $@
	chmod 774 ./dbdata

apps/requirements.txt:
	cp -f ./requirements.txt $@

apps/static: apps/requirements.txt
	mkdir -p $@
	docker-compose build apps
	docker run -v $(PWD)/apps:/apps --entrypoint=/apps/manage.py --rm tdsemi_apps:latest collectstatic --noinput

dbstart: dbdata
	docker run -d -v $(PWD)/dbdata:/var/lib/postgresql/data/ --name dbconst --rm postgres:9.5

hardclean:
	rm -rf apps/static
	rm -rf web/static
	rm -rf log
	rm -rf dbdata
	docker kill fluentd
	docker kill dbconst

