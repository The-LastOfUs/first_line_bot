import requests
import time
from linebot import (
    LineBotApi
)

from linebot.models import (
    TextSendMessage
)
import os

# release key
lineBotKey = 'O0uYQ4ZwnqhAKcS9fufK/shJXVXxWEOWTj4Thxo78Wu3a' \
             '+xJJZxDqnS5WoCXrsV3Ix4XMsgxW9rdsn52SpKM6pl8VycJ2uZ1d5zfHZnQraEnsfdKwz9t4/O' \
             '+npMh7dRvmydVQ1wLhJxhjQLrb0O5MgdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(lineBotKey)

URL = "https://app.angelsctek.com:8080/"

LINE_BOT_URL = "https://app.angelsctek.com:8000/"

GROUP_ID = "C8bfa988418a2b8d33d482d3e51066ed0"

SLEEP_FIVE_MIN = 300


def send_error_message_and_reboot_server(message, screen_name):
    line_bot_api.push_message(GROUP_ID, TextSendMessage(message))

    os.popen(f'sh ~/reboot_server.sh {screen_name}')


def check(url, error_message, screen_name):
    try:
        print(f'start testing {screen_name}, {time.ctime()}')
        requests.get(url)
        print(f'{screen_name} is OK,  {time.ctime()}')
    except requests.exceptions.HTTPError as err:
        send_error_message_and_reboot_server(error_message, screen_name)
        print("Http Error:", err)
    except requests.exceptions.ConnectionError as err:
        send_error_message_and_reboot_server(error_message, screen_name)
        print("Error Connecting:", err)
    except requests.exceptions.Timeout as err:
        send_error_message_and_reboot_server(error_message, screen_name)
        print("Timeout Error:", err)
    except requests.exceptions.RequestException as err:
        send_error_message_and_reboot_server(error_message, screen_name)
        print("OOps: Something Else", err)


if __name__ == '__main__':
    check(URL, 'Server出錯了!!!!!!!! 不過別擔心，我搞定了💪💪💪', 'app')
    check(LINE_BOT_URL, 'LineBot出錯了!!!!!!!! 不過別擔心，我搞定了💪💪💪', 'sales')
