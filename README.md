# Corner Case

### Key Tools

### Features

### Starting the application

To run the project on development mode run

```sh
docker-compose build
docker-compose up
```

Or you can also combine them both using single command

```sh
docker-compose up --build
```

To create a superuser run the following command and follow the steps

```sh
docker-compose run --rm django python manage.py createsuperuser
```

*Please bear in mind that the production environment is not completely configured. So running the application in
production mode might fail

Finally you will have an admin panel at
`http://localhost:8000/admin`

## Unit test

To run the unit tests run

```sh
docker-compose run --rm django pytest
```

## How the app works

### Project Generation

This project was generated with django Cookiecutter
