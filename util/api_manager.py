import json
import requests

from template.send_type_enum import SendTypeEnum
from util.template_factory import get_template
from util.fake_data import fake_button_response, fake_text_with_quick_reply_response
from util.constant import *


# 上傳圖片
def upload_file(file):
    url = DOMAIN + '/upload_file'

    param = {
        'file': file
    }

    response = requests.post(url, files={'file': file})
    return response.json().get('result').get('url')


# 送出回答
def send_answer(user_id, answer, answer_type):
    url = DOMAIN + "/sales/post_answer"
    param = {
        'user_id': user_id,
        'content': answer,
        'type': answer_type,
    }

    def on_success(json_obj):
        print("send_answer_on_success")
        result = json_obj['result']
        send_type = SendTypeEnum(result['type'])
        return get_template(send_type, result)

    return _request_post(url, param, on_success)


# 新增使用者
def add_user(profile):
    url = DOMAIN + "/sales/add_user"
    response = requests.post(url, json=profile)
    result = response.json()
    print(result)
    return result['result']


def _request_post(url, param, on_success):
    try:
        result = requests.post(url, json=param)

        # check responseCode == 200
        if result.status_code != requests.codes.ok:
            print("post status code error:", result.status_code)
            return

        print('post response: ', result.text)
        json_obj = json.loads(result.text)

        # do something on success
        return on_success(json_obj)
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
    except requests.exceptions.ConnectionError as err:
        print("Error Connecting:", err)
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


def _request_get(url, on_success):
    try:
        # data = fake_text_with_quick_reply_response
        # json_obj = json.loads(data)

        result = requests.get(url)

        # check responseCode == 200
        if result.status_code != requests.codes.ok:
            print("get state code error:", result.status_code)
            return

        print('get response: ', result.text)
        json_obj = json.loads(result.text)

        # do something on success
        return on_success(json_obj)
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
    except requests.exceptions.ConnectionError as err:
        print("Error Connecting:", err)
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
