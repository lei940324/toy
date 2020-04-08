# -*- coding: utf-8 -*-
"""
Created on 2020年3月26日晚

@author: lei
"""
from appmi import dxpath
import uiautomator2 as u2
import time
import logging
import os
import re
import threading
import subprocess


# adb kill-server --停止adb服务
# adb start-server --开启adb服务
# python -m weditor

class kings(threading.Thread):

    device_num = 0

    def __init__(self, name, device, num=60, timer=98, wait=20, level=2, jinbi=56):
        """
        Parameters
        ----------
        name   - 设备名
        device - 设备选择
        num    - 刷金币次数
        timer  - 随关卡时间调整
        wait   - 最大等待次数
        level  - 信息显示等级,0级最低,5级最大
        jinbi  - 每一关金币数量
        """

        super(kings, self).__init__()
        self.name = name
        self.device = device
        self.num = num
        self.timer = timer
        self.wait = wait
        self.level = level
        self.jinbi = jinbi

        self.mi = dxpath(device)
        kings.device_num += 1

    def run(self):
        """
        串联各流程
            1. 设置日志等级
            2. 第一次准备工作
            3. 正式开始循环
        """
        self.Info_level()
        self.ready()
        self.go()

    def Info_level(self):
        """
        日志等级设置
        """
        levels = [logging.NOTSET, logging.DEBUG, logging.INFO,
                  logging.WARNING, logging.ERROR, logging.CRITICAL]
        logging.basicConfig(level=levels[self.level],
                            format='%(asctime)s - %(message)s')

    def click(self, n):
        """
        点击屏幕中心，主要是快进对话框以及结算页面

        Parameters
        ----------
        n : 点击次数，每次间隔一秒
        """
        for i in range(n):
            self.device.click(self.x2, self.y2)
            time.sleep(1)
            logging.debug(f'调试信息：已点击{i+1}次')

    def ready(self):
        """
        第一次准备工作,获取闯关坐标与再次挑战坐标
        """
        _, [(self.x1, self.y1)] = self.mi.ocr_click(
            ['闯关'], picture=True, picture_name=f'{self.name}_chuangguan', shot_name=f'{self.name}_screenshot')
        logging.info(f'{self.name}闯关按钮坐标:({self.x1},{self.y1})')
        self.x2, self.y2 = [self.device.info['displayWidth']//2,
                            self.device.info['displayHeight']//2]  # 中心点
        for _ in range(10):
            time.sleep(1)  # 等待载入画面
        self.click(self.timer)  # 随关卡不同可以更改时间
        for i in range(self.wait):
            try:
                _, [(self.x3, self.y3)] = self.mi.ocr_click(
                    ['再次挑战'], at_once=True, picture=True, picture_name=f'{self.name}_tiaozhan', shot_name=f'{self.name}_screenshot')
                break
            except:
                self.click(1)
        logging.info(f'{self.name}再次挑战按钮坐标:({self.x3},{self.y3})')
        logging.info(f'提示:{self.name}已刷第1次，获得金币{self.jinbi}个')

    def go(self):
        """
        开始进入主循环
        """
        jinbi = self.jinbi
        for T in range(self.num-1):
            jinbi += self.jinbi
            for _ in range(self.wait):
                self.device.click(self.x3, self.y3)
                if self.mi.locatonScreen(f'{self.name}_chuangguan.png', shot_name=f'{self.name}_screenshot'):
                    break  # 判定是否回到闯关界面
            time.sleep(1)
            self.device.click(self.x1, self.y1)
            for _ in range(10):
                time.sleep(1)
            self.click(self.timer)
            for _ in range(self.wait):
                if self.mi.locatonScreen(f'{self.name}_tiaozhan.png', shot_name=f'{self.name}_screenshot'):
                    break  # 判定是否回到重新挑战界面
                self.click(1)
            time.sleep(0.5)
            logging.info(f'提示:{self.name}已刷第{T+2}次，获得金币{jinbi}个')
            self.device.click(self.x3, self.y3)



if __name__ == '__main__':
    print('程序开始运行')
    os.chdir(r'.\截图')   # 改变当前工作目录

    # 获取设备ID
    dev = subprocess.getstatusoutput("adb devices")[1]
    dev_ID = re.findall(r'\n(.*?)\t', dev)

    # 创建线程
    threadKings = []
    for i, ID in enumerate(dev_ID, start=1):
        d = u2.connect(ID)
        print(f'机名:phone{i}; ID:{ID}')
        phone = kings(name=f'phone{i}', device=d)
        phone.start()
        threadKings.append(phone)

    # 结束线程
    for single in threadKings:
        single.join()
    logging.info('程序已运行结束')
