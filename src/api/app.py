from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load data
prices_df = pd.read_csv("../../data/raw/BrentOilPrices.csv", parse_dates=['Date'])
events_df = pd.read_csv("../../data/raw/key_events.csv", parse_dates=['Date'])
# change_points = pd.read_json("../../data/raw/change_points.json")

@app.route("/api/prices")
def get_prices():
    return jsonify(prices_df.to_dict(orient='records'))

@app.route("/api/events")
def get_events():
    return jsonify(events_df.to_dict(orient='records'))

@app.route("/api/change-points")
def get_change_points():
    return jsonify(change_points.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
