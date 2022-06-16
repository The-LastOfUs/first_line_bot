import sys
import os

if len(sys.argv) > 1 and 'debug' in sys.argv:
    print('set debug key')
    lineBotKey = 'ZCyA68bpkHyWKcaK0ZumuImzTRWmiv9G49dSy1sATpBS58mgm9mJNF6g/T3sj2PVdNfdX+11rpIhmv3UtO9f04CLJqASNMmT2LOgT3GscQy2RcFcWvLz6O0fB2Hg6bLtdIlda9WZtTeaW+/baRflOAdB04t89/1O/w1cDnyilFU='
    webHookKey = '34dd48d922b58fa8365b6f893726ce2d'
    couponBotKey = 'fH8U3oGdkg3GK+Nbf9OmtrHkTIipMBvSNm7LJvxo+s+lLL/ze3/TdHIsGFL2IRx2phgCUAyntHER1h8jcRD4/ihLR6zFSJAQ0S2YhznRRwbu9BeR1PODhCvzY+6GmbDg9HFIjPa+mj3BwiNHa9EokgdB04t89/1O/w1cDnyilFU='
    couponChannelSecret = '897adad1b36864fe64f3639e7e740a10'
    DOMAIN = 'https://app.dev.angelsctek.com/api'
    SALES_WEB_URL = 'https://sales.dev.angelsctek.com'
else:
    #  release key
    lineBotKey = 'ZCyA68bpkHyWKcaK0ZumuImzTRWmiv9G49dSy1sATpBS58mgm9mJNF6g/T3sj2PVdNfdX+11rpIhmv3UtO9f04CLJqASNMmT2LOgT3GscQy2RcFcWvLz6O0fB2Hg6bLtdIlda9WZtTeaW+/baRflOAdB04t89/1O/w1cDnyilFU='
    webHookKey = '34dd48d922b58fa8365b6f893726ce2d'
    couponBotKey = 'fH8U3oGdkg3GK+Nbf9OmtrHkTIipMBvSNm7LJvxo+s+lLL/ze3/TdHIsGFL2IRx2phgCUAyntHER1h8jcRD4/ihLR6zFSJAQ0S2YhznRRwbu9BeR1PODhCvzY+6GmbDg9HFIjPa+mj3BwiNHa9EokgdB04t89/1O/w1cDnyilFU='
    couponChannelSecret = '897adad1b36864fe64f3639e7e740a10'
    DOMAIN = 'https://app.angelsctek.com/api'
    SALES_WEB_URL = 'https://sales.angelsctek.com'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

