# cashew-backend-focused-interview

## Setup
1. Create the database with `start_database.sh`
2. Install dependencies `pip install -r requirements.txt`
3. Run the initial migration `flask db upgrade`
4. Run with `flask run --debug` (`--debug` for hot reloading)

## Development

### Migrations

You have the option of handling migrations by manually running commands on the database or managing migrations with `Flask-Migrate`

### Manual migrations
1. Connect to the database: `bash scripts/psql_database.sh` and run commands through the CLI.
2. In the code, use raw SQL (see `examples.py`).

### Migrations with Flask-Migrate
1. Add / remove / edit a model in `models.py`
2. Create a migration with `flask db migrate -m MIGRATION_NAME`
3. Apply all migrations with `flask db upgrade`

Docs: https://flask-migrate.readthedocs.io/en/latest/#command-reference

## Project development (candidates interviewing can ignore)
1. Create a virtualenv with `python3 -m venv venv`
2. Activate the virtualenv with `. venv/bin/activate`
3. Install `pip install -r requirements.txt`.
- Note that there's an SSL library issue installing `psycopg2` with macOS. One way to solve this is to link to homebrew's openssl:
    ```
    env LDFLAGS="-I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib" pip install psycopg2
    ```
4. If you add new dependencies, export requirements with `pip freeze > requirements.txt`