from linebot.models import CameraRollAction

from buttons.buttonBase import ButtonBase


class CameraRollButton(ButtonBase):
    def __init__(self, button_json_obj):
        super().__init__(button_json_obj)

    def to_button(self):
        return CameraRollAction(label=self.label)
