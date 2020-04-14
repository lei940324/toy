<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/fxsjy/jieba"><img src="https://img.shields.io/badge/jieba-0.42.1-blue"></a>
<a href="https://github.com/pandas-dev/pandas"><img src="https://img.shields.io/badge/pandas-1.0.1-yellow"></a>
<a href="https://pypi.org/project/wordcloud/"><img src="https://img.shields.io/badge/wordcloud-1.6.0-blue"></a>
<a href="https://github.com/matplotlib/matplotlib"><img src="https://img.shields.io/badge/matplotlib-3.1.3-blue"></a>

## 介绍

将文本分词处理后，与情感词典匹配得分，得到情感极性分类与强度。

## 原理

单文本情绪指数构建示意图

<div align=center><img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/13/154213-136410.png" width="750"></div>

## 代码详解

主要分为以下步骤：

1. **收集数据**

   一般使用网络爬虫技术进行抓取，也可以人工手动收集

   ```python
   """1. 收集数据，这里导入初始文本"""
   with open(r'数据\文本.txt', 'r', encoding='utf-8', errors="ignore") as file:
       data = file.read()
   ```

   

2. **数据清洗**

   多用正则`re`或者`pandas`

   ```python
   """2. 数据清洗，使用正则"""
   data = re.sub(r'【.*?】', '', data)  # 去除【】内容
   ```

   

3. **中文分词**

   * [jieba](https://github.com/fxsjy/jieba)
   * [玻森中文语义开放平台](https://bosonnlp.com/)           

   ```python
   """3. 分词处理, 这里使用jieba分词"""
   cut = " ".join(jieba.cut(data))
   ```

   

4. **停用词典选取**

   中文语句中含有大量的停用词，若不进行剔除，最终得到的情绪分值会出现较大误差，因此根据网络现有资源，对“哈工大停用词词库”、“四川大学机器学习智能实验室停用词库”、“百度停用词表”等各种停用词表整理去重，共得到1598个停用词

   ```python
   """4. 去除停用词"""
   stopwords = set()
   with open(r'数据\停用词词典.txt', encoding='utf-8') as f:
       for line in f.readlines():
           stopwords.add(line.strip())
   cut_not_stop = [i for i in jieba.cut(
       data) if i not in stopwords and len(i) >= 2]
   out = dict(Counter(cut_not_stop))
   ```

   

5. **情绪词典选取**

   文本分析质量关键在于信息字典的选取，大连理工大学本体库在研究中有较为广泛的应用，该词典将词语进行不同极性划分，并进行强度打分。考虑到网络词汇具有浓厚的口语化特点，因此在大连理工大学本体库的基础上，添入汉语情感词极值表、BosonNLP极值表以作补充，若某一词语在多个词典内均有出现，则取其平均值作为该词语信息强度，下表给出了信息词典示例。

   |   词语   | 极性 | **信息强度** |
   | :------: | :--: | :----------: |
   | 国富民强 | 乐观 |    4.330     |
   | 求之不得 | 乐观 |    4.763     |
   |   看好   | 乐观 |    2.041     |
   |   厌恨   | 悲观 |    -5.000    |
   |   征税   | 悲观 |    -1.019    |
   |   争端   | 悲观 |    -0.678    |

6. **匹配分类**

   将去重后的词语，逐一与情绪词典进行匹配，若词语不存在则跳过

   ```python
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
   ```

> 详细代码请参看`main.py`