import math

from buttons.camera_button import CameraButton
from buttons.camera_roll_button import CameraRollButton
from buttons.date_button import DateButton
from buttons.date_time_button import DateTimeButton
from buttons.location_button import LocationButton
from buttons.message_button import MessageButton
from buttons.post_back_button import PostBackButton
from buttons.time_button import TimeButton
from buttons.uri_button import UriButton
from template.send_carousel_template import SendCarouselTemplate
from template.send_image_template import SendImageTemplate
from template.send_location_template import SendLocationTemplate
from template.send_type_enum import SendTypeEnum
from template.send_buttons_template import SendButtonsTemplate
from template.send_flex_template import SendFlexTemplate
from template.send_if_template import SendIfTemplate
from template.send_text_template import SendTextTemplate
from buttons.button_type_enum import ButtonTypeEnum
from template.send_video_template import SendVideoTemplate

# 按鈕最多四個
BUTTON_MAX_SIZE = 4
# carousel中的按鈕最多3個
CAROUSEL_BUTTON_MAX_SIZE = 3


def get_template(send_type, json_obj):
    if send_type == SendTypeEnum.TEXT:  # 文字
        return SendTextTemplate(json_obj)
    elif send_type == SendTypeEnum.BUTTON:  # 多個按鈕
        if not check_buttons_is_carousel(json_obj):  # 按鈕小於4個=> 回傳button
            return SendButtonsTemplate(json_obj)
        # 回傳carousel
        return parse_buttons_to_carousel(json_obj)
    elif send_type == SendTypeEnum.IF:  # 是/否兩顆按鈕
        return SendIfTemplate(json_obj)
    elif send_type == SendTypeEnum.FLEX:  # 自訂義
        return SendFlexTemplate(json_obj)
    elif send_type == SendTypeEnum.IMAGE:  # 圖片
        return SendImageTemplate(json_obj)
    elif send_type == SendTypeEnum.VIDEO:  # 影片
        return SendVideoTemplate(json_obj)
    elif send_type == SendTypeEnum.LOCATION:  # 地點
        return SendLocationTemplate(json_obj)
    elif send_type == SendTypeEnum.CAROUSEL:  # carousel
        return SendCarouselTemplate(json_obj)


# 檢查按鈕是否大於4個
def check_buttons_is_carousel(json_obj):
    buttons_json_array = json_obj['buttons']
    buttons_json_array_size = len(buttons_json_array)
    if buttons_json_array_size > BUTTON_MAX_SIZE:
        return True
    return False


# 按鈕轉為carousel
def parse_buttons_to_carousel(json_obj):
    columns = []
    title = json_obj['title']
    text = json_obj.get('text', '-')
    buttons_json_array = json_obj['buttons']
    buttons_json_array_size = len(buttons_json_array)

    x = math.ceil(buttons_json_array_size / CAROUSEL_BUTTON_MAX_SIZE)

    for i in range(0, x):
        buttons = []
        print('i: ', i)
        for j in range(0, CAROUSEL_BUTTON_MAX_SIZE):
            index = i * CAROUSEL_BUTTON_MAX_SIZE + j
            print('j: ', j, ' , ', index)
            if index >= buttons_json_array_size:
                continue

            buttons.append(buttons_json_array[index])

        columns.append({'title': title,
                        'text': text,
                        'buttons': buttons})
        print(columns)

    carousel_obj = {'columns': columns}
    return SendCarouselTemplate(carousel_obj)


def get_buttons(button_json_array):
    buttons = []
    for json_obj in button_json_array:
        send_type = ButtonTypeEnum(json_obj.get('type', ButtonTypeEnum.POST_BACK.value))

        if send_type == ButtonTypeEnum.MESSAGE:
            buttons.append(MessageButton(json_obj))
        elif send_type == ButtonTypeEnum.POST_BACK:
            buttons.append(PostBackButton(json_obj))
        elif send_type == ButtonTypeEnum.DATE:
            buttons.append(DateButton(json_obj))
        elif send_type == ButtonTypeEnum.TIME:
            buttons.append(TimeButton(json_obj))
        elif send_type == ButtonTypeEnum.DATE_TIME:
            buttons.append(DateTimeButton(json_obj))
        elif send_type == ButtonTypeEnum.LOCATION:
            buttons.append(LocationButton(json_obj))
        elif send_type == ButtonTypeEnum.CAMERA:
            buttons.append(CameraButton(json_obj))
        elif send_type == ButtonTypeEnum.CAMERA_ROLL:
            buttons.append(CameraRollButton(json_obj))
        elif send_type == ButtonTypeEnum.URI:
            buttons.append(UriButton(json_obj))

    return buttons
