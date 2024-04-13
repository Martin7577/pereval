import json
import psycopg
from psycopg import sql
import os
from dotenv import load_dotenv

load_dotenv()


class DataHandler:
    def __init__(self):
        self.conn = psycopg.connect(
            dbname=os.getenv('FSTR_DB_NAME'),
            user=os.getenv('FSTR_DB_LOGIN'),
            password=os.getenv('FSTR_DB_PASS'),
            host=os.getenv('FSTR_DB_HOST'),
            port=os.getenv('FSTR_DB_PORT')
        )
        self.cursor = self.conn.cursor()

    def addPereval(self, data):
        try:
            # Преобразование данных в JSON
            raw_data = json.dumps(data)
            # SQL запрос для добавления данных о перевале
            query = sql.SQL(
                "INSERT INTO pereval_added (date_added, raw_data, status) VALUES (NOW(), %s, 'new') RETURNING id;")
            self.cursor.execute(query, [raw_data])
            # Получение ID вставленной записи
            inserted_id = self.cursor.fetchone()[0]
            # Подтверждение изменений в базе данных
            self.conn.commit()
            return inserted_id
        except Exception as e:
            # Откат изменений в случае ошибки
            self.conn.rollback()
            print("Error:", e)
            return None

    def close(self):
        self.cursor.close()
        self.conn.close()


# Пример использования:
if __name__ == "__main__":
    db = DataHandler()
    data = {"beauty_title": "пер. ",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "",
            "add_time": "2021-09-22 13:18:13",
            "user": {
                "email": "user@email.tld",
                "phone": "79031234567",
                "fam": "Пупкин",
                "name": "Василий",
                "otc": "Иванович"
            },
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"
            },
            "level": {
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": ""
            },
            "images": [{'data': "<картинка1>", 'title': "Седловина"},
                       {'data': "<картинка>", 'title': "Подъём"}]}  # Данные о перевале в формате JSON
    inserted_id = db.addPereval(data)
    print("Inserted ID:", inserted_id)
    db.close()
