# cashew-python-backend-focused-interview

## Setup
1. Run setup: `bash scripts/setup.sh`
2. Create virtualenv: `python -m venv .venv`
3. Activate virtualenv: `source .venv/bin/activate`
4. Install: `pip install -r requirements.txt`
5. Migrate database: `flask db upgrade`
6. Run with `flask run --debug`

## Project layout

1. `routes.py` - You'll be working mostly out of this file. Feel free to put all your route declarations here.
2. `models.py` - This contains the models that were used to create the database. You shouldn't need to make edits to this file.
3. `scripts` - This contains some useful scripts, like how to connect to the database with `psql_database.sh` or examples of how to curl the backend in `curl_examples.sh`.

Candidates interviewing can ignore anything below this line

-----

## Project development
1. Create a virtualenv with `python3 -m venv venv`
2. Activate the virtualenv with `. venv/bin/activate`
3. Install `pip install -r requirements.txt`.
- There's an SSL library issue installing `psycopg2` with macOS. One way to solve this is to link to homebrew's openssl:
    ```
    env LDFLAGS="-I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib" pip install -r requirements.txt
    ```
4. If you add new dependencies, export requirements with `pip freeze > requirements.txt`

## Migrations with Flask-Migrate
1. Add / remove / edit a model in `models.py`
2. Create a migration with `flask db migrate -m MIGRATION_NAME`
3. Apply all migrations with `flask db upgrade`

Docs: https://flask-migrate.readthedocs.io/en/latest/#command-reference
