FROM python:3.6

RUN pip install pipenv
WORKDIR /apiengine
COPY . .
RUN set -ex && pipenv install --deploy --system

RUN touch /tmp/uwsgi.pid
ENTRYPOINT ["uwsgi","--ini", "uwsgi.ini"]
