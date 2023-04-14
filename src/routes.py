from flask import json, request
from sqlalchemy import text

from .db import db
from .flask import app


def to_json(result_set):
    return [list(result) for result in result_set]


@app.get("/")
def hello():
    return 'Hello world!'


@app.get("/addresses")
def get_addresses():
    result_set = db.session.execute(text("SELECT * FROM address"))
    return to_json(result_set)


@app.post("/addresses")
def create_address():
    body = request.get_json(force=True)
    db.session.execute(
        text("INSERT INTO address (name, street, city) VALUES (:name, :street, :city)"),
        body
    )
    db.session.commit()
    return 'OK'


@app.delete("/addresses/<address_id>")
def delete_address(address_id):
    db.session.execute(
        text("DELETE FROM address WHERE id = :id"),
        {'id': address_id}
    )
    db.session.commit()
    return 'OK'


@app.get("/packages")
def get_packages():
    result_set = db.session.execute(text("SELECT * FROM package"))
    return to_json(result_set)


@app.post("/packages")
def create_package():
    body = request.get_json(force=True)
    db.session.execute(
        text("INSERT INTO package (name, weight, address_id) VALUES (:name, :weight, :addressId)"),
        body
    )
    db.session.commit()
    return 'OK'


@app.delete("/packages/<package_id>")
def delete_package(package_id):
    db.session.execute(
        text("DELETE FROM package WHERE id = :id"),
        {'id': package_id}
    )
    db.session.commit()
    return 'OK'
