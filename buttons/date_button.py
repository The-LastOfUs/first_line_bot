from linebot.models import DatetimePickerAction

from buttons.buttonBase import ButtonBase
from buttons.button_type_enum import ButtonTypeEnum


class DateButton(ButtonBase):
    def __init__(self, button_json_obj):
        super().__init__(button_json_obj)
        self.data = ButtonTypeEnum.DATE.value

    def to_button(self):
        return DatetimePickerAction(
            label=self.label,
            data=self.data,
            mode='date')
