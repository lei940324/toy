# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:49:57 2020

@author: lei
"""
import jieba
import re
from collections import Counter
import pandas as pd

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import imageio


"""1. 收集数据，这里导入初始文本"""
with open(r'数据\文本.txt', 'r', encoding='utf-8', errors="ignore") as file:
    data = file.read()

"""2. 数据清洗，使用正则"""
data = re.sub(r'【.*?】', '', data)  # 去除【】内容

"""3. 分词处理, 这里使用jieba分词"""
cut = " ".join(jieba.cut(data))

"""4. 去除停用词"""
stopwords = set()
with open(r'数据\停用词词典.txt', encoding='utf-8') as f:
    for line in f.readlines():
        stopwords.add(line.strip())
cut_not_stop = [i for i in jieba.cut(
    data) if i not in stopwords and len(i) >= 2]
out = dict(Counter(cut_not_stop))

"""5. 词云展示"""
trump_coloring = imageio.imread(r'数据\timg.jpg')
wordcloud = WordCloud(
    font_path='simhei.ttf', margin=5, width=3600,
    height=1600, background_color='white',
    scale=1,   # 图片像素
    stopwords=stopwords,         # 设置停用词
    max_words=10000, mask=trump_coloring,
    max_font_size=100, random_state=42).generate(cut)
plt.imshow(wordcloud, interpolation='bilinear')
wordcloud.to_file('output.png')
plt.axis('off')
plt.show()

"""6. 匹配情感词典"""
sen_dict = pd.read_excel(r'数据\情感词典.xlsx', index_col=0)
sen = {}
sen['词语'] = []
sen['频率'] = []
sen['分数'] = []
for (key, value) in out.items():
    try:
        sen['分数'].append(float(sen_dict.loc[key]))
        sen['词语'].append(key)
        sen['频率'].append(value)
    except:
        pass
df = pd.DataFrame(sen)
df.to_excel('output.xlsx')
