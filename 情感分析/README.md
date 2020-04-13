<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/fxsjy/jieba"><img src="https://img.shields.io/badge/jieba-0.42.1-blue"></a>


# 原理

单文本情绪指数构建示意图

<div align=center><img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/13/152730-390512.png" width="450"></div>

主要分为几大步骤：

1. 收集数据：一般使用网络爬虫技术进行抓取，也可以人工手动收集
2. 数据清洗：多用正则`re`或者`pandas`
3. 中文分词：[jieba](https://github.com/fxsjy/jieba)或者[玻森中文语义开放平台](https://bosonnlp.com/)
4. 停用词典选取
5. 情绪词典选取
6. 匹配分类