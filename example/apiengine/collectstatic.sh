#!/bin/sh

# local webserver's directory will be mounted to /tmp in apiengine container.

python manage.py collectstatic
rm -rf /tmp/webserver/collected_static
mv ./collected_static /tmp/webserver

