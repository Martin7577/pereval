 <h1>REST API для управления данными</h1>
    <p>Этот проект представляет собой REST API для управления данными, отправляемыми на сервер. API позволяет отправлять данные о перевалах и изображениях, а также получать информацию о них.</p>

  <h4>Чтобы открыть документацию от Swagger:</h4> 
  <h5>Запустите файл main.py и перейдите по ссылке http://127.0.0.1:5000/swagger/</h5>

   <h2>Методы API</h2>

  <h3>1. Отправка данных на сервер</h3>
  <p><strong>Метод:</strong> POST</p>
  <p><strong>Путь:</strong> /submitData</p>
  <p>Этот метод позволяет отправить данные о перевалах и изображениях на сервер. Данные должны быть отправлены в формате JSON.</p>


  <p><strong>Ответы:</strong></p>
    <ul>
        <li><strong>200:</strong> Данные успешно отправлены на сервер</li>
        <li><strong>500:</strong> Ошибка при отправке данных</li>
    </ul>
  <h3>2. Получение данных о перевале по ID</h3>
<p><strong>Метод:</strong> GET</p>
<p><strong>Путь:</strong> /submitData/{id}</p>
<p>Этот метод позволяет получить данные о перевале по его уникальному идентификатору (ID).</p>
<p><strong>Ответ:</strong> Данные о перевале в формате JSON</p>

<h3>3. Получение данных о перевалах по email пользователя</h3>
<p><strong>Метод:</strong> GET</p>
<p><strong>Путь:</strong> /submitData/{user_email}</p>
<p>Этот метод позволяет получить список данных обо всех объектах, которые пользователь с указанным email отправил на сервер.</p>
<p><strong>Ответ:</strong> Список данных о перевалах в формате JSON</p>

<h3>4. Обновление данных о перевале по ID</h3>
<p><strong>Метод:</strong> PATCH</p>
<p><strong>Путь:</strong> /submitData/{id}</p>
<p>Этот метод позволяет отредактировать существующую запись о перевале по его уникальному идентификатору (ID).</p>
<p><strong>Тело запроса:</strong> Данные о перевале для обновления в формате JSON</p>
<p><strong>Ответы:</strong></p>
<ul>
    <li><strong>200:</strong> Запись успешно обновлена</li>
    <li><strong>404:</strong> Запись не найдена или не может быть обновлена</li>
    <li><strong>500:</strong> Ошибка при обновлении данных</li>
</ul>

Параметры запроса:
user__email: Адрес электронной почты пользователя
Ответы:
200: Данные успешно получены
404: Данные не найдены
