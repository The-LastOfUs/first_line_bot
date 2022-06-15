from linebot.models import (TemplateSendMessage, ButtonsTemplate)

from template.template_base import TemplateBase
from util import template_factory


class SendButtonsTemplate(TemplateBase):
    def __init__(self, json_data):
        super().__init__(json_data)
        self.title = json_data['title']
        self.text = json_data.get('text', '-')
        # buttons max 4
        self.buttons = template_factory.get_buttons(json_data['buttons'])
        self.thumbnail_image_url = json_data.get('thumbnail_image_url', None)
        # rectangle or square, default rectangle
        self.image_aspect_ratio = json_data.get('image_aspect_ratio', None)
        # cover or contain, default cover
        self.image_size = json_data.get('image_size', None)
        # default #FFFFFF
        self.image_background_color = json_data.get('image_background_color', None)

    def get_send_message(self):
        # 增加按鈕
        new_actions = []
        for button in self.buttons:
            new_actions.append(button.to_button())

        buttons_template = ButtonsTemplate(
            title=self.title,
            text=self.text,
            actions=new_actions,
            thumbnail_image_url=self.thumbnail_image_url,
            image_aspect_ratio=self.image_aspect_ratio,
            image_size=self.image_size,
            image_background_color=self.image_background_color
        )

        buttons_template_message = TemplateSendMessage(
            alt_text='無法使用電腦版',
            template=buttons_template,
            quick_reply=self.get_quick_reply()
        )

        return buttons_template_message
