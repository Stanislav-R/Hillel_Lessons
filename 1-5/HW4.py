# GIT + SQLITE
from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields
from db import execute_query
from html_formatters import format_records

app = Flask(__name__)


# def get_unique_names() -> /unique_names
@app.route("/unique_names")
def get_unique_names():
    query = f"select * from customers group by FirstName"
    records = execute_query(query)
    print(records)
    return format_records(records)


# def get_tracks_count() -> /tracks_count
@app.route("/tracks_count")
def get_tracks_count():
    query = f"select * from tracks"
    records = execute_query(query)
    print(records)
    return f'Количество записей в таблице = {len(records)}'


# def get_customers() -> /customers?city=Oslo&country=Norway
@app.route("/customers")
@use_kwargs({
    "country": fields.String(
        required=False,
    ),
    "city": fields.String(
        required=False,
    )},
    location="query"
)
def get_customers(country=None, city=None):
    if country and city:
        query = f"select * from customers where Country = '{country}' AND City = '{city}'"
    elif country or city:
        query = f"select * from customers where Country = '{country}' OR City = '{city}'"
    else:
        query = f"select * from customers"
    records = execute_query(query)
    print(records)
    return format_records(records)


# def get_sales() -> /sales
@app.route("/sales")
def get_sales():
    query = f"select * from invoice_items"
    records = execute_query(query)
    total = 0
    for elem in records:
        total += (elem[3] * elem[4])
    print(total)
    return f'Сумма продаж компании = {total}'


app.run(debug=True, port=5001)
