# FLASK PARAMETERS
from flask import Flask, render_template
from webargs import fields, validate
from webargs.flaskparser import use_kwargs
import string
import requests
from hw_utils import generate_password

app = Flask(__name__)


# get_random() -> 127.0.0.1:5000/random?length=42
@app.route("/random")
@use_kwargs({
    "length": fields.Int(
        required=False,
        missing=10,  # default_value
        validate=[validate.Range(min=1, max=100)]
    ),

    "specials": fields.Int(
        required=False,
        missing=0,
        validate=[validate.Range(min=0, max=1)]
    ),
    "digits": fields.Int(
        required=False,
        missing=0,
        validate=[validate.Range(min=0, max=1)]
    )},
    location="query"

)
def get_random(length, specials, digits):
    return generate_password(length, specials, digits)


# def get_bitcoin_rate() -> /bitcoin_rate?currency=UAH
@app.route("/bitcoin_rate")
@use_kwargs({
    "currency": fields.Str(
        required=False,
        missing='USD',
        validate=[validate.ContainsOnly(string.ascii_uppercase)]
    )},
    location="query"
)
def get_bitcoin_rate(currency):
    r = requests.get('https://bitpay.com/api/rates')
    if r.status_code == 200:
        for key in r.json():
            if key['code'] == currency:
                return render_template('bitcoin.html', code=key['rate'], rate=currency, name=key['name'])
    return (f'Код ошибки: {r.status_code}')


app.run(debug=True)
