from flask import Flask, jsonify
# import requests

app = Flask(__name__)
port = 5000

dict = {"New York": 10001, "Los Angeles": 90001,"Chicago": 60601,"Houston": 77001,"Philadelphia": 19019,
    "Phoenix": 85001,"San Antonio": 78201,"San Diego": 92101,"Dallas": 75201,"San Jose": 95101,
    "Austin": 78701,"Jacksonville": 32201,"San Francisco": 94101,"Indianapolis": 46201,"Fort Worth": 76101,
    "Charlotte": 28201,"Detroit": 48201,"El Paso": 79901,"Tampa": 33601,"Sunnyvale": 94085,"Seattle": 98101}

for key in dict:
    dict[key] = str(dict[key])

@app.route("/city_to_zip/<city_name>", methods=["GET"])
def city_to_zip(city_name):
    zipcode = dict[city_name]
    return jsonify(zipcode)

@app.route("/")
def index():
    return "Homepage for Zipcode to Weather"

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=port)


