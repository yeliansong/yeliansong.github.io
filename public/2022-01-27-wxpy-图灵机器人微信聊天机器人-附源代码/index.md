# wxpy+图灵机器人微信聊天机器人--附源代码


# 1 背景

看到很多小伙伴用微信玩聊天机器人，能自动回复，看着还挺像模像样的，心里痒痒，也想着自己做个聊天机器人玩玩，初步想法是能每天定时给女朋友“早安”消息，推送当天的天气，引入图灵机器人能自动回复女朋友的消息，尽量回答的有水平点。

# 2 方案实现
## 2.1 工具
-  微信号两个，用来做测试
-  调用wxpy pthon库
-  python3.5 及以上版本
-  注册图灵机器人

## 2.2 整个原理
原理是非常简单的，wxpy 是在itchat 基础上，对一些接口进行了优化，并提升了模块调用的易用性，同时对部分功能也进行了扩充。itchat 大家都知道是一个开源的微信个人号接口，这里列下wxpy 可以做的一些事：
- 控制路由器、智能家居等具有开放接口的玩意儿

- 运行脚本时自动把日志发送到你的微信

- 加群主为好友，自动拉进群中

- 跨号或跨群转发消息

- 自动陪人聊天

- 逗人玩

- ...

  

  附上wxpy 的github： https://github.com/youfou/wxpy

原理也是非常简单，wxpy 是利用网页版微信API来实现微信里的联系人搜索和消息发送，同时wxpy 是支持图灵机器人接口，所以可以将机器人的自动回复发送。**这里要注意，如果你的微信不支持网页版登陆，整个也是跑不通的。**

## 2.3 实现步骤
> **安装wxpy**

```shell 
sudo pip3 install -U wxpy
```
> **图灵机器人注册**

可参照这个链接，购买一个月体验版玩玩：[https://www.turingapi.com/](https://www.turingapi.com/)
> **代码**

```python
# -*- coding: UTF-8 -*-    # 防止搜的用户名是中文
from wxpy import *         # 调用wxpy 包
bot = Bot()                # 初始化机器人，网页扫码登陆
friend = bot.friends().search('we_test')[0]          #搜索昵称为 test 的好友
friend1 = bot.friends().search('大聪明')[0]           #搜索昵称为 大聪明 的好友
group = bot.groups().search('test')[0]               #搜索为 test 的群组
tuling = Tuling(api_key='58e4c4c..........')         #调用图灵机器人API

#主动发送消息
friend.send('hello world')         #向 test 好友主动发送 ‘hello world’
group.send('for test')             #向test群组发送消息

#自动回复
@bot.register(friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)      #图灵机器人自动回复

@bot.register(friend1)
def reply_my_friend1(msg):
    tuling.do_reply(msg)     #图灵机器人自动回复
    
@bot.register(group)
def reply_my_group(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:  #msg.chat 和 msg.is_at 可参考文档类型说明。@ 我才回复                                              
        return
    else:
        tuling.do_reply(msg)

bot.join()              #保持登陆状态
```

## 2.4 改良版本
只是玩一些自动回复还是没啥意思，改良版本加上每天早上和晚上的定点发送“早安”、“晚安”，每隔一小时提醒喝水、走动，同时推送天气信息。
思路就是加一个定时线程，一直跑，然后到固定时间了就调wxpy 的接口去发送通知消息。推送天气信息，我用的是goole 的天气API 接口，也是拉取后解析出需要的信息发送消息。我来贴下代码：

```python
#定时推送早安和晚安
def run_thread():
    list = [11,12,13,14,15,16,17]  #这些时间点发送喝水的通知
    while True:
        now = datetime.now()
        if now.hour == 6 and now.minute == 00 and now.second == 00:
            friend.send('早上好呀')
            # 获取当天的天气
            temp,sky = get_weather()        #封装了一份函数，调取
            friend.send('今天天气:'+ temp + '   ' + sky)
        elif(now.hour in list) and now.minute == 00 and now.second == 00:   
            friend.send('喝点水，走动下吧')
        elif now.hour == 18 and now.minute == 30 and now.second == 00:
            friend.send('工作了一天幸苦了')
        elif now.hour == 23 and now.minute == 00 and now.second == 00:
            friend.send('太晚了，早点休息吧')


        time.sleep(1) 
```



获取天气的接口

```python
#调google 天气API，获取天气信息
def get_weather():
    city = "hubei"    #可修改城市
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # list having all div tags having particular clas sname
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

    # particular list with required data
    strd = listdiv[5].text

    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # printing all the data
    print("Temperature is", temp)
    #print("Time: ", time)
    #print("Sky Description: ", sky)
    #print(other_data)
    return temp,sky
```


简简单单，整个功能就做完了。



## 2.5 项目源代码

运行过程中需要安装的一些库，可以直接pip3 直接安装。

```python
# -*- coding: UTF-8 -*-
from wxpy import *
from datetime import datetime
import threading
import time
import requests
from bs4 import BeautifulSoup

def get_weather():
    city = "hubei"
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # list having all div tags having particular clas sname
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

    # particular list with required data
    strd = listdiv[5].text

    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # printing all the data
    print("Temperature is", temp)
    #print("Time: ", time)
    #print("Sky Description: ", sky)
    #print(other_data)
    return temp,sky

#定时推送早安和晚安
def run_thread():
    list = [11,12,13,14,15,16,17]  #这些时间点发送喝水的通知
    while True:
        now = datetime.now()
        if now.hour == 6 and now.minute == 00 and now.second == 00:
            friend.send('早上好呀')
            # 获取当天的天气
            temp,sky = get_weather()  #封装了一份函数，调取
            friend.send('今天天气:'+ temp + '   ' + sky)
        elif(now.hour in list) and now.minute == 00 and now.second == 00:
            friend.send('喝点水，走动下吧')
        elif now.hour == 18 and now.minute == 30 and now.second == 00:
            friend.send('工作了一天幸苦了')
        elif now.hour == 23 and now.minute == 00 and now.second == 00:
            friend.send('太晚了，早点休息吧')

        time.sleep(1) 

if __name__=="__main__":
    #起一个线程去跑定时任务
    bot = Bot()
    friend = bot.friends().search('we_test')[0]
    friend1 = bot.friends().search('大聪明')[0]
    group = bot.groups().search('test')[0]
    tuling = Tuling(api_key='58e4c4c..................')

    @bot.register(friend)
    def reply_my_friend(msg):
        tuling.do_reply(msg)     #图灵机器人自动回复

    @bot.register(friend1)
    def reply_my_friend1(msg):
        tuling.do_reply(msg)     #图灵机器人自动回复

    @bot.register(group)
    def reply_my_group(msg):
        if isinstance(msg.chat, Group) and not msg.is_at:
            return
        else:
            tuling.do_reply(msg)
         
    t = threading.Thread(target=run_thread, name='push_msg')
    t.start()

    bot.join() #保持登陆状态
```


