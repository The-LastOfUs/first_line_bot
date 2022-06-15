from abc import abstractmethod


class ButtonBase:
    def __init__(self, button_json_obj):
        self.label = button_json_obj['title']

    @abstractmethod
    def to_button(self):
        pass
