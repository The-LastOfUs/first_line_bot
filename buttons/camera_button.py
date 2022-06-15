from linebot.models import CameraAction

from buttons.buttonBase import ButtonBase


class CameraButton(ButtonBase):
    def __init__(self, button_json_obj):
        super().__init__(button_json_obj)

    def to_button(self):
        return CameraAction(label=self.label)
