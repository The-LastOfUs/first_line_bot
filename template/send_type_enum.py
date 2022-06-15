from enum import Enum


class SendTypeEnum(Enum):
    # 文字
    TEXT = 'text'
    # 多個按鈕
    BUTTON = 'button'
    # 是/否兩顆按鈕
    IF = 'if'
    # 錯誤訊息
    ERROR = 'error'
    # 自訂
    FLEX = 'flex'

    CAROUSEL = 'carousel'

    IMAGE = 'image'
    VIDEO = 'video'
    LOCATION = 'gps'