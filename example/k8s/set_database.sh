#kubectl exec -it database-0 -- psql -U postgres -c "CREATE ROLE harukabot WITH LOGIN PASSWORD 'harukabot';"
#kubectl exec -it database-0 -- psql -U postgres -c "CREATE DATABASE harukabot;"
kubectl -n pvtest exec -it apiengine-bd76db54b-vmvmp -- python manage.py makemigrations
kubectl -n pvtest exec -it apiengine-bd76db54b-vmvmp -- python manage.py migrate
kubectl -n pvtest exec -it apiengine-bd76db54b-vmvmp -- python manage.py createsuperuser

