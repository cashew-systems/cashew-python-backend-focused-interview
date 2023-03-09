from dataclasses import dataclass
from .db import db

# Example model using dataclasses. The type hint (e.g. "id: int") makes it
# visible to the dataclass decorator
@dataclass
class Example(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False)