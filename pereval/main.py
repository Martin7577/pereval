from flask import Flask, request, jsonify
from db import DataHandler

app = Flask(__name__)
data_handler = DataHandler()


@app.route("/submitData", methods=["POST"])
def submit_data():
    try:
        raw_data = request.json['raw_data']
        images = request.json['images']
        email = request.json['email']
        fam = request.json['fam']
        name = request.json['name']
        otc = request.json['otc']
        phone = request.json['phone']
        if data_handler.addPereval(raw_data, images) and data_handler.addUser(email, fam, name, otc, phone):
            # if data_handler.addUser(email, fam, name, otc, phone):
            return jsonify({"status": 200, "message": "Data submitted successfully"}), 200
        else:
            return jsonify({"status": 500, "message": "Error submitting data"}), 500
    except Exception as e:
        return jsonify({"status": 500, "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")
