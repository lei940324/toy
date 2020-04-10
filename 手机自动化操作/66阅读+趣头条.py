# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:11:11 2019

@author: Administrator
"""
import threading
import re
import subprocess
from appmi import dxpath
import time
import random

def run(mi, bao=False, video=False, read=True):  

    # def open_screen():
    #     mi.d.press(26) # power
    #     time.sleep(1)
    #     mi.d.swipe(300, 300, 1000, 300, 0.1)
    
    if read:
        #66阅读程序启动
        mi.d.session("com.tencent.mm") # start
        mi.click('//*[@text="我"]/preceding-sibling::node')
        mi.click('//*[@text="收藏"]')
        time.sleep(2)
        while True:
            if '66阅读' in mi.get_text('//*[@resource-id="com.tencent.mm:id/bb"]',False):
                mi.click('//*[@text="66阅读"]')
                break
            mi.d.swipe(300, 1000, 300, 300, 0.1)
        
        #mi.exists('//*[@text="开始阅读"]')
        mi.click('//*[@text="开始阅读"]')  
        time.sleep(2)  
        if mi.exist('//*[@text="文章更新中"]') :EXIT=True
        else : EXIT = False
        if not EXIT:
            time.sleep(6)        
            while True:
                mi.d.press(4) # back
                time.sleep(11) 
                try : 
                    if mi.exist('//*[@text="文章更新中"]') : break
                except : pass
        mi.d.press(3) # home
        print('66阅读已完毕')
    
    #趣头条
    while True:
        if video:
            #if d.serial=='d5212f2c':
            mi.d.session("com.jifen.qukan") # start
            mi.click('//*[@text="小视频"]/..')
            ci = random.randint(200, 300)
            for _ in range(ci):
                times = random.uniform(6, 8)
                time.sleep(times)
# =============================================================================
#                 if not mi.exist('//*[@text="小视频"]') : 
#                     print('趣阅读已完毕')
#                     break
# =============================================================================
                mi.d.swipe(300, 1500, 300, 300, 0.01)
                
        #刷宝
        if bao:
            mi.d.session("com.jm.video") # start
            ci = random.randint(200, 300)
            for i in range(ci):
                times = random.uniform(8, 20)
                time.sleep(times)
                mi.d.swipe(300, 1500, 300, 300, 0.01)
                
        
                
# =============================================================================
#             d.press(3) # home
#             print('趣阅读已完毕')
#     d.press(26) # power
# =============================================================================
    

if __name__ == '__main__':   
    # 获取设备ID
    dev = subprocess.getstatusoutput("adb devices")[1]
    dev_ID = re.findall(r'\n(.*?)\t', dev)

    # 创建线程
    runthread = []
    for i, ID in enumerate(dev_ID, start=1):
        print(f'机名:phone{i}; ID:{ID}')
        threadObj = threading.Thread(target=run,args=[dxpath(ID)])
        threadObj.start()
        runthread.append(threadObj)

    # 结束线程
    for single in runthread:
        single.join()
    print('程序已运行结束')
