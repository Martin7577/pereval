import requests

response = requests.get("http://127.0.0.1:5000/submitData/example@mail.com")
# Печатаем ответ
print(response.status_code)
print(response.json())
