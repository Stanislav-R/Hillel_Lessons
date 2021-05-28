# FLASK
# -*- coding: UTF-8 -*-
from flask import Flask, json
import pandas as pd
from faker import Faker

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# get_avr_data() -> 127.0.0.1:5000/avr_data
@app.route("/avr_data")
def avr_data():
    return '''
        <html><body>
        <h1>Hello! <a href="/get_avr_data">Here is your request.</a></h1>
        </body></html>
        '''


@app.route("/get_avr_data")
def get_avr_data():
    data = pd.read_csv("C:/Python/Hillel_Lessons/1-5/hw.csv", header=None, names=["Index", "Height", "Weight"])
    data["Height"] = pd.to_numeric(data["Height"], errors='coerce')
    data["Weight"] = pd.to_numeric(data["Weight"], errors='coerce')
    result = f'''Средний рост = {data["Height"].mean()}  Средний вес = {data["Weight"].mean()}'''

    return result


# get_requirements() -> 127.0.0.1:5000/requirements
@app.route("/requirements")
def get_requirements():
    with open("C:/Python/Hillel_Lessons/1-5/requirements.txt") as f:
        file_content = f.read()

    return file_content


# get_random_students() -> 127.0.0.1:5000/random_students
@app.route("/random_students")
def get_random_students(n=10):
    names = {}
    fake = Faker(['uk_UA'])
    # return ''.join(fake.name() + ', ' for i in range(5))
    names = {key: fake.name() for key in range(n)}
    return json.dumps(names, ensure_ascii=False)


app.run(debug=True)
