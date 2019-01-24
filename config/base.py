import json
import os
CONFIG_PATH = os.path.abspath('..')
API_KEY='lemon'
API_NAME='test1'
with open(os.path.join('.','config','ExpressDelivery100.json'), 'r') as f:
    EXPRESS_DATA = json.load(f)
with open(os.path.join('.','config','citylist.json'), 'r') as f:
    CITYLIST = json.load(f)
SERVER_HOST='' #接受信息的LWR服务器