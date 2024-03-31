import json
import psycopg2
from psycopg2 import sql
import os

class DataHandler:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.environ.get('FSTR_DB_NAME', 'pereval'),
            user=os.environ.get('FSTR_DB_LOGIN'),
            password=os.environ.get('FSTR_DB_PASS'),
            host=os.environ.get('FSTR_DB_HOST', 'localhost'),
            port=os.environ.get('FSTR_DB_PORT', '5432')
        )
        self.cursor = self.conn.cursor()

    def addPereval(self, data):
        try:
            # Преобразование данных в JSON
            raw_data = json.dumps(data)
            # SQL запрос для добавления данных о перевале
            query = sql.SQL("INSERT INTO pereval_added (date_added, raw_data, status) VALUES (NOW(), %s, 'new') RETURNING id;")
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
    data = {...}  # Данные о перевале в формате JSON
    inserted_id = db.addPereval(data)
    print("Inserted ID:", inserted_id)
    db.close()