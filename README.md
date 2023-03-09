# cashew-backend-focused-interview

## Setup
1. Run setup: `bash scripts/setup.sh`
1. Create a virtualenv: `python -m venv venv`
1. Activate the virtualenv: `. venv/bin/activate`
1. Install dependencies `pip install -r requirements.txt`
1. Run the initial migration `flask db upgrade`
1. Run with `flask run --debug` (`--debug` for hot reloading)

## Project layout

1. `routes.py` - You'll be working mostly out of this file. Feel free to put all your route declarations here.
1. `examples.py` - This contains examples for accessing the database using either the SQLAlchemy ORM or with raw SQL. Feel free to use whatever you prefer.
    - Documentation:
        - https://docs.sqlalchemy.org/en/20/orm/quickstart.html#create-objects-and-persist
        - https://docs.sqlalchemy.org/en/20/orm/quickstart.html#simple-select
        - https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#query-the-data
        - https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
1. `models.py` - This contains the table declarations that were used to create the database. You shouldn't need to make edits to this file, but feel free to if you think its useful. If you do, you'll need to create and apply migrations using `Flask-Migrate`. See the `Migrations` section below.
1. `scripts` - This contains some useful scripts, like how to connect to the database with the `psql` CLI with `psql_database.sh` or how to curl the backend with `curl_examples.sh`.

## Migrations with Flask-Migrate
1. Add / remove / edit a model in `models.py`
1. Create a migration with `flask db migrate -m MIGRATION_NAME`
1. Apply all migrations with `flask db upgrade`

Docs: https://flask-migrate.readthedocs.io/en/latest/#command-reference

------

Candidates interviewing can ignore anything below this line

------

## Project development
1. Create a virtualenv with `python3 -m venv venv`
1. Activate the virtualenv with `. venv/bin/activate`
1. Install `pip install -r requirements.txt`.
- Note that there's an SSL library issue installing `psycopg2` with macOS. One way to solve this is to link to homebrew's openssl:
    ```
    env LDFLAGS="-I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib" pip install psycopg2
    ```
1. If you add new dependencies, export requirements with `pip freeze > requirements.txt`