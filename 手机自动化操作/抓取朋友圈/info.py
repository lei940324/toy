# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:20:49 2020

@author: Administrator
"""


from appmi import dxpath
import uiautomator2 as u2
import time
import pandas as pd

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import imageio


class spider():

    def __init__(self):
        self.d = u2.connect()
        print(self.d.info)
        self.mi = dxpath(self.d)
        self.data()

    def data(self):
        """
        创建抓取数据容器

        """
        self.names = []      # 网名
        self.comments = []   # 数据内容

    def load(self):
        """
        载入界面

        """
        self.d.session("com.tencent.mm")   # 启动微信
        self.mi.click('//*[@text="发现"]/preceding-sibling::node')   # 点击发现
        self.mi.click('//*[@text="朋友圈"]')   # 点击朋友圈
        self.d(resourceId="com.tencent.mm:id/en0").exists()   # 判断朋友圈信息是否加载
        print('朋友圈界面载入成功')
        time.sleep(2)

    def run(self, num):
        """
        开始循环抓取

        num : 抓取个数

        """
        while len(self.names) < num:
            for t in self.mi.dxpath('//*[@resource-id="com.tencent.mm:id/fiw"]'):
                try:
                    comment = self.mi.dxpath_text(
                        t, './/*[@resource-id="com.tencent.mm:id/b8c"]')
                    name = self.mi.dxpath_text(
                        t, './/*[@resource-id="com.tencent.mm:id/e0n"]')

                    # 不能是广告
                    if comment not in self.comments and not self.mi.dxpath_exist(t, './/*[@resource-id="com.tencent.mm:id/e2"]'):
                        print("抓取到{}朋友圈数据：\n{}".format
                              (name, comment))
                        self.comments.append(comment)
                        self.names.append(name)
                        print('*'*25+str(len(self.names)))
                except:
                    pass
            # 滑动
            self.d.swipe(300, 800, 300, 300, 0.1)

    def save(self):
        """
        保存数据到excel
        """
        self.df = pd.DataFrame()
        self.df['姓名'] = self.names
        self.df['内容'] = self.comments
        self.df.to_excel('output.xlsx', index=False)

    def get_wordcloud(self):
        word=''
        for cut in self.comments:
            mytext_cut =' '.join(list(jieba.cut(cut)))
            word +=' '+mytext_cut
        trump_coloring = imageio.imread('weixin.jpg')
        wordcloud = WordCloud(
        font_path='simhei.ttf', margin=5, width=3600, 
        height=1600, background_color='white',
        scale=16,
        max_words=10000, mask=trump_coloring, 
        max_font_size=100, random_state=42).generate(word)
        plt.imshow(wordcloud, interpolation='bilinear')
        wordcloud.to_file('output.png')
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    print('程序开始运行')
    exc = spider()
    exc.load()
    exc.run(20)
    exc.save()
    exc.get_wordcloud()
    print('程序运行结束')
