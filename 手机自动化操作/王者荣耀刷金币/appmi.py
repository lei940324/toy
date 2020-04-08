# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:04:19 2019

@author: Administrator
"""
from PIL import Image
from lxml import etree
import re
import os
import time
import tencentOCR
import aircv as ac
import threading
import uiautomator2 as u2


class dxpath():
    def __init__(self, d):
        self.d = d

    def code(self, file='dump_hierarchy.xml',
             open_file=True):
        """
        查看xml源码

        Parameters
        ----------
        file : xml文件保存路径
        open_file : True表示保存后打开该文件

        Returns
        -------
        xml_content : xml源码内容

        """
        xml_content = self.d.dump_hierarchy()
        with open(file, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        if open_file:
            threadObj = threading.Thread(target=os.system, args=[file])
            threadObj.start()
        return xml_content

    def dxpath(self, arg):
        """
        通过xpath获得etree.module，可以继续使用xpath定位，适用于从某一区域继续检索  

        Parameters
        ----------
        arg : xpath路径

        Returns：xpath类型，可继续使用xpath搜寻

        """
        #
        xml_content = self.d.dump_hierarchy()
        root = etree.fromstring(xml_content.encode('utf-8'))
        return root.xpath(arg)

    def dxpath_text(self, t, arg, One=True):
        """
        获取控件文本

        Parameters
        ----------
        t : dxpath迭代的对象
        arg : xpath路径
        One : True表示获取第一个文本

        Returns：控件文本

        """

        args = '{}/@text'.format(arg)
        text = []
        for txt in t.xpath(args):
            text.append(str(txt))
        if One:
            return text[0]
        else:
            return text

    def dxpath_exist(self, t, arg):
        """
        判断控件是否存在，存在则返回控件的xpath类型

        Parameters
        ----------
        t : 控件的xpath类型
        arg : xpath路径

        """
        return t.xpath(arg)

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

    def center(self, arg, t=None):
        bounds = '{}/@bounds'.format(arg)
        try:
            if t is not None:
                coord = str(t.xpath(bounds)[0])
            else:
                coord = str(self.dxpath(bounds)[0])
            lx, ly, rx, ry = map(int, re.findall(r"\d+", coord))
            return lx, ly, rx, ry
        except:
            raise Exception("未找到控件")

    def click(self, arg, timeout=10, at_once=False, set_x=0, set_y=0,
              picture=False, picture_name='crop', t=None):
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
        t : dxpath迭代的对象

        Returns
        -------
        x : 点击点的x坐标
        y : 点击点的y坐标

        """

        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                lx, ly, rx, ry = self.center(arg, t)
                x, y = (lx + rx) // 2, (ly + ry) // 2
                x = set_x+x
                y = set_y+y
                self.d.click(x, y)
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

    def ocr(self):
        self.d.screenshot('screenshot.png')
        connect = tencentOCR.TencentOCR('screenshot.png')
        ocr = {}
        for key in connect:
            lx, ly, rx, ry = connect[key]['itemcoord'].values()
            x, y = lx + rx//2, ly + ry // 2
            ocr[key] = (x, y)
        return ocr

    def ocr_click(self, char=None, timeout=10, at_once=False, repetition=1,
                  set_x=0, set_y=0, picture=False, picture_name='crop', shot_name='screenshot'):
        """
        通过图像识别位置，进行点击

        Parameters
        ----------
        char : 识别的字符串
        timeout : 响应时间
        at_once : True表示只判别一次
        repetition : 重复点击次数
        set_x : x坐标调整
        set_y : y坐标调整
        picture : True表示保存图像
        picture_name : 保存图片名
        shot_name : 截图名

        Returns
        -------
        connect : 腾讯OCR发回的数据
        succes s：为点击坐标

        """
        deadline = time.time() + timeout
        while time.time() < deadline:
            success = []
            self.d.screenshot(f'{shot_name}.png')
            connect = tencentOCR.TencentOCR(f'{shot_name}.png')
            for single in char:
                try:
                    # 优先精确查找
                    lx, ly, rx, ry = connect[single]['itemcoord'].values()
                except:
                    for key in connect:  # 精确查找找不到的话查看是否包含在里面
                        if single in key:
                            lx, ly, rx, ry = connect[key]['itemcoord'].values()
                            break
                try:
                    x, y = set_x + lx + rx//2, set_y + ly + ry // 2
                except:
                    continue
                for i in range(repetition):
                    if i != 0:
                        time.sleep(0.3)
                    self.d.click(x, y)
                success.append((x, y))
                if picture:
                    catIm = Image.open(f'{shot_name}.png')
                    croppedIm = catIm.crop((lx+set_x, ly+set_y,
                                            lx+set_x+rx, ly+set_y+ry))
                    croppedIm.save('%s.png' % picture_name)
                if len(char) > 1:
                    time.sleep(0.3)
            if success or at_once:
                break
        if not success:
            raise Exception("未找到控件")
        return connect, success

    def locatonScreen(self, imgobj, confidence=0.9, click=True, imsrc=None, shot_name='screenshot'):
        """
        判断图像是否匹配当前屏幕

        Parameters
        ----------
        imgobj : 待查找图片
        confidence : 置信度
        click : 是否进行点击
        imsrc : 原始图像
        shot_name : 手机截屏

        Returns
        -------
        match_result : 匹配结果

        """
        if not imsrc:
            imsrc = ac.imread(self.d.screenshot(f'{shot_name}.png'))
        else:
            imsrc = ac.imread(imsrc)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj, confidence)
        if match_result is not None:
            match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
            if click:
                x, y = match_result['result']
                self.d.click(x, y)
        return match_result


def main():
    # =============================================================================
    #     xml = mi.code()   #获取底层渲染xml文件
    #     ocr =mi.ocr()
    #     mi.click('//*[@text="发现"]/preceding-sibling::node')
    #     connect , [(x,y)] = mi.ocr_click([x for x in '15806527017'])
    #     connect , [(x,y)] = mi.ocr_click(['QQ浏览器'],picture=True)
    #     a=mi.locatonScreen(r'C:\Users\Administrator\Desktop\1.jpg')
    # =============================================================================
    connect, success = mi.ocr_click(['QQ浏览器'], picture=True)


if __name__ == '__main__':
    os.chdir(r'C:\Users\Administrator\Desktop')
    d = u2.connect()
    mi = dxpath(d)
    main()
