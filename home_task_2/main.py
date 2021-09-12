from flask import Flask
from faker import Faker
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/pipfile")
def get_pipfile():
    with open(r'..\Pipfile.lock', 'r') as pipfile:
        pipfile_content = pipfile.read()
    return pipfile_content


@app.route("/random_students")
def get_random_students():
    students = list()
    fake = Faker(locale='uk_UA')
    for i in range(30):
        students.append(fake.name())
    return '</br>'.join(students)


app.run(debug=True)
