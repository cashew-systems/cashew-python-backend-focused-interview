from flask import request
from .app import app

@app.get("/example")
def get_example():
    foo = request.args.get('foo')
    print('foo:', foo)
    return "GET example"


@app.post("/example")
def post_example():
    # Parse as JSON even if Content-Type is not set
    json = request.get_json(force=True)
    print(json)
    print('foo:', json.get('foo'))
    return "POST example"