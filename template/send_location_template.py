from template.template_base import TemplateBase
from linebot.models import LocationSendMessage


class SendLocationTemplate(TemplateBase):
    def __init__(self, json_data):
        super().__init__(json_data)
        self.title = json_data['title']
        self.address = json_data['address']
        self.latitude = json_data['latitude']
        self.longitude = json_data['longitude']

    def get_send_message(self):
        return LocationSendMessage(title=self.title,
                                   address=self.address,
                                   latitude=self.latitude,
                                   longitude=self.longitude,
                                   quick_reply=self.get_quick_reply())
