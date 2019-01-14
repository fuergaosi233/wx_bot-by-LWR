from django.db import models

# Create your models here.
class receive(models.Model):
    msg_id = models.CharField(max_length=100)
    msg_type = models.CharField(max_length=20)
    msg_time = models.TimeField()
    at_list= models.CharField(max_length=30)
    from_wxid= models.CharField(max_length=30)
    send_wxid= models.CharField(max_length=30)
    recv_wxid= models.CharField(max_length=30)
    msg= models.CharField(max_length=200)
    