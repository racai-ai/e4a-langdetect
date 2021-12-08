FROM python:3
LABEL maintainer="radu@racai.ro"
LABEL version="1.0"
LABEL description="The Docker Image containing the language identificator for \
    the Enrich4All project."

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY entrypoint.sh ./
COPY enrichforall.py ./
COPY enrichforall_api.py ./
COPY profiles ./profiles

EXPOSE 5000

CMD ["./entrypoint.sh"]
