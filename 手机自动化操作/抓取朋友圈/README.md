# 介绍

实现朋友圈好友动态抓取，并生成词云展示

![image-20200408210520162](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/08/212610-630866.png)

# 要求

* python3.6+
  * 第三方库：`lxml`、`uiautomator2`、`pandas`、`wordcloud`、`jieba`、`matplotlib`

# 使用

使用python-uiautomator2操控手机，只支持安卓手机，具体准备工作可以参考：[手机自动化测试（准备篇）](https://blog.csdn.net/u013289615/article/details/90480832)。

不同手机控件信息不同，所以需要命令行输入`weditor`打开ATX界面，获取各控件信息，从而修改`info.py`代码内容

![image-20200408205651029](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/08/205656-366997.png)

![image-20200408210007805](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/08/210015-166410.png)

修改完，命令行输入运行

```python
python info.py
```

