from buttons.buttonBase import ButtonBase
from linebot.models import (URIAction)


class UriButton(ButtonBase):
    def __init__(self, button_json_obj):
        super().__init__(button_json_obj)
        self.uri = button_json_obj['value']

    def to_button(self):
        return URIAction(label=self.label,
                         uri=self.uri)
