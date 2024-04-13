import requests

# Укажите данные для вашего нового перевала
data = {
    "raw_data": {"beauty_title": "per. ",
                 "title": "name",
                 "other_titles": "name2",
                 "connect": "con",
                 "coords": {
                     "latitude": "55.1234",
                     "longitude": "37.5678",
                     "height": "1500"},
                 "level": {
                     "winter": "",
                     "summer": "1А",
                     "autumn": "1А",
                     "spring": ""}
                 },
    "images": [{"id": 1, "title": "Седловина"},
               {"id": 2, "title": "Подъем"}
               ],
    'email': "example@mail.com",
    'fam': "Ivanov",
    "name": "Ivan",
    "otc": "Ivanovich",
    "phone": "+71234567890"
}

# Отправляем POST-запрос на наш эндпоинт submitData
response = requests.post("http://127.0.0.1:5000/submitData", json=data)
# Печатаем ответ
print(response.status_code)
print(response.json())
