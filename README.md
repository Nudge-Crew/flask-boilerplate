# flask-boilerplate
A Flask Api Boilerplate

# Environment Installation
## Virtual Environment
### Linux and MacOS

The venv folder contains all dependencies which are needed to run this project. To enter the venv virtual environment use:

``` source venv/bin/activate ```

If this is the first time running or if anything in the requirements has changed use:

``` virtualenv venv && source venv/bin/activate && pip install -r requirements.txt ```

after installing a new package use: 

``` pip freeze > requirements.txt ```

to update the requirments folder

### Windows
The venv folder contains all dependencies which are needed to run this project. To enter the venv virtual environment use:

``` source venv/bin/activate ```

If this is the first time running or if anything in the requirements has changed use:

``` virtualenv venv && source venv/Scripts/activate && pip install -r requirements.txt ```

after installing a new package use: 

``` pip freeze > requirements.txt ```

to update the requirments folder

#### Important Note
Make sure to have python37 and python37\Scripts added in your environmental path.
Else command such as ```virtualenv venv``` may not work.

Example environmental variables:

![Environmental Variables](https://i.imgur.com/2u3va11.png "Environmental Variables")

# Project Installation
## Environmental Variables
rename `.flaskenv.example` to `.flaskenv` and change the variable values accordingly.

## Database
Change the database driver to your database. in `.flaskenv` change `DB_DRIVER` to either `LOCAL` for Sqlite or `POSTGRES` for PostgreSQL.

Enter the portgreSQL database details in `.flaskenv`:
```
DB_HOST={database_host}
DB_PORT={database_port}
DB_USER={database_user}
DB_PASSWORD={database_user_password}
DB_NAME={database_name}
```
You do not need to enter these variables when using the Sqlite driver, and you'll only ned to execute the commands below.

execute `flask db upgrade` in your console (e.g in your virtual environment)

## Run Flask
In order to run flask, you just need to execute `flask run`.

# Swagger Documentation
Swagger documentation will be generated on start-up, and can be found at `{url}:{port}/apidocs/`.

The json documentation can be found at `{url}:{port}/apispec_1.json`.

# Development
## Creation of Models
Models can be found under `app.models` directory.
In this directory all models should be placed (e.g `User`) by creating a new python file (e.g `user.py`)

A model should look similar to the one below:

Filename: `app/models/user.py`
```python
from app import db
from .abstract_base_class import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "users"

    first_name = db.Column(db.String(300), primary_key=True)
    last_name = db.Column(db.String(300), primary_key=True)
    email = db.Column(db.String(300), unique=True)
    access_token = db.Column(db.String(300))

    def __init__(self, first_name, last_name, email, access_token):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.access_token = access_token
```

It's recommended to remain the basic structure regarding `db.Model`, `BaseModel` and metaclass `MetaBaseModel`.
In order to export the class, make sure to import it in `__init__.py` in the same directory.

Filename: `app/models/__init__.py`
```python
from .user import User
```

### Important
Be sure to use the [SQLAlachemy Orm](https://docs.sqlalchemy.org/en/13/orm/index.html) documentation, when creating the fields, as these will be used to create the migrations.

### BaseModel and MetaBaseModel
These will be used to avoid duplicate code regarding deserializing objects.
The main functionality is to jsonify the object, as by default SQLAlchemy objects or other custom objects can not be converted to json.

## Creation of Repositories
Repositories can be found under `app.repositories` directory.
In this directory all repositories named corresponding to their `model` in plural with a classname named `{model}_repository`.
A repository should look similar to the one below:

Filename: `app/repositories/users.py`
```python
from app.models import User


class user_repository:
    @staticmethod
    def all():
        return User.query.all()

    @staticmethod
    def get(first_name, last_name, email):
        return User.query.filter_by(first_name=first_name, last_name=last_name, email=email).one()

    def update(self, first_name, last_name, email, access_token):
        user = self.get(first_name, last_name, email)
        user.access_token = access_token

        return user.save()

    @staticmethod
    def create(first_name, last_name, email, access_token):
        user = User(first_name=first_name, last_name=last_name, email=email, access_token=access_token)

        return user.save()
```

Here you can see methods being used from `BaseModel` and `MetaBaseModel` such as `save()`.
In order to export the class, make sure to import it in `__init__.py` in the same directory.

Filename: `app/repositories/__init__.py`
```python
from .users import user_repository
```

## Creation of Resources
Resources can be found under `app.resources` directory.
In this directory all resources named corresponding to their `model` in plural with a classname named `{model}_resource`.
A resource should look similar to the one below:

Filename: `app/resources/users.py`
```python
from flask.json import jsonify

from app.repositories import user_repository


class user_resource:

    @staticmethod
    def all():
        users = user_repository.all()
        results = []

        for u in users:
            results.append(u.json)

        return jsonify({
            "users": results
        })

    @staticmethod
    def get(first_name, last_name, email):
        user = user_repository.get(first_name=first_name, last_name=last_name, email=email)

        return jsonify({
            "user": user.json
        })

    @staticmethod
    def post(first_name, last_name, email, access_token):
        user = user_repository.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            access_token=access_token
        )

        return jsonify({
            "user": user.json
        })

    @staticmethod
    def put(first_name, last_name, email, access_token):
        user = user_repository.update(
            first_name=first_name,
            last_name=last_name,
            email=email,
            access_token=access_token
        )

        return jsonify({
            "user": user.json
        })

```

Here you can see methods being used from `BaseModel` and `MetaBaseModel` such as `user.json`, which converts the User object to `JSON`.
Also make sure to always use `jsonify` in your return statement, to ensure you get a `JSON` response.
In order to export the class, make sure to import it in `__init__.py` in the same directory.

Filename: `app/resources/__init__.py`
```python
from .users import user_resource
```

## Creation of Routes (API Endpoints)
Routes can be found under `app.routes` directory.
In this directory all routes named corresponding to their `model` in plural.
For each resource a new route file should be created, to keep a good overview of all the routes.
A route should look similar to the one below:

Filename: `app/routes/users.py`
```python
from flask import Blueprint

from app.resources import user_resource

PREFIX = "users"

USER_BLUEPRINT = Blueprint(PREFIX, __name__)


@USER_BLUEPRINT.route('/', methods=['GET'])
def all():
    """
    Returning a list of users
    ---
    responses:
        200:
            description: A list of users
            schema:
                $ref: '#/models/User'
    """
    return user_resource.all()
```
Here the value in `PREFIX` will be the endpoint (e.g `{url}/api/users`).
In order to export the class, make sure to import it in `__init__.py` in the same directory.

Filename: `app/routes/__init__.py`
```python
from .users import USER_BLUEPRINT
```

### Swagger Documentation
In the routes you'll also have the possibility to add swagger specifications such as description, responses etc...
More can be found in de [flasgger documentation](https://github.com/flasgger/flasgger).

## Creation of a new migration
The database tables are based of your models.
It's therefore important to use the [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/13/orm/index.html) documentation for reference.

To add a new migration use `flask db migrate`, this will go through the models and create migrations based of those models.
Once completed execute `flask db upgrade`.

### Important
Alembic may not detect everything specified, it's therefore recommended to check the migrations to be correct.
This can be found in `migrations/versions`.

### Downgrading
Made a mistake during development, and want to downgrade a migration back? use `flask db downgrade` to back to the previous migration.


