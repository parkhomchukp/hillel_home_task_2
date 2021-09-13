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


@app.route("/avr_data")
def get_avr_data():
    heights = list()
    weights = list()
    with open("hw.csv", encoding="utf-8") as file:
        file_reader = csv.DictReader(file, delimiter=',')
        for row in file_reader:
            heights.append(float(row[' "Height(Inches)"']))
            weights.append(float(row[' "Weight(Pounds)"']))
    avr_height = sum(heights) / len(heights)
    avr_weight = sum(weights) / len(weights)
    return f'Средний рост: {str(avr_height)}</br>Средний вес: {str(avr_weight)}'


app.run(debug=True)
