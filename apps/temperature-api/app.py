import random
from datetime import datetime, timezone

from flask import Flask, jsonify, request
from pydantic import BaseModel

app = Flask(__name__)

class TemperatureResponse(BaseModel):
    value: float
    unit: str
    timestamp: datetime
    location: str
    status: str
    sensor_id: str
    sensor_type: str
    description: str

@app.route('/temperature', methods=['GET'])
def get_temperature_by_location():
    location = request.args.get('location', type=str)  # Получаем параметр location из строки запроса
    if location is None:
        return jsonify({"error": "Location parameter is required"}), 400
    response = {
        "value": random.uniform(-20.0, 40.0),
        "unit": "Celsius",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "location": str(location),
        "status": "OK",
        "sensor_id": str(id),
        "sensor_type": "DHT22",
        "description": "Random temperature sensor"
    }
    return jsonify(response), 200


@app.route('/temperature/<id>', methods=['GET'])
def get_temperature_by_id(id):
    response = {
        "value": random.uniform(-20.0, 40.0),
        "unit": "Celsius",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "location": str(id),
        "status": "OK",
        "sensor_id": str(id),
        "sensor_type": "DHT22",
        "description": "Random temperature sensor"
    }
    return jsonify(response), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)