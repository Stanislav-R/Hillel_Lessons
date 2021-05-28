from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from db import execute_query
from html_formatters import format_records

app = Flask(__name__)


@app.route("/customers")
@use_kwargs({
    "first_name": fields.Str(
        required=False
    ),
    "last_name": fields.String(
        required=False
    )},
    location="query"
)
def get_customers(first_name=None, last_name=None):
    query = f"select * from customers"

    where_filter = {}
    if first_name:
        where_filter['FirstName'] = first_name
    if last_name:
        where_filter['LastName'] = last_name

    if where_filter:
        query += ' WHERE ' + ' OR '.join(f'{k}=\'{v}\'' for k, v in where_filter.items())

    records = execute_query(query)
    print(records)
    return format_records(records)


app.run(debug=True, port=5001)
