import requests

# Определяем JSON-данные для отправки в запросе PATCH
raw_data = {"beauty_title": "p ",
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
            }

# Отправляем PATCH-запрос на ваш эндпоинт
response = requests.patch("http://127.0.0.1:5000/submitData/12", json=raw_data)

# Печатаем ответ
print("Status code:", response.status_code)
print("Response data:", response.json())
