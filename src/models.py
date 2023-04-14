from dataclasses import dataclass
from .db import db


@dataclass
class Address(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    street: str = db.Column(db.String, nullable=False)
    city: str = db.Column(db.String, nullable=False)


@dataclass
class Package(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False, unique=True)
    weight: float = db.Column(db.Float, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
