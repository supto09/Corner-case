# Corner Case

### Key Tools

| Tool | version |
| ------ | ------ |
| python | 3.9 &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
| django | 3.1.11 |
| PostgreSQL | 13.2 |

### Features

### Requirements

1. Docker
2. Docker-compose

### Starting the application

To run the project on development mode run. Make sure your 8000 & 8001 ports are free

```sh
docker-compose build
docker-compose up
```

Or you can also combine them both using single command

```sh
docker-compose up --build
```

Finally, you will have an dashboard at
`http://localhost:8000`

and an admin panel at
`http://localhost:8000/admin`

Api Documentation will be available at
`http://localhost:8000/api/apidoc` and `http://localhost:8000/api/apidoc/swagger`

To create a superuser run the following command and follow the steps

```sh
docker-compose run --rm django python manage.py createsuperuser
```

## Unit test

To run the unit tests run

```sh
docker-compose run --rm django pytest
```

### Project Generation

This project was generated with django Cookiecutter

## Winner Restaurant selection Process

The restaurant with highest voted menu is selected as the winner restaurant. In case there are two menu with same vote
count then menu created earlier is prioritized
