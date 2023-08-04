# wxpy+Turing robot WeChat chat robot -- with source code


# 1 Background

I saw a lot of friends using WeChat to play chatbots, and they can reply automatically. They look pretty decent, and I feel itchy. I also want to make a chatbot by myself. The initial idea is to be able to send "Good morning" to my girlfriend on a regular basis every day "News, push the weather of the day, introduce a Turing robot that can automatically reply to your girlfriend's message, and try to answer as level as possible.

# 2 Solution implementation

## 2.1 Tools

- Two WeChat IDs for testing
- Call wxpy python library
- python3.5 and above
- Register Turing Robot

## 2.2 The whole principle

The principle is very simple. On the basis of itchat, wxpy optimizes some interfaces, improves the ease of use of module calls, and expands some functions. Everyone knows that itchat is an open source WeChat personal account interface. Here are some things that wxpy can do:

- Control routers, smart homes and other gadgets with open interfaces

- Automatically send logs to your WeChat when running scripts

- Add the group owner as a friend and automatically pull into the group

- Forward messages across numbers or groups

- Chat with people automatically

- funny

-...

  

   Attach the github of wxpy: https://github.com/youfou/wxpy

The principle is also very simple. wxpy uses the web version of WeChat API to realize contact search and message sending in WeChat. At the same time, wxpy supports the Turing robot interface, so the robot's automatic reply can be sent. **It should be noted here that if your WeChat does not support web version login, the whole thing will not work. **

## 2.3 Implementation steps

> **install wxpy**

```shell
sudo pip3 install -U wxpy
```

> **Turing Robot Registration**

You can refer to this link to buy a one-month trial version to play: [https://www.turingapi.com/](https://www.turingapi.com/)

> **Code**

```python
# -*- coding: UTF-8 -*- # The user name to prevent the search is Chinese
from wxpy import * # call wxpy package
bot = Bot() # Initialize the robot, scan the code to log in
friend = bot.friends().search('we_test')[0] #search for friends whose nickname is test
friend1 = bot.friends().search('Big Clever')[0] #Search for friends whose nickname is Big Smart
group = bot.groups().search('test')[0] #Search for the group of test
tuling = Tuling(api_key='58e4c4c.......') #call Turing robot API

#Actively send a message
friend.send('hello world') #Send 'hello world' to the test friend
group.send('for test') #Send a message to the test group

#automatic response
@bot.register(friend)
def reply_my_friend(msg):
     tuling.do_reply(msg) # Turing robot auto-reply

@bot.register(friend1)
def reply_my_friend1(msg):
     tuling.do_reply(msg) # Turing robot auto-reply
    
@bot.register(group)
def reply_my_group(msg):
     if isinstance(msg.chat, Group) and not msg.is_at: #msg.chat and msg.is_at can refer to the document type description. @ I just replied
         return
     else:
         tuling.do_reply(msg)

bot.join() #Keep logging in
```

## 2.4 Improved version

Just playing some automatic replies is still not interesting. The improved version adds "good morning" and "good night" at fixed points every morning and evening, reminds to drink water and move around every hour, and pushes weather information at the same time.
The idea is to add a timing thread, keep running, and then adjust the wxpy interface to send notification messages when the fixed time is reached. To push the weather information, I use the weather API interface of goole, which is also to parse out the required information and send the message after pulling it. I will paste the code:

```python
#Push good morning and good night regularly
def run_thread():
     list = [11,12,13,14,15,16,17] #Send water drinking notifications at these time points
     while True:
         now = datetime. now()
         if now.hour == 6 and now.minute == 00 and now.second == 00:
             friend.send('Good morning')
             # Get the weather of the day
             temp, sky = get_weather() #encapsulate a function, call
             friend.send('Today's weather: '+ temp + ' ' + sky)
         elif(now.hour in list) and now.minute == 00 and now.second == 00:
             friend.send('Drink some water, let's move around')
         elif now.hour == 18 and now.minute == 30 and now.second == 00:
             friend.send('It's a hard day at work')
         elif now.hour == 23 and now.minute == 00 and now.second == 00:
             friend.send('It's too late, let's go to bed early')


         time. sleep(1)
```



API for getting weather

```python
#Tune google weather API to get weather information
def get_weather():
     city = "hubei" #City can be modified
     url = "https://www.google.com/search?q="+"weather"+city
     html = requests. get(url). content
     soup = BeautifulSoup(html, 'html. parser')

     # get the temperature
     temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

     # this contains time and sky description
     str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

     # format the data
     data = str. split('\n')
     time = data[0]
     sky = data[1]

     # list having all div tags having particular clas sname
     listdiv = soup. findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

     # particular list with required data
     strd = listdiv[5].text

     # formatting the string
     pos = strd. find('Wind')
     other_data = strd[pos:]

     # printing all the data
     print("Temperature is", temp)
     #print("Time: ", time)
     #print("Sky Description: ", sky)
     #print(other_data)
     return temp, sky
```


Simple, the whole function is done.



## 2.5 Project source code

Some libraries that need to be installed during operation can be installed directly with pip3.

````python
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
     html = requests. get(url). content
     soup = BeautifulSoup(html, 'html. parser')

     # get the temperature
     temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

     # this contains time and sky description
     str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

     # format the data
     data = str. split('\n')
     time = data[0]
     sky = data[1]

     # list having all div tags having particular clas sname
     listdiv = soup. findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

     # particular list with required data
     strd = listdiv[5].text

     # formatting the string
     pos = strd. find('Wind')
     other_data = strd[pos:]

     # printing all the data
     print("Temperature is", temp)
     #print("Time: ", time)
     #print("Sky Description: ", sky)
     #print(other_data)
     return temp, sky

#Push good morning and good night regularly
def run_thread():
     list = [11,12,13,14,15,16,17] #Send water drinking notifications at these time points
     while True:
         now = datetime. now()
         if now. hour == 6 and now. minute == 00 and now.second == 00:
             friend.send('Good morning')
             # Get the weather of the day
             temp, sky = get_weather() #encapsulate a function, call
             friend.send('Today's weather: '+ temp + ' ' + sky)
         elif(now.hour in list) and now.minute == 00 and now.second == 00:
             friend.send('Drink some water, let's move around')
         elif now.hour == 18 and now.minute == 30 and now.second == 00:
             friend.send('It's a hard day at work')
         elif now.hour == 23 and now.minute == 00 and now.second == 00:
             friend.send('It's too late, let's go to bed early')

         time. sleep(1)

if __name__=="__main__":
     #Start a thread to run the scheduled task
     bot = Bot()
     friend = bot.friends().search('we_test')[0]
     friend1 = bot.friends().search('big smart')[0]
     group = bot.groups().search('test')[0]
     tuling = tuling(api_key='58e4c4c..........')

     @bot.register(friend)
     def reply_my_friend(msg):
         tuling.do_reply(msg) # Turing robot auto-reply

     @bot.register(friend1)
     def reply_my_friend1(msg):
         tuling.do_reply(msg) # Turing robot auto-reply

     @bot.register(group)
     def reply_my_group(msg):
         if isinstance(msg.chat, Group) and not msg.is_at:
             return
         else:
             tuling.do_reply(msg)
         
     t = threading.Thread(target=run_thread, name='push_msg')
     t. start()

     bot.join() #Keep logging in
```
