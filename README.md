# Asynchronous Tasks with Django and Celery

Example of how to handle background processes with Django, Celery, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-and-celery/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to http://localhost:1337 to view the app or to http://localhost:5555 to view the Flower dashboard.

Trigger a new task:

```sh
$ curl -F type=0 http://localhost:1337/tasks/
```

Check the status:

```sh
$ curl http://localhost:1337/tasks/<TASK_ID>/
```
