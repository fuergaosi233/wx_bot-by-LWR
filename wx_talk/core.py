    # 返回信息格式
    #{
    # "apiKey":"软件上设置的密匙",
    # "apiName":"处理类型（日志会显示）",
    # "sendType":-1不处理,仅显示日志  发送消息 1文本  3图片 5名片  6XMl,     
    # "sendWxid":"好友或群的wxid",
    # "msg":"发送的消息",
    # "atName":"柠檬（可选）",
    # "atWxid":"群成员wxid（可选）"
    #}
    # msg_objects内容
    # msgID 
    # type
    # time
    # atlist
    # fromWxid
    # sendWxid
    # recvWxid
    # msg 
from .models import qa
from config import base
import logging
import requests
import json
class talk():
    def __init__(self):
        self.route={}
        all_kv = qa.objects.all()
        for kv in all_kv:
            self.route[kv.key]=lambda x:{'msg':kv.value}

    def add(self,name):
        def decorate(func):
            self.route[name]=func
        return decorate

    def parser(self,msg_objects,res_msg):
        data={
            "apiKey":base.API_KEY,
            "apiName":base.API_KEY,
            "sendType":res_msg.get('sendType',1),     
            "sendWxid":msg_objects['sendWxid'],
            "msg":res_msg.get('msg','回复错误'),
            "atName":res_msg.get('atName',''),
            "atWxid":res_msg.get('atWxid',''),
        }
        return data

    def run(self,msg_objects):
        msg=msg_objects['msg']
        for msgkey in self.route.keys():
            if msgkey == msg[:len(msgkey)]:
                logging.info(f'{msgkey}被触发')
                res_msg=self.route[msgkey](msg_objects)
                return self.parser(msg_objects,res_msg)
        else:
            return self.parser(msg_objects,{'sendType':-1})

