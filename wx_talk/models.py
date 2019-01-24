from django.db import models

# Create your models here.
class receive_msg(models.Model):
    msgID = models.CharField(max_length=100)
    type = models.IntegerField(null=True,blank=True)
    time = models.CharField(max_length=50,null=True,blank=True)
    atlist = models.CharField(max_length=300,null=True,blank=True)
    fromWxid = models.CharField(max_length=100,null=True,blank=True)
    sendWxid = models.CharField(max_length=100,null=True,blank=True)
    recvWxid = models.CharField(max_length=100,null=True,blank=True)
    msg = models.CharField(max_length=500,null=True,blank=True)

class qa(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=30)

class send_msg(models.Model):
    wx_id=models.CharField(max_length=100)
    msg = models.CharField(max_length=400)

    # "apiKey":"软件上设置的密匙",
    # "apiName":"处理类型（日志会显示）",
    # "sendType":-1不处理,仅显示日志  发送消息 1文本  3图片 5名片  6XMl,     
    # "sendWxid":"好友或群的wxid",
    # "msg":"发送的消息",
    # "atName":"柠檬（可选）",
    # "atWxid":"群成员wxid（可选）"
