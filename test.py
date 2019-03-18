import requests
import itchat
import time
import re

itchat.auto_login()
itchat.dump_login_status()

allText = '''还有这个洗手液，孕妇宝宝适用 柠檬香型500g*3瓶正装，一起拼一下
———————— 
京东价：¥29.90
券后价：¥19.90
领券抢购：https://u.jd.com/PZjz2Z
'''

chatrooms_list = []
for i in range(2):
    chatrooms = itchat.get_chatrooms(update=True)
    for item in chatrooms:
        if item['NickName'] not in chatrooms_list:
            chatrooms_list.append(item['NickName'])
    print(i)

print('此微信号有%d个群聊'%len(chatrooms_list))
print(chatrooms_list)







