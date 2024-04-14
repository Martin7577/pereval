import os

import psycopg
from flask import Flask, request, jsonify
from db import DataHandler
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
data_handler = DataHandler()
url = os.getenv("DATABASE_URL")
connection = psycopg.connect(url)

PEREVAL_DATE = "SELECT date_added FROM pereval_added WHERE id = (%s);"
PEREVAL_RAW_DATA = "SELECT raw_data FROM pereval_added WHERE id = (%s);"
PEREVAL_IMAGES = "SELECT images FROM pereval_added WHERE id = (%s);"
PEREVAL_STATUS = "SELECT status FROM pereval_added WHERE id = (%s);"


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


@app.route('/submitData/<int:id>', methods=['GET'])
def get_submitData(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(PEREVAL_DATE, (id,))
            date_added = cursor.fetchone()[0]
            cursor.execute(PEREVAL_RAW_DATA, (id,))
            raw_data = cursor.fetchall()[0]
            cursor.execute(PEREVAL_IMAGES, (id,))
            images = cursor.fetchall()[0]
            cursor.execute(PEREVAL_STATUS, (id,))
            status = cursor.fetchall()[0]
    return {'date_added': date_added, "raw_data": raw_data, "images": images, 'status': status}


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")
