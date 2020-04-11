# -*- coding: utf-8 -*-
"""
Created on 2020年3月29日

@author: deng
"""

import re
import itchat as wx
import pandas as pd

print('''说明：
本程序功能为汇总微信信息，并导入Excel文件
****************************************************
程序运行需扫描二维码登陆微信

微信信息格式例如：
姓名：张三
电话：14565343245
地址：山东省青岛市...

收到信息默认自动回复“已查收”，如需更改请输入2
输入样式为：姓名，电话，地址
(注：中间用中文逗号隔开)
****************************************************''')

keyword = input('请输入汇总信息关键词（中间用逗号隔开）:')
kword = re.split('[,.，。；;]', keyword)

# 去掉列表里空元素
while '' in kword:
    kword.remove('')
select = input('是否更改自动回复语句，默认“已查收”，不改请输入1，改则输入2：')

while select != '1' and select != '2':
    select = input('输入错误，请重新输入（1或者2）:')
    if select == '1' or select == '2':
        break
if select == '1':
    auto_reply = '已查收'
if select == '2':
    auto_reply = input('请输入自动回复语句:')

# 初始化数据
df = pd.DataFrame(columns=kword)   # 创建表头
someone = []   # 保存某个人信息
n = 0   # 已统计人数


@wx.msg_register([wx.content.TEXT])
def text_reply(msg):
    # 先判断接受到的信息是否为文本类型
    global n, someone, df
    if msg['Type'] == 'Text':
        info = msg['Content']

        for i in kword:
            if i.strip() in info:
                try:
                    someone.append(re.findall(f'{i}.(.+)', info)[0].strip())
                except:
                    pass

        if len(someone) == len(kword):
            wx.send_msg(auto_reply, msg['FromUserName'])
            n += 1
            df.loc[str(n)] = someone
            df.to_excel('output.xlsx', index=False)
            print(f'已汇总{n}人')
        someone = []


if __name__ == '__main__':
    wx.auto_login()
    wx.run()
