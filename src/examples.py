from flask import jsonify, request
from sqlalchemy import text
from .db import db
from .flask import app
from .models import Example


@app.post("/sql-example")
def sql_example():
    db.session.execute(text("insert into example (name) values ('john')"))
    result_set = db.session.execute(text("select * from example where name = 'john'"))
    for result in result_set:
        print("result:", result)
    db.session.commit()
    return ""


# This uses a Flask-SQLAlchemy integration. Documentation:
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/
@app.post("/orm-example")
def orm_example():
    # Add one
    example = Example(name="foo")
    db.session.add(example)
    db.session.flush()  # Pushes the change to the current transaction, but doesn't commit to database

    # Add many
    examples = [Example(name="bar"), Example(name="baz")]
    db.session.add_all(examples)
    db.session.flush()

    # Filter by id, take first result or None
    result = db.session.execute(
        db.select(Example).filter_by(id=example.id)
    ).scalar_one_or_none()
    print("filter by id:", result)

    # Filter by name like, take all results
    result_set = db.session.execute(
        db.select(Example).filter(Example.name.like("baz"))
    ).scalars()
    print("filter by name:", [e for e in result_set])

    result.name = "updated"
    db.session.flush()
    updated_result = db.session.execute(
        db.select(Example).filter_by(id=example.id)
    ).scalar_one_or_none()
    print("updated result:", updated_result)

    db.session.delete(example)
    db.session.commit()  # Commits the changes to the database
    return jsonify(example), 200
