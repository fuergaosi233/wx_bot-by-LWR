import requests
import json
import logging
from config.base import *
from wx_talk.core import talk
app = talk()
def express(kind,postid):
    kind= EXPRESS_DATA.get(kind,None)
    if kind == None:
        return '快递错误' 
    url='http://www.kuaidi100.com/query'
    payload={
        'type':kind,
        'postid':postid,
    }
    data=requests.get(url,params=payload)
    data=data.json()
    logging.debug(json.dumps(data,indent=4,sort_keys=True))
    if data['message']=='ok':
        return data['data'][0]['ftime']+data['data'][0]['context']
    else:
        return data['message']

def translation():
    url='http://fanyi.youdao.com/translate?doctype=json&jsonversion=&type=&keyfrom=&model=&mid=&imei=&vendor=&screen=&ssid=&network=&abtest='
    data='merry me'
    response= requests.post(url,data=data)
    print(response.text)

def weather(city):
    city_id=CITYLIST.get(city,None)
    if city_id==None:
        return {'msg':'未找到地点'}
    url=f'http://www.weather.com.cn/data/sk/{city_id}.html'
    response=requests.get(url)
    response.encoding='gbk2312'
    data=response.json()
    data=data['weatherinfo']
    logging.debug(json.dumps(data,indent=4,sort_keys=True,ensure_ascii=False))
    return data
def send_msg(wxid,msg):
    data = app.parser({
        'fromWxid':wxid,
    },{'msg':msg})
    data=json.dumps(data)
    data=requests.post(SERVER_HOST,data=data)
    logging.info(data.json())