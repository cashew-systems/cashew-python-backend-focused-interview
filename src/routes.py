from flask import request
from .examples import *
from .flask import app


@app.get("/example")
def get_example():
    foo = request.args.get("foo")
    print("args:", request.args)
    return foo, 200


@app.post("/example")
def post_example():
    # Parse as JSON even if Content-Type is not set
    json = request.get_json(force=True)
    print("json:", json)
    return json.get("foo"), 200

