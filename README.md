# cashew-backend-focused-interview

## Setup
1. Create the database with `start_database.sh`
2. Run initial migration

## Development
### Migrations
1. Add / remove / edit a model in `models.py`
2. Create a migration with `flask db migrate -m MIGRATION_NAME_HERE`
3. Apply all migrations with `flask db upgrade`

## Project development
1. Create a virtualenv with `python3 -m venv venv`
2. Activate the virtualenv with `. venv/bin/activate`
3. Install `pip install -r requirements.txt`
4. If you add new dependencies, export requirements with `pip freeze > requirements.txt`