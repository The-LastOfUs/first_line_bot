from linebot.models import CarouselColumn, TemplateSendMessage, CarouselTemplate

from template.template_base import TemplateBase, get_buttons
# from util import template_factory


class SendCarouselTemplate(TemplateBase):
    def __init__(self, json_data):
        super().__init__(json_data)
        # columns max 10
        self.carousel_columns = []
        for json_obj in json_data['columns']:
            self.carousel_columns.append(Carousel(json_obj))
        # rectangle or square, default rectangle
        self.image_aspect_ratio = json_data.get('image_aspect_ratio', None)
        # cover or contain, default cover
        self.image_size = json_data.get('image_size', None)

    def get_send_message(self):
        columns = []

        for carousel in self.carousel_columns:
            columns.append(carousel.to_carousel_column())

        return TemplateSendMessage(
            alt_text="電腦版無法使用",
            template=CarouselTemplate(
                columns=columns,
                image_aspect_ratio=self.image_aspect_ratio,
                image_size=self.image_size)
        )


class Carousel:
    def __init__(self, json_obj):
        self.title = json_obj.get('title', None)
        self.text = json_obj['text']
        # buttons max 3
        self.buttons = get_buttons(json_obj['buttons'])
        # 如有使用圖片，全部的carousel都要加圖片
        self.thumbnail_image_url = json_obj.get('thumbnail_image_url', None)
        # default #FFFFFF
        self.image_background_color = json_obj.get('image_background_color', None)

    def to_carousel_column(self):
        # 增加按鈕
        new_actions = []
        for button in self.buttons:
            new_actions.append(button.to_button())

        return CarouselColumn(text=self.text,
                              title=self.title,
                              actions=new_actions,
                              thumbnail_image_url=self.thumbnail_image_url,
                              image_background_color=self.image_background_color)
