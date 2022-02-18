import pickle
import requests
from time import sleep

with open('data_chat.txt', 'rb') as inp:
    data_chat = pickle.load(inp)

url = 'https://dev.wapp.im/v3/'
header = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}
id = data_chat['id']
token = data_chat['chat_token']

status = f'{url}instance{id}/status?full=1&token={token}'
response = requests.get(status, headers=header)

sleep(120)
with open("qrcode.jpg", 'wb') as out:
    out.write(response.content)
