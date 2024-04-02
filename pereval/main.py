from flask import Flask, request, jsonify
from db import DataHandler

app = Flask(__name__)
data_handler = DataHandler()

@app.route("/submitData", methods=["POST"])
def submit_data():
    try:
        data = request.json
        if data_handler.addPereval(data):
            return jsonify({"status": 200, "message": "Data submitted successfully"}), 200
        else:
            return jsonify({"status": 500, "message": "Error submitting data"}), 500
    except Exception as e:
        return jsonify({"status": 500, "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="127.0.0.1")
