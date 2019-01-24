import json
import os
CONFIG_PATH = os.path.abspath('..')
DATABASE = {
    'host': '127.0.0.1',
    'name': 'SA',
    'password': 'test2019!'
}
API_KEY='lemon'
API_NAME='test1'
with open(os.path.join('.','config','ExpressDelivery100.json'), 'r') as f:
    EXPRESS_DATA = json.load(f)
with open(os.path.join('.','config','citylist.json'), 'r') as f:
    CITYLIST = json.load(f)
SERVER_HOST='http://blog.holegots.com:7003'