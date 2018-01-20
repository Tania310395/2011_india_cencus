import usecase
from flask import Flask, render_template, request
import csv
import json
from operator import itemgetter


app = Flask(__name__)

filename = "india-districts-census-2011.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields =next(csvreader)
    for row in csvreader:
        rows.append(row)
totallist = []

for row in rows:
    dict_file = {}
    for item in row:
        i = row.index(item)
        dict_file[fields[i]] = item
    totallist.append(dict_file)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/usecase/1", methods=["GET", "POST"])
def usecase1():
    if request.method == 'GET':
        return render_template("usecase1.html")
    elif request.method == 'POST':
        literacy_value = request.form['literacy']
        usecase1 = usecase.one(totallist, literacy_value)
        return json.dumps(usecase1)


@app.route("/usecase/2", methods=["GET", "POST"])
def usecase2():
    if request.method == 'GET':
        return render_template("usecase2.html", fields=fields[3:])
    if request.method == 'POST':
        search_index = request.form['value']
        print(search_index)
        usecase2 = usecase.two(totallist,search_index)
        return json.dumps(usecase2)


@app.route("/usecase/3", methods=["GET", "POST"])
def usecase3():
    if request.method == 'GET':
        return render_template("usecase3.html")
    elif request.method == 'POST':
        search_index = request.form['value']
        print(search_index)
        usecase3 = usecase.three(totallist, search_index)
        return json.dumps(usecase3)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
