from linebot.models import (TemplateSendMessage, MessageAction, ConfirmTemplate, PostbackAction)

from buttons.button_type_enum import ButtonTypeEnum
from template.template_base import TemplateBase
from util import template_factory


class SendIfTemplate(TemplateBase):
    def __init__(self, json_data):
        super().__init__(json_data)
        self.title = json_data['title']
        self.buttons = []
        # buttons max 2
        self.buttons = template_factory.get_buttons(json_data['buttons'])

    def get_send_message(self):
        # 按鈕
        new_actions = []
        for button in self.buttons:
            new_actions.append(button.to_button())

        buttons_template = ConfirmTemplate(
            text=self.title,
            actions=new_actions
        )

        buttons_template_message = TemplateSendMessage(
            alt_text="無法使用電腦版",
            template=buttons_template,
            quick_reply=self.get_quick_reply()
        )

        return buttons_template_message
