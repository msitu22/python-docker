from flask import Flask, jsonify
# import requests

app = Flask(__name__)
port = 4001

dict = {"94085": "sunny","60601": "thunderstorm","77001": "rainy","19019": "snowy","85001": "clear",
        "10001": "cloudy","78201": "windy","92101": "mist","75201": "windy","95101": "fog","78701": "rainy",
        "32201": "chilly","94101": "windy","46201": "hot","76101": "cold","28201": "humid","48201": "sunny",
        "79901": "cloudy","33601": "windy","98101": "rainy"}

@app.route("/zip_to_weather/<zipcode>", methods=["GET"])
def zip_to_weather(zipcode):
    weather = dict[zipcode]
    return jsonify(weather)

if __name__ == "__main__":  
    app.run(debug=True, host='127.0.0.1', port=port)
