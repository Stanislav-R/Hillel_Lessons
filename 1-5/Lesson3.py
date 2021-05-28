import datetime
import random
import string

from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import fields, validate

from Utils import generate_password, get_current_time

app = Flask(__name__)

from flask import jsonify


# Return validation errors as JSON
@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello???</p>"


@app.route("/now")
def now():
    return str(get_current_time())


# def parse_int(request, param_name, min_limit=0, max_limit=100, default=10):
#     value_int = request.args.get(param_name, str(default))
#
#     if not value_int.isnumeric():
#         raise ValueError("VALUE ERROR: int")
#
#     value_int = int(value_int)
#
#     if not min_limit < value_int < max_limit:
#         raise ValueError(f"RANGE ERROR: [{min_limit}..{max_limit}]")
#
#     return value_int


@app.route("/random")
@use_kwargs({
    "length": fields.Int(
        required=True,
        # missing=100,
        validate=[validate.Range(min=1, max=999)]
    )},
    location="query"
)
def get_random(length):
    return generate_password(length)


app.run(debug=True, port=5001)
