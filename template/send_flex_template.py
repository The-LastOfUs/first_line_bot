from linebot.models import FlexSendMessage

from template.template_base import TemplateBase


class SendFlexTemplate(TemplateBase):
    def __init__(self, json_data):
        super().__init__(json_data)
        self.title = json_data['title']
        self.content = json_data['content']

    def get_send_message(self):
        return FlexSendMessage(
            alt_text='無法使用電腦版',
            contents=self.content,
            quick_reply=self.get_quick_reply()
        )
