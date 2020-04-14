<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/lxml/lxml"><img src="https://img.shields.io/badge/lxml-4.5.0-red"></a>
<a href="https://github.com/openatx/uiautomator2"><img src="https://img.shields.io/badge/uiautomator2-2.7.1-brightgreen"></a>
<a href="https://github.com/pandas-dev/pandas"><img src="https://img.shields.io/badge/pandas-1.0.1-yellow"></a>
<a href="https://pypi.org/project/wordcloud/"><img src="https://img.shields.io/badge/wordcloud-1.6.0-blue"></a>
<a href="https://github.com/fxsjy/jieba"><img src="https://img.shields.io/badge/jieba-0.42.1-blue"></a>
<a href="https://github.com/matplotlib/matplotlib"><img src="https://img.shields.io/badge/matplotlib-3.1.3-blue"></a>

## 介绍

实现朋友圈好友动态抓取，并生成词云展示

<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/08/212610-630866.png" width="375">


## 使用

使用python-uiautomator2操控手机，只支持安卓手机，具体准备工作可以参考：[手机自动化测试（准备篇）](https://blog.csdn.net/u013289615/article/details/90480832)。

不同手机控件信息不同，所以需要命令行输入`weditor`打开ATX界面，获取各控件信息，从而修改`info.py`代码内容

![image-20200408205651029](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/08/205656-366997.png)

![image-20200408210007805](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/08/210015-166410.png)

修改完，命令行输入运行

```python
python info.py
```

