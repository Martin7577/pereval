import requests

# Укажите данные для вашего нового перевала
data = {
    "beauty_title": "пер. ",
    "title": "Название перевала",
    "other_titles": "Дополнительные названия",
    "connect": "Что соединяет",
    "user": {
        "email": "example@mail.com",
        "fam": "Иванов",
        "name": "Иван",
        "otc": "Иванович",
        "phone": "+71234567890"
    },
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
    },
    "images": [
        {"data": "<картинка1>", "title": "Описание 1"},
        {"data": "<картинка2>", "title": "Описание 2"}
    ]
}

# Отправляем POST-запрос на наш эндпоинт submitData
response = requests.post("http://127.0.0.1:8080/submitData", json=data)

# Печатаем ответ
print(response.status_code)
print(response.json())