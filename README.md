# 微信机器人
使用`django`+`drf`来作为后端   
使用`sqlserver`作为服务器  
使用[lemonWechatRobot](https://blog.csdn.net/u014431237/article/details/80293709)控制信息收发  
## 已有的功能
* 根据数据库中的设置的应答语句来进行应答 
* 增加对应关键字的返回（比如查快递 查天气  
* 检测数据库中未发送的信息 来完成自动发送 
## 关于数据库
由于`django`自带的数据库引擎不支持`mssql` 需要另行安装  
我使用的是[django-pyodbc-azure](https://pypi.org/project/django-pyodbc-azure/)作为后端引擎  
使用方法可以查看文档   
## 使用 
首先需要新建一个`python`虚拟环境
```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
将config中base的参数按需更换(比如 LWR的key   
更换`wxbot/settings.py`中的数据库参数 

```bash
python manage migrate 
#迁移数据库
python manage.py runserver
#启动服务
```
## 增加新功能
只需要在`wx_talk`文件夹中`views.py`增加对应的函数即可  
目前已经带了两个功能分别为`查快递`与`查天气`    
关键字映射的方法 在`wx_talk.core`中