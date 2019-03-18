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


chatrooms = itchat.get_chatrooms(update=True)
print(len(chatrooms))
# 已发送的群数量
send_count = 0
for chatroom in chatrooms:
    # 拿到群昵称
    NickName = chatroom['NickName']
    if not re.findall('专访|希鸥|峰会|纳斯达克|媒体|搜狐|大咖|CEO说', NickName):
    # if NickName == '幼儿园大班':
        name = itchat.search_chatrooms(name=chatroom['NickName'])
        XiaoMing = name[0]["UserName"]
        itchat.send(allText, XiaoMing)
        print('当前发送-------' + NickName)
        send_count += 1
    else:
        print('此群不在群发范围内-------'+NickName)
    time.sleep(5)

print('此次发送内容：' + allText)
print('此次发送到' + str(send_count) + '个群里')
