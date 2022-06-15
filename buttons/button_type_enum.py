from enum import Enum


# 按鈕類別
# name: 對應line文件的action
# value: response回傳的type
class ButtonTypeEnum(Enum):
    # 訊息
    MESSAGE = 'text'
    # 不會回傳訊息
    POST_BACK = 'post_back'
    # 日期
    DATE = 'date'
    # 時間
    TIME = 'time'
    # 日期+時間
    DATE_TIME = 'datetime'
    # 地點
    LOCATION = 'gps'
    # 相機
    CAMERA = 'camera'
    # 相簿
    CAMERA_ROLL = 'album'
    # uri
    URI = 'link'
