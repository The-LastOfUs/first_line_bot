from abc import abstractmethod

# from util import template_factory
from linebot.models import QuickReplyButton, QuickReply

from buttons.button_type_enum import ButtonTypeEnum
from buttons.camera_button import CameraButton
from buttons.camera_roll_button import CameraRollButton
from buttons.date_button import DateButton
from buttons.date_time_button import DateTimeButton
from buttons.location_button import LocationButton
from buttons.message_button import MessageButton
from buttons.post_back_button import PostBackButton
from buttons.time_button import TimeButton
from buttons.uri_button import UriButton


class TemplateBase:
    def __init__(self, json_data):
        self.quick_reply = None
        quick_buttons_json_array = json_data.get('quick_buttons', None)

        if quick_buttons_json_array is not None:
            self.quick_reply = get_buttons(quick_buttons_json_array)

    @abstractmethod
    def get_send_message(self):
        pass

    def get_quick_reply(self):
        if self.quick_reply is None:
            return None

        items = []
        for quick_reply_item in self.quick_reply:
            items.append(QuickReplyButton(action=quick_reply_item.to_button()))

        return QuickReply(items)


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
