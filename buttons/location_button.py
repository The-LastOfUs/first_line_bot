from linebot.models import LocationAction

from buttons.buttonBase import ButtonBase


class LocationButton(ButtonBase):
    def __init__(self, button_json_obj):
        super().__init__(button_json_obj)

    def to_button(self):
        return LocationAction(label=self.label)
