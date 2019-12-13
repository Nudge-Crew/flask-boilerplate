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
`We currently make use of a sqlite database for testing`

Enter the portgreSQL database details in `.flaskenv`:
```
DB_HOST={database_host}
DB_PORT={database_port}
DB_USER={database_user}
DB_PASSWORD={database_user_password}
DB_NAME={database_name}
```

execute `flask db migrate` in your console (e.g in your virtual environment)