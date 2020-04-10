# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:04:19 2019

@author: Administrator
"""
from lxml import etree
import re
import time
import uiautomator2 as u2


class dxpath():
    """
    增强uiautomator2功能，增加图像识别点击
    """

    def connect(self, ID=None):
        """
        连接手机

        Parameters
        ----------
        ID : 手机设备名

        """
        self.d = u2.connect(ID)

    def dxpath(self, arg):
        """
        通过xpath获得etree.module，可以继续使用xpath定位，适用于从某一区域继续检索  

        Parameters
        ----------
        arg : xpath路径

        Returns：xpath类型，可继续使用xpath搜寻

        """
        xml_content = self.d.dump_hierarchy()
        root = etree.fromstring(xml_content.encode('utf-8'))
        return root.xpath(arg)

    def xpaths(self, arg):
        """
        通过xpath获得XPathSelector类型，适用于从某一区域获取文本  

        Parameters
        ----------
        arg : xpath路径

        Returns：xpath类型，可继续使用xpath搜寻

        """
        xml_content = self.d.dump_hierarchy()
        root = etree.fromstring(xml_content.encode('utf-8'))
        out = []
        for t in root.xpath(arg):
            out.append(XPathSelector(t))
        return out

    def exist(self, arg):
        return self.dxpath(arg)

    def wait(self, arg, timeout=10, always=False):
        """
        默认等待十秒,否则报错,always设定True时,一直进行等待直到出现为止

        Parameters
        ----------
        arg : xpath路径
        timeout : 响应时间
        always : False表示只判断一次，若不存在则报错

        Returns
        -------
        data : 控件的xpath类型

        """
        deadline = time.time() + timeout
        while time.time() < deadline or always:
            data = self.dxpath(arg)
            if data:
                return data
            time.sleep(0.1)
        raise Exception("未找到控件")

    def not_exists(self, arg):
        """
        控件不存在时退出循环
        """
        while True:
            data = self.dxpath(arg)
            if not data:
                return data
            time.sleep(0.1)

    def get_text(self, arg, One=True):
        args = '{}/@text'.format(arg)
        text = []
        for txt in self.dxpath(args):
            text.append(str(txt))
        if One:
            return text[0]
        else:
            return text

    def center(self, arg):
        bounds = '{}/@bounds'.format(arg)
        try:
            coord = str(self.dxpath(bounds)[0])
            lx, ly, rx, ry = map(int, re.findall(r"\d+", coord))
            return lx, ly, rx, ry
        except:
            raise Exception("未找到控件")

    def click(self, arg, timeout=10, at_once=False, set_x=0, set_y=0):
        """
        增强click功能，添加保存图片功能

        Parameters
        ----------
        arg : xpath路径
        timeout : 响应时间
        at_once : True表示只判别一次
        set_x : x坐标调整
        set_y : y坐标调整

        Returns
        -------
        x : 点击点的x坐标
        y : 点击点的y坐标

        """
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                lx, ly, rx, ry = self.center(arg)
                x, y = (lx + rx) // 2, (ly + ry) // 2
                x = set_x+x
                y = set_y+y
                self.d.click(x, y)
                return x, y
            except:
                if at_once:
                    raise Exception("未找到控件")
                else:
                    time.sleep(0.1)
        raise Exception("未找到控件")

class XPathSelector():
    def __init__(self, obj):
        self.obj = obj

    def text(self, arg, One=True):
        """
        获取控件文本

        Parameters
        ----------
        arg : xpath路径
        One : True表示获取第一个文本

        Returns：控件文本

        """
        args = '{}/@text'.format(arg)
        text = []
        for txt in self.obj.xpath(args):
            text.append(str(txt))
        if One:
            return text[0]
        else:
            return text

    def exist(self, arg):
        """
        判断控件是否存在，存在则返回控件的xpath类型

        Parameters
        ----------
        arg : xpath路径

        """
        return self.obj.xpath(arg)

    def center(self, arg):
        """
        获取控件坐标

        Parameters
        ----------
        arg : xpath路径

        Returns：控件坐标

        """
        bounds = '{}/@bounds'.format(arg)
        try:
            coord = str(self.obj.xpath(bounds)[0])
            lx, ly, rx, ry = map(int, re.findall(r"\d+", coord))
            return lx, ly, rx, ry
        except:
            raise Exception("未找到控件")

    def click(self, arg, timeout=10, at_once=False, set_x=0, set_y=0,
              picture=False, picture_name='crop'):
        """
        增强click功能，添加保存图片功能

        Parameters
        ----------
        arg : xpath路径
        timeout : 响应时间
        at_once : True表示只判别一次
        set_x : x坐标调整
        set_y : y坐标调整
        picture : True表示保存图像
        picture_name : 保存图片名

        Returns
        -------
        x : 点击点的x坐标
        y : 点击点的y坐标

        """
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                lx, ly, rx, ry = self.center(arg)
                x, y = (lx + rx) // 2, (ly + ry) // 2
                x = set_x+x
                y = set_y+y
                mi.d.click(x, y)
                if picture:
                    catIm = Image.open('screenshot.png')
                    croppedIm = catIm.crop((lx+set_x, ly+set_y,
                                            lx+set_x+rx, ly+set_y+ry))
                    croppedIm.save('%s.png' % picture_name)
                return x, y
            except:
                if at_once:
                    raise Exception("未找到控件")
                else:
                    time.sleep(0.1)
        raise Exception("未找到控件")


mi = dxpath()   # 创建实例
