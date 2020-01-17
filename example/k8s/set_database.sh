kubectl exec -it database-77f55d5b4f-5jtst -- psql -U postgres -c "CREATE ROLE harukabot WITH LOGIN PASSWORD 'harukabot';"
kubectl exec -it database-77f55d5b4f-5jtst -- psql -U postgres -c "CREATE DATABASE harukabot;"
kubectl exec -it apiengine-58475f6c46-58n9d --  python manage.py makemigrations
kubectl exec -it apiengine-58475f6c46-58n9d --  python manage.py migrate

