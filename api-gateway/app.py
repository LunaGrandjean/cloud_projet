import os
from flask import Flask, request, jsonify
import base64
import msgpack
import sys
from sqlalchemy import create_engine, text
import requests
import json

# Assuming you've correctly set up the environment variables or defined them here.
DATABASE_URI = os.environ.get("DATABASE_URI", "postgresql://postgres:datasql78$$@database:5432/NumericFarm")
SERVER_URI = os.environ.get("SERVER_URI")

app = Flask(__name__)
engine = create_engine(DATABASE_URI)

# Save the original sys.path
original_sys_path = sys.path.copy()
# Modify sys.path, adjust as necessary for your import
sys.path.append("..")
# Perform import
from data_processing_service.database_connection import add_sensor_data
# Restore the original sys.path
sys.path = original_sys_path    

# Use environment variables for configuration
port = 8080#int(os.environ.get("FLASK_PORT", 5000))

def send_sensor_data(sensor_data, url=SERVER_URI):
    # URL of the endpoint
    url += "add_sensor_data"

    # Ensure the data is in JSON format
    headers = {'Content-Type': 'application/json'}

    # Convert the data dictionary to JSON string
    response = requests.post(url, data=json.dumps(sensor_data), headers=headers)

    # Check response status and act accordingly
    if response.status_code == 200:
        print("Data successfully posted.")
    else:
        print(f"Failed to post data. Status code: {response.status_code}, Response: {response.text}")

@app.route('/collectData', methods=['POST'])
def collect_data():
    try:
        # Get raw data from the POST request body
        encoded_data = request.data  # Use 'request' with lowercase 'r'
        if not encoded_data:
            return jsonify({"status": "error", "message": "Empty data payload."}), 400
        
        # Decode data from base64
        decoded_data = base64.b64decode(encoded_data)
        # Unpack data from msgpack
        sensor_data = msgpack.unpackb(decoded_data, raw=False)

        print(sensor_data)
        send_sensor_data(sensor_data)

#{'sensor_id': '746312', 
#'sensor_version': 'FR-v8', 
#'plant_id': 1, 
#'time': '2024-04-19T19:36:52Z', 
#'measures': {'humidite': '12%', 'temperature': '12°C'}}

        return jsonify({"status": "success", "message": "Data received and stored successfully."}), 201
    except (base64.binascii.Error, msgpack.exceptions.UnpackException):
        return jsonify({"status": "error", "message": "Invalid data format."}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    try:
        send_sensor_data(
                {
                'sensor_id': '746312', 
                'sensor_version': 'FR-v8', 
                'plant_id': 1, 
                'time': '2024-04-19T19:36:52Z', 
                'measures': {'humidite': '12%', 'temperature': '12°C'}
                }
                         )
        return jsonify({"status": "success", "message": "API and database are healthy."}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
