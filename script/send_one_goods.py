import requests
import itchat
import time
import re

itchat.auto_login()
itchat.dump_login_status()

allText2 = '''还有这个洗手液，孕妇宝宝适用 柠檬香型500g*3瓶正装，一起拼一下
———————— 
京东价：¥29.90
券后价：¥19.90
领券抢购：https://u.jd.com/PZjz2Z
'''
allText1 = '''谁下班和我拼一个，京东，京东，蓝月亮 洗衣液2瓶4袋套装 洁净1kg*2瓶+500g*4袋装
———————— 
京东价：¥109.90
券后价：¥59.90
领券抢购：https://u.jd.com/dQQTK3
'''
chatrooms = itchat.get_chatrooms(update=True)
# 已发送的群数量
send_count = 0
for chatroom in chatrooms:
    # 拿到群昵称
    NickName = chatroom['NickName']
    if not re.findall('专访|希鸥|峰会|纳斯达克|媒体|搜狐|大咖|CEO说', NickName):
        name = itchat.search_chatrooms(name=chatroom['NickName'])
        XiaoMing = name[0]["UserName"]
        itchat.send(allText1, XiaoMing)
        print('当前发送-------' + NickName)
        send_count += 1
    else:
        print('此群不在群发范围内-------' + NickName)
    time.sleep(5)

print('此次发送到' + str(send_count) + '个群里')


