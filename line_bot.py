from flask import Flask, request, abort
import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,
    LineBotApiError)
from linebot.models import (
    MessageEvent, TextMessage, ImageMessage, LocationMessage, PostbackEvent, FollowEvent, TextSendMessage, JoinEvent
)

from buttons.button_type_enum import ButtonTypeEnum
from util import (
    api_manager, menu_manager,
)
import sys
from io import BytesIO
from util.constant import *


app = Flask(__name__)
line_bot_api = LineBotApi(lineBotKey)
handler = WebhookHandler(webHookKey)


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)

    return 'OK'


@app.route('/')
def hello():
    return 'Hello World!'


@handler.add(FollowEvent)
def handle_follow(event):
    print(event)
    user_id = event.source.user_id

    profile = line_bot_api.get_profile(user_id)
    print(profile)

    try:
        line_bot_api.get_rich_menu_id_of_user(user_id)
    except LineBotApiError:
        print('rich id not found')
        user = api_manager.add_user(profile.as_json_dict())
        token = user['token']
        sales_menu = menu_manager.get_sales_menu(token=token)
        rich_menu_id = line_bot_api.create_rich_menu(rich_menu=sales_menu)
        with open(f'linebot_menu.png', 'rb') as f:
            line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)
        line_bot_api.link_rich_menu_to_user(user_id=user_id, rich_menu_id=rich_menu_id)


@handler.add(JoinEvent)
def handle_join(event):
    print(event)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('text message ', event)

    if event.source.type == 'group':
        message = event.message.text
        url = f'{DOMAIN}/sales/report'
        data = {'user_id': event.source.user_id, 'message': message}
        response = requests.post(url=url, data=data)
        result = response.json()['result']
        if 'message' in result:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(result['message']),
            )

        return

    message = event.message.text

    # if message == "test":
    #     response = api_manager.get_state("aaa")
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         response.get_send_message()
    #     )
    #     return

    # 其他
    answer = {'text': message}
    send_answer_and_send_next_question(event, answer, 'text')


# 送出答案並取得下一個問題
def send_answer_and_send_next_question(event, answer, answer_type, messages=[]):
    user_id = event.source.user_id
    response = api_manager.send_answer(user_id, answer, answer_type)

    line_bot_api.reply_message(
        event.reply_token,
        messages + [response.get_send_message()]
    )


@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    print('location_message: ', event)
    
    if event.source.type == 'group':
        return

    answer = {
        'lat': event.message.latitude,
        'lng': event.message.longitude,
        'address': event.message.address,
    }
    if event.message.title:
        answer['title'] = event.message.title

    send_answer_and_send_next_question(event, answer, 'gps')


@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    print('image_message: ', event)

    if event.source.type == 'group':
        return
    message_id = event.message.id
    message_content = line_bot_api.get_message_content(message_id)

    file = BytesIO(message_content.content)
    response = api_manager.upload_file(file)
    answer = {'url': response}
    send_answer_and_send_next_question(event, answer, 'image')


@handler.add(PostbackEvent)
def handle_post_back(event):
    print('post_back: ', event)

    if event.source.type == 'group':
        return

    data = event.postback.data

    # 時間
    if data == ButtonTypeEnum.TIME.value:
        value = ButtonTypeEnum.TIME.value
        answer = event.postback.params
        time = event.postback.params.get('time', 'null')

        send_answer_and_send_next_question(event, answer, value, [TextSendMessage(text=time)])
        return

    # 日期
    if data == ButtonTypeEnum.DATE.value:
        value = ButtonTypeEnum.DATE.value
        answer = event.postback.params
        date = event.postback.params.get('date', 'null')
        send_answer_and_send_next_question(event, answer, value, [TextSendMessage(text=date)])
        return

    # 日期+時間
    if data == ButtonTypeEnum.DATE_TIME.value:
        value = ButtonTypeEnum.DATE_TIME.value
        answer = event.postback.params
        datetime = event.postback.params.get('datetime', 'null')
        send_answer_and_send_next_question(event, answer, value, [TextSendMessage(text=datetime)])
        return

    # 其他
    answer = {'value': data}
    send_answer_and_send_next_question(event, answer, 'value')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
