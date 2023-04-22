# Recipebox_API
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

This is a backend API for a recipe box application, built using FastAPI and SQLAlchemy.

## Installation


Clone the repository: git clone https://github.com/MarinaZhdanovich/recipebox_API.git

Set up the environment using the command: python -m venv env and .env\Scripts\activate

Connect to PostgreSql through DBeaver and create a database named 'recipes'

Define the settings for connecting to the database (port, database name, username, and password) in the .env file

Install the dependencies using Poetry: poetry install

Install PostgreSQL and all the necessary libraries if they are not already installed on your computer. Install psycopg2 using the following command:  pip install psycopg2 

If your interpreter version is different, modify it in pyproject.toml

Install the libraries using the command: poetry add Alembic, Pydentic, SQLAlchemy

Create a database migration using Alembic by running the command: alembic revision --autogenerate -m 'create db'

Apply the migration to the database by running the command:alembic upgrade head

Apply the script to populate the role table in the database: insert into role(id, name, create_at, update_at) values(1, 'admin', '2023-04-11', '2023-04-11'),(2, 'user', '2023-04-11','2023-04-11').
Fixtures (sample data) are specified in the code to initialize the tables. Run them in the following order using python .\run_db.py: user, recipe, ingredient, recipe-ingredient

Start the server by running the following command: uvicorn main:app --reload

## Project Structure

backend: The backend directory contains the FastAPI application, along with the database models, schemas, CRUD operations, and API endpoints.

logs: The logs directory is where logs generated by the application are stored.

poetry.lock: The Poetry lock file containing the project dependencies and their versions.

pyproject.toml: The Poetry project configuration file.

README.md: The README file containing instructions for installing and running the project.
```
 recipebox_API
├─ backend
│  ├─ alembic
│  │  ├─ env.py
│  │  ├─ README
│  │  ├─ script.py.mako
│  │  └─ versions
│  │     └─ f71af3d8e713_create_db.py
│  ├─ alembic.ini
│  ├─ app
│  │  ├─ api
│  │  │  ├─ endpoints
│  │  │  ├─ api.py
│  │  │  └─ __init__.py
│  │  ├─ core
│  │  │  ├─ config.py
│  │  │  └─ __init__.py
│  │  ├─ crud
│  │  │  ├─ ingredient.py
│  │  │  ├─ recipe.py
│  │  │  ├─ recipe_ingredient.py
│  │  │  ├─ user.py
│  │  │  └─ __init__.py
│  │  ├─ db
│  │  │  ├─ base.py
│  │  │  ├─ base_class.py
│  │  │  ├─ db_setup.py
│  │  │  ├─ init_db.py
│  │  │  ├─ init_recipe_ingredient.py
│  │  │  ├─ session.py
│  │  │  └─ __init__.py
│  │  ├─ models
│  │  │  ├─ ingredient.py
│  │  │  ├─ mixin.py
│  │  │  ├─ recipe.py
│  │  │  ├─ recipe_ingredient.py
│  │  │  ├─ role.py
│  │  │  ├─ user.py
│  │  │  └─ __init__.py
│  │  ├─ schemas
│  │  │  ├─ ingredient.py
│  │  │  ├─ recipe.py
│  │  │  ├─ recipe_ingredient.py
│  │  │  ├─ role.py
│  │  │  ├─ user.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ run_db.py
│  ├─ main.py
│  └─ __init__.py
├─ logs  
├─ poetry.lock
├─ pyproject.toml
└─ README.md
```

## Backend

alembic: The alembic directory contains the database migration scripts generated by Alembic.

alembic.ini: The Alembic configuration file.

app: The app directory contains the main FastAPI application code.

run_db.py: A script to initialize the database and create tables.

main.py: The main entry point for the FastAPI application.

__init__.py: An empty file to make the backend directory a Python package. 

### app directory

api: The api directory contains the API endpoints for the application.

core: The core directory contains the core configuration code for the application.

crud: The crud directory contains the CRUD (Create, Read, Update, Delete) operations for the database models.

db: The db directory contains the database session setup and initialization code.

models: The models directory contains the database models.

schemas: The schemas directory contains the Pydantic schema definitions for the database models.

__init__.py: An empty file to make the app directory a Python package. 

### api directory

endpoints: The endpoints directory contains the implementation code for the API endpoints.

api.py: The main API router that ties all the endpoints together.

__init__.py: An empty file to make the api directory a Python package. 


### core directory

config.py: Configuration settings for the application.

__init__.py: An empty file to make the core directory a Python package.


### crud directory

ingredient.py: CRUD operations for the Ingredient model.

recipe.py: CRUD operations for the Recipe model.

recipe_ingredient.py: CRUD operations for the RecipeIngredient model.

user.py: CRUD operations for the User model.

__init__.py: An empty file to make the crud directory a Python package. 


### db directory
base.py: Base class for SQLAlchemy models.

base_class.py: Base class for custom SQLAlchemy models.