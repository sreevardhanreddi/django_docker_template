# django-docker-template

## docker setup for local development

- supports sqlite3 and postgres for db (db can be a docker service)
- supports static and media files serving

## docker setup for production

- nginx for proxying requests to application server, and serving static and media files
- application server (a.k.a django project) is run by **gunicorn**
- application server is connected to a separate db service

```yml
version: "3.7"

services:
  nginx:
    build: ./nginx-proxy
    volumes:
      - static_volume:/app/staticfiles
      - ./media_volume:/app/media
    ports:
      - 81:80
    depends_on:
      - web
    restart: on-failure:5
  web:
    build:
      context: ./web-project
      dockerfile: Dockerfile.prod
    command: gunicorn docker_proj.wsgi:application --workers 2 --bind 0.0.0.0:8000
    volumes:
      - static_volume:/app/staticfiles
      - ./media_volume:/app/media # ./ will mount the dir on the host, if you don't want to store them on host remove ./
    expose:
      - 8000
    env_file:
      - .env.prod
    depends_on:
      - db
  db:
    build:
      context: ./postgres-db
    volumes:
      - ./postgres-db:/var/lib/postgresql
    env_file:
      - .env.prod

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

## Commands

```shell

# for development localhost:8000
docker-compose up --build -d

# for production localhost:81
docker-compose -f docker-compose-prod.yml up --build -d


```

## Architecture

![architecture](./app.png)

## TODO

- [] add support for celery workers
- [] figure out how to add SSL for nginx
