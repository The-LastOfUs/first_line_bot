import sys
import os

if len(sys.argv) > 1 and 'debug' in sys.argv:
    print('set debug key')
    lineBotKey = 'AijUGmFB6Z7cxg0FHBO08dOtJVvJ/iSbeCChYAk90u6XiWYFUxmlIrFeXq1kgSrmm9mnRQAQ6ZRYnWsY5B1Z9jBBhpxSUtYMk' \
                 'dfg8l5KKOa+K8QRYn1M8qQYHK87JzAncFmHN5+SUqcbZU2WhTkgUwdB04t89/1O/w1cDnyilFU='
    webHookKey = '5ad181a3428b90c433f4b8e411f19abc'
    DOMAIN = 'https://app.dev.angelsctek.com/api'
    SALES_WEB_URL = 'https://sales.dev.angelsctek.com'
else:
    #  release key
    lineBotKey = 'O0uYQ4ZwnqhAKcS9fufK/shJXVXxWEOWTj4Thxo78Wu3a+xJJZxDqnS5WoCXrsV3Ix4XMsgxW9rdsn52SpKM6pl8VycJ2uZ1d5' \
                 'zfHZnQraEnsfdKwz9t4/O+npMh7dRvmydVQ1wLhJxhjQLrb0O5MgdB04t89/1O/w1cDnyilFU='
    webHookKey = '06fd9106919a98c2b69ce2457760698b'
    DOMAIN = 'https://app.angelsctek.com/api'
    SALES_WEB_URL = 'https://sales.angelsctek.com'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

