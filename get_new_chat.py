"""Сервер API: https://dev.wapp.im/v3/
Метод  для получения нового чата chat/spare?crm=TEST&domain=test
Метод для работы с чатом instance{ID}/{METHOD}?token={TOKEN}
ID , TOKEN это данные полученные при получении чата
Пример https://dev.wapp.im/v3/instance23/me?token=123DYUUD

При каждом запросе необходимо отправлять заголовок (header)
X-Tasktest-Token: f62cdf1e83bc324ba23aee3b113c6249"""

""" Получить свободный чат и записать данные в базу
2. Инициализировать чат методом status с параметром full=1
3. Дождаться статуса got qr code (метод status)
4. Получить QR код и просканировать его своим Whatsapp
5. Получить статус что вацап подключен и записать имя и телефон
6. Отправить сообщение 
7. Загрузить код в гит и прислать вместе со скрином  отправленного сообщения в переписку. 
"""
import requests
import pickle

url = 'https://dev.wapp.im/v3/'
header = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}

new_chat = 'chat/spare?crm=TEST&domain=test'

response = requests.get(url + new_chat, headers=header)

"""записываем ответ в фаил"""
with open('data_chat.txt', 'wb') as out:
     pickle.dump(response.json(), out)
