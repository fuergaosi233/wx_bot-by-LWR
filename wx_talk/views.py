from django.shortcuts import render
from .models import receive_msg as msg
from .seriarizers import msgSeriarizer
from .core import talk
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging 
import threading
import time
from wx_talk.models import send_msg as sm_model
from .tools import express,weather,send_msg


logging.basicConfig(level=logging.DEBUG)
# Create your views here.
class msg_monitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        threading.name='monitor'
    def run(self):
        while True:
            all_msg=sm_model.objects.all()
            if len(all_msg)>0:
                tmp_msg=all_msg.first()
                send_msg(tmp_msg.wx_id, tmp_msg.msg)
                tmp_msg.delete()
            time.sleep(1)
monitor=msg_monitor()
monitor.start()
app=talk()
@app.add('你好')
def hello(msg):
    data={
        'msg':'hello'
    }
    return data

@app.add('快递')
def express_data(msg):
    try:
        kind=msg.get('msg').split(' ')[1]
        postid=msg.get('msg').split(' ')[2]
    except:
        return {'msg':'参数错误'}
    data = express(kind,postid)
    return {'msg':data}    

@app.add('天气')
def weather_data(msg):
    try:
        position= msg.get('msg').split(' ')[1]
    except:
        return {'msg':'参数错误'}
    try:
        logging.info(position)
        data = weather(position)
    except Exception as e:
        logging.exception(e)
        return {'msg':'天气获取失败'}
    city = data['city']
    temp = data['temp']
    WD = data['WD']
    WS = data['WS']
    time = data['time']
    return {'msg':f'{city} 温度:{temp} 风向:{WD} 风力:{WS} 更新时间{time}'}

class TalkAPIView(APIView):
    serializer_class = msgSeriarizer
    def post(self,request,format=None):
        seriarizer = msgSeriarizer(data=request.data)
        print(request.data)
        if seriarizer.is_valid():
            seriarizer.save()
            logging.info(f'记录成功')
            return Response(app.run(seriarizer.data),status.HTTP_200_OK)
        else:
            print('创建失败')
            return Response(seriarizer.errors,status.HTTP_400_BAD_REQUEST)