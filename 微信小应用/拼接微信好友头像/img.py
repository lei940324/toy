# -*- coding: utf-8 -*-
"""
需要先扫码登陆

@author: lei
"""
import itchat
import math
import PIL.Image as Image


itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]   

# 获取好友头像
name = []
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    name.append(i["NickName"])
    fileImage = open(rf'头像\{i["NickName"]}.jpg','wb')
    fileImage.write(img)
    fileImage.close()

# 拼接各头像
num = len(friends)
each_size = int(math.sqrt(float(640*640)/num))
lines = int(640/each_size)
image = Image.new('RGBA', (640, 640))
x = 0
y = 0
for i in name:
    img = Image.open(rf'头像\{i}.jpg')
    img = img.resize((each_size, each_size), Image.ANTIALIAS)
    image.paste(img, (x * each_size, y * each_size))
    x += 1
    if x == lines:
        x = 0
        y += 1
image.save(r'头像\all.png')
itchat.send_image(r'头像\all.png', 'filehelper')