from linebot.models import TextSendMessage

from template.template_base import TemplateBase


class SendErrorTemplate(TemplateBase):
    def __init__(self, json_data, status):
        super().__init__(json_data)
        self.status = status
        self.message = json_data['message']
        print('SendError: ', status, ", ", self.message)

    def get_send_message(self):
        text = "錯誤: " + str(self.status) + ", " + self.message
        return TextSendMessage(text)
