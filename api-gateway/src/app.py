from flask import Flask, request, jsonify
import msgpack
import base64

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    # Récupérer les données encodées en base64
    encoded_data = request.data

    # Décoder de base64
    base64_decoded = base64.b64decode(encoded_data)

    # Décoder de msgpack
    data = msgpack.unpackb(base64_decoded, raw=False)

    # Traiter les données reçues
    print("Received data:", data)

    # Répondre avec succès
    return jsonify({"status": "success", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
