FROM python:3.6

# ARG http_proxy
# ARG https_proxy

RUN pip install pipenv
WORKDIR /harukabot
COPY . .
RUN set -ex && pipenv install --deploy --system

RUN touch /tmp/uwsgi.pid
ENTRYPOINT ["uwsgi","--ini", "uwsgi.ini"]
