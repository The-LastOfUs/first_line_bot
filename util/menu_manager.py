from linebot.models import RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, URIAction, MessageAction
from linebot import (
    LineBotApi, WebhookHandler
)
from util.constant import *


def get_sales_menu(token):
    sales_menu = RichMenu(
        size=RichMenuSize(width=1200, height=810),
        selected=False,
        name='我的測試選單',
        chat_bar_text='大天使選單',
        areas=[
            RichMenuArea(
                bounds=RichMenuBounds(x=0, y=0, width=400, height=405),
                action=MessageAction(label='visit', text='*--打卡--*'),
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=400, y=0, width=400, height=405),
                action=URIAction(label='create_mou', uri=f'{SALES_WEB_URL}/create?token={token}'),
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=800, y=0, width=400, height=405),
                action=URIAction(label='map', uri=f'{SALES_WEB_URL}/map'),
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=0, y=405, width=400, height=405),
                action=MessageAction(label='clear', text='*--清除表單--*'),
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=400, y=405, width=400, height=405),
                action=URIAction(label='mymou', uri=f'{SALES_WEB_URL}/mymou?token={token}'),
            ),
            RichMenuArea(
                bounds=RichMenuBounds(x=400, y=405, width=400, height=405),
                action=MessageAction(label='report', text=f'*--意見回報--*'),
            ),
        ]
    )
    return sales_menu


if __name__ == '__main__':
    lineBotKey = 'AijUGmFB6Z7cxg0FHBO08dOtJVvJ/iSbeCChYAk90u6XiWYFUxmlIrFeXq1kgSrmm9mnRQAQ6ZRYnWsY5B1Z9jBBhpxSUtYMk' \
                 'dfg8l5KKOa+K8QRYn1M8qQYHK87JzAncFmHN5+SUqcbZU2WhTkgUwdB04t89/1O/w1cDnyilFU='
    line_bot_api = LineBotApi(lineBotKey)
    menu_list = line_bot_api.get_rich_menu_list()
    print(menu_list)

    # create_rich_menu(line_bot_api, '0fb88ceb70b84e6f8aada82b16c19b77','Uc7494b2c9528dd96c1490bff33b5d103')
    # menu = line_bot_api.get_rich_menu_id_of_user('Ua2241af7e5bc2fee626da62b11827c42')
    for menu in menu_list:
        print(menu)
        line_bot_api.delete_rich_menu(rich_menu_id=menu.rich_menu_id)
