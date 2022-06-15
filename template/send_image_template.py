from template.template_base import TemplateBase
from linebot.models import ImageSendMessage


class SendImageTemplate(TemplateBase):
    def __init__(self, json_data):
        super().__init__(json_data)
        self.original_content_url = json_data['original_content_url']
        self.preview_image_url = json_data['preview_image_url']

    def get_send_message(self):
        return ImageSendMessage(original_content_url=self.original_content_url,
                                preview_image_url=self.preview_image_url,
                                quick_reply=self.get_quick_reply())
