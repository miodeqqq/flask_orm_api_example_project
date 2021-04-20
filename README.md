Flask ORM Example Project
=========================

**Current stable version:** v1.0.0

**Release date:** 20.04.2021

### Authors:

* Maciej Januszewski <maciek@mjanuszewski.pl>;

### Pre-requirements:

Create `.flaskenv` file and set proper values for:

```bash
FLASK_APP=app.py # should be the same
FLASK_ENV=development # or production
FLASK_RUN_PORT=8000
```

### Install dependencies:

```bash
pip install poetry or brew install poetry

poetry install -vvv
```

### Running API server:

```bash
make runserver
```

Server: localhost:8000 # will initially generate fake data

### CURL examples:

* List API Users:

```bash
curl http://localhost:8000/users/
```

* Get User by ID:

```bash
curl http://localhost:8000/users/<user_id>/
```

* Create User:

```bash
curl http://localhost:8000/users/ -X POST -H "Content-Type: application/json" -d '{"email":"foo@bar.com", "name":"Lorem ipsum", "is_bot": 1}'
```

* Update User:

```bash
curl http://localhost:8000/users/<user_id>/ -X PATCH -H "Content-Type: application/json" -d '{"email":"foo2@bar.com", "name":"Ipsum Lorem", "is_bot": 0}'
```

* Delete User:

```bash
curl http://localhost:8000/users/<user_id>/ -X DELETE -I
```

### Cleaning tmp files:

```bash
make clean
```
