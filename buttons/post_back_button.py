from linebot.models import PostbackAction

from buttons.buttonBase import ButtonBase


class PostBackButton(ButtonBase):
    def __init__(self, button_json_obj):
        super().__init__(button_json_obj)
        self.data = button_json_obj['value']
        self.display_text = button_json_obj.get('display_text', self.label)

    def to_button(self):
        return PostbackAction(label=self.label, data=self.data, display_text=self.display_text)
