import requests
from project import local_settings


def send_message(chat_id, token, message):
    url_req = 'https://api.telegram.org/bot' + token + '/sendMessage' + '?chat_id=' + chat_id + '&text=' + message
    requests.get(url_req)
