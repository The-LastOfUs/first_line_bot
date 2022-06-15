from linebot.models import MessageAction

from buttons.buttonBase import ButtonBase


class MessageButton(ButtonBase):
    def __init__(self, button_json_obj):
        super().__init__(button_json_obj)

        # Text sent when the action is performed
        self.text = button_json_obj.get('value', self.label)

    def to_button(self):
        return MessageAction(label=self.label, text=self.text)
