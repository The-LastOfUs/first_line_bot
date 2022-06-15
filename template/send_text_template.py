from linebot.models import (TextSendMessage)

from template.template_base import TemplateBase


class SendTextTemplate(TemplateBase):
    def __init__(self, json_data):
        super().__init__(json_data)
        self.title = json_data['title']

    def get_send_message(self):
        return TextSendMessage(text=self.title,
                               quick_reply=self.get_quick_reply())
