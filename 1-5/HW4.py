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


# def get_genre_durations() -> /genres_durations
@app.route("/genres_durations")
def genres_durations():
    # query = f"select genres.*, sum(tracks.Milliseconds)/60000 from genres join tracks on genres.GenreId = " \
    #         f"tracks.GenreId group by genres.Name"
    query = f"select i.Name, sum(ii.Milliseconds)/(1000*60) as duration from genres as i join tracks " \
            f"as ii on i.GenreId == ii.GenreId group by i.Name order by duration desc"
    records = execute_query(query)
    print(records)
    return format_records(records)


# def get_greatest_hits() -> /greatest_hits?count=20
@app.route("/greatest_hits")
@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=-1
    )},
    location="query"
)
def greatest_hits(count):
    # query = f"select genres.*, sum(tracks.Milliseconds)/60000 from genres join tracks on genres.GenreId = " \
    #         f"tracks.GenreId group by genres.Name"
    query = f"select tracks.Name, (count(*) * invoice_items.UnitPrice * invoice_items.Quantity) as profit " \
            f"from tracks join invoice_items on tracks.TrackId = invoice_items.TrackId group by tracks.Name " \
            f"order by profit desc limit {count}"
    records = execute_query(query)
    print(records)
    return format_records(records)


app.run(debug=True, port=5001)
