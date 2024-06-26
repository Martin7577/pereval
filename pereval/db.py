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

    def addPereval(self, raw_data, images, user_email):
        try:
            # Преобразование данных в JSON
            raw_data = json.dumps(raw_data)
            images = json.dumps(images)
            # SQL запрос для добавления данных о перевале
            query = sql.SQL(
                "INSERT INTO pereval_added (date_added, raw_data, images, status, user_email) VALUES (NOW(), %s, %s, 'new', %s) RETURNING id;"
            )
            self.cursor.execute(query, (raw_data, images, user_email))
            # Получение ID вставленной записи
            pereval_id = self.cursor.fetchone()[0]
            # Подтверждение изменений в базе данных
            self.conn.commit()
            return pereval_id
        except Exception as e:
            # Откат изменений в случае ошибки
            self.conn.rollback()
            print("Error:", e)
            return None

    def addUser(self, email, fam, name, otc, phone):
        try:
            email = json.dumps(email)
            fam = json.dumps(fam)
            name = json.dumps(name)
            otc = json.dumps(otc)
            phone = json.dumps(phone)
            user_query = sql.SQL(
                "INSERT INTO users (email, fam, name, otc, phone) VALUES (%s, %s, %s, %s, %s) RETURNING id;"
            )
            self.cursor.execute(user_query, [email, fam, name, otc, phone])
            # Получение ID вставленной записи
            user_id = self.cursor.fetchone()[0]
            # Подтверждение изменений в базе данных
            self.conn.commit()
            return user_id
        except Exception as e:
            # Откат изменений в случае ошибки
            self.conn.rollback()
            print("Error:", e)
            return None

    def get_data_by_id(self, id):
        try:
            # Выполнение SQL-запроса для получения данных о перевале по его ID
            query = "SELECT * FROM pereval_added WHERE id = %s"
            self.cursor.execute(query, (id,))
            data = self.cursor.fetchone()
            if data:
                # Преобразование данных в словарь и возврат
                return {
                    "id": data[0],
                    "date_added": data[1],
                    "raw_data": data[2],
                    "status": data[3]
                }
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None

    def update_data(self, id, data):
        try:
            # Преобразование данных в JSON
            raw_data = json.dumps(data)
            # SQL-запрос для обновления данных о перевале
            query = "UPDATE pereval_added SET raw_data = %s WHERE id = %s AND status = 'new'"
            self.cursor.execute(query, (raw_data, id))
            # Получение количества обновленных строк
            rows_updated = self.cursor.rowcount
            # Подтверждение изменений в базе данных
            self.conn.commit()
            return rows_updated > 0
        except Exception as e:
            # Откат изменений в случае ошибки
            self.conn.rollback()
            print("Error:", e)
            return False

    def close(self):
        self.cursor.close()
        self.conn.close()


# Пример использования:
if __name__ == "__main__":
    db = DataHandler()
    raw_data = {
        "beauty_title": "per. ",
        "title": "name",
        "other_titles": "name2",
        "connect": "con",
        "coords": {
            "latitude": "55.1234",
            "longitude": "37.5678",
            "height": "1500"
        },
        "level": {
            "winter": "",
            "summer": "1А",
            "autumn": "1А",
            "spring": ""
        }
    }
    images = ({'data': "<1>", 'title': "sed"},
              {'data': "<2>", 'title': "pod"})

    email = {"email": "examplesrg@mail.com"}
    fam = {"fam": "Ivanov"}
    name = {"name": "Ivan"}
    otc = {"otc": "Ivanovich"}
    phone = {"phone": "+71234567890"}

    # Данные о перевале в формате JSON
    pereval_id = db.addPereval(raw_data, images)
    user_id = db.addUser(email['email'], fam['fam'], name['name'], otc['otc'], phone['phone'])
    print("pereval ID:", pereval_id)
    print("user ID:", user_id)
    db.close()
