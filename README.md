> 所有人都告诉你怎么活，只有自己没有搞清楚该如何活。相信自己，我们每个人都是主角❤️

<p align="center">
<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/125615-184630.png"  width=200/>
</p>
<h1 align="center">toy</h1>
<p align="center">
<em>Python ❤️    献给我亲爱的女朋友——如</em>
</p>
<p align="center">
<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/python-openxml/python-docx"><img src="https://img.shields.io/badge/python--docx-0.2.4-orange"></a>
<a href="https://github.com/littlecodersh/ItChat"><img src="https://img.shields.io/badge/itchat-1.3.10-blue"></a>
<a href="https://github.com/lxml/lxml"><img src="https://img.shields.io/badge/lxml-4.5.0-red"></a>
<a href="https://github.com/matplotlib/matplotlib"><img src="https://img.shields.io/badge/matplotlib-3.1.3-blue"></a>
</p>
<p align="center">
<a href="https://github.com/numpy/numpy"><img src="https://img.shields.io/badge/numpy-1.18.1-blue"></a>
<a href="https://github.com/pandas-dev/pandas"><img src="https://img.shields.io/badge/pandas-1.0.1-yellow"></a>
<a href="https://github.com/pyecharts/pyecharts"><img src="https://img.shields.io/badge/pyecharts-1.7.1-orange"></a>
<a href="https://pypi.org/project/PyQt5/"><img src="https://img.shields.io/badge/pyqt5-5.10-orange"></a>
<a href="https://github.com/psf/requests"><img src="https://img.shields.io/badge/requests-2.22.0-yellow"></a>
</p>
<p align="center">
<a href="https://github.com/scipy/scipy"><img src="https://img.shields.io/badge/scipy-1.4.1-brightgreen"></a>
<a href="https://github.com/SeleniumHQ/selenium"><img src="https://img.shields.io/badge/selenium-3.141.0-lightgrey"></a>
<a href="https://github.com/statsmodels/statsmodels"><img src="https://img.shields.io/badge/statsmodels-0.11.0-red"></a>
<a href="https://github.com/sympy/sympy"><img src="https://img.shields.io/badge/sympy-1.5.1-lightgrey"></a>
<a href="https://github.com/openatx/uiautomator2"><img src="https://img.shields.io/badge/uiautomator2-2.7.1-brightgreen"></a>
</p>

## <span id="head1"> 📃介绍</span>

学习python时积累的笔记以及编写的小工具。

## <span id="head2"> 🔨安装依赖库</span>

```shell
pip install -r requirements.txt
```

## 目录

- [📣 玩具](#head3)
  - [ 小工具](#head4)
  - [ 微信小应用](#head5)
  - [ spider](#head6)
  - [ 手机自动化操作](#head7)
  - [ 其他](#head8)
- [ 📝笔记](#head9)
- [ 📢其他优秀项目](#head10)
  - [ 热门](#head11)
  - [ 小众](#head12)
- [ 🔧浏览器插件](#head13)

## <span id="head3">📣 玩具</span>

### <span id="head4"> 小工具</span>

|        项目名        |               功能                |                         Introduction                         |
| ------------------ | ------------------------------- | :----------------------------------------------------------: |
| 论文统计性描述生成器 |    统计量自动标星，GUI界面操作    | [click](https://github.com/lei940324/toy/tree/master/小工具/description) |
|  毕业论文格式调整器  |        适用于中国海洋大学         | [click](https://github.com/lei940324/toy/tree/master/小工具/ouc_thesis_format) |
|      pdf去水印       | 将pdf转为图片，通过对比度进行处理 | [click](https://github.com/lei940324/toy/tree/master/小工具/pdf%E5%8E%BB%E6%B0%B4%E5%8D%B0) |
|     文本倾斜矫正     |      图片格式的倾斜文本矫正       | [click](https://github.com/lei940324/toy/tree/master/小工具/文本倾斜矫正) |
|       word套打       | 信息存于excel中，批量生成word文件 | [click](https://github.com/lei940324/toy/tree/master/小工具/word套打) |

### <span id="head5"> 微信小应用</span>

基于`itchat`库开发的小应用

|      项目名      |             功能             |                         Introduction                         |
| -------------- | -------------------------- | :----------------------------------------------------------: |
|   汇总微信消息   |      汇总某些群体的信息      | [click](https://github.com/lei940324/toy/tree/master/微信小应用/汇总微信消息) |
| 拼接微信好友头像 | 获取微信好友头像，并进行拼接 | [click](https://github.com/lei940324/toy/tree/master/微信小应用/拼接微信好友头像) |
| 分析微信好友信息 |    包括性别、地区分布分析    | [click](https://github.com/lei940324/toy/tree/master/微信小应用/分析微信好友信息) |

### <span id="head6"> spider</span>

网络爬虫的例子

|        项目名        |                  功能                  |                         Introduction                         |
| ------------------ | ------------------------------------ | :----------------------------------------------------------: |
|     网络爬虫入门     |   `requests`与`selenium`的单线程教程   | [click](https://github.com/lei940324/spider/blob/master/网络爬虫——入门.md) |
|       **模板**       |                                        |                                                              |
|        单线程        |      网址无响应，默认自动重连5次       | [click](https://github.com/lei940324/spider/blob/master/模板/GetUrl.py) |
|        多线程        |            依赖于单线程模板            | [click](https://github.com/lei940324/spider/blob/master/模板/ThreadGetUrl.py) |
|       **微博**       |                                        |                                                              |
|       登陆微博       |      使用`requests`获取cookie信息      | [click](https://github.com/lei940324/spider/blob/master/%E5%BE%AE%E5%8D%9A/loginWeibo.py) |
|     微博高级搜索     | 通过微博自带的高级搜索功能进行数据爬取 | [click](https://github.com/lei940324/spider/tree/master/微博/微博高级搜索) |
|   **selenium应用**   |                                        |                                                              |
| 谷歌浏览器初始化设置 |        设定带有参数的谷歌浏览器        | [click](https://github.com/lei940324/spider/blob/master/selenium/chrome_init.py) |
|     selenium模板     |       依赖于谷歌浏览器初始化设置       | [click](https://github.com/lei940324/spider/blob/master/selenium/template.py) |



### <span id="head7"> 手机自动化操作</span>

使用`uiautomator2`库进行手机操作，适用于`Android`手机

|     项目名      |                   功能                   |                         Introduction                         |
| ------------- | -------------------------------------- | :----------------------------------------------------------: |
|   抓取朋友圈    | 模拟滑屏进行抓取，并将内容分词与词云展示 | [click](https://github.com/lei940324/toy/tree/master/手机自动化操作/抓取朋友圈) |
| 王者荣耀刷金币  |          通过图像识别增加稳定性          | [click](https://github.com/lei940324/toy/tree/master/手机自动化操作/王者荣耀刷金币) |
| 刷66阅读+趣头条 |          刷完66阅读自动刷趣头条          | [click](https://github.com/lei940324/toy/tree/master/手机自动化操作/66阅读+趣头条.py) |

### <span id="head8"> 其他</span>

|  项目名  |                             功能                             |                         Introduction                         |
| ------ | ---------------------------------------------------------- | :----------------------------------------------------------: |
| Quantile | 介绍分位数回归，包括分位数Granger因果检验、QVAR及脉冲响应函数 |        [click](https://github.com/lei940324/Quantile)        |
| 情感分析 | 将文本分词处理后，与情感词典匹配得分，得到情感极性分类与强度。 | [click](https://github.com/lei940324/toy/tree/master/情感分析) |



## <span id="head9"> 📝笔记</span>

|    笔记名    |            简介            |                         Introduction                         |
| ---------- | ------------------------ | :----------------------------------------------------------: |
|  python基础  |  字典、列表、正则表达式等  | [click](https://github.com/lei940324/toy/blob/master/笔记/python基础.md) |
| `pandas`总结 |   `pandas`基本与进阶操作   | [click](https://github.com/lei940324/toy/blob/master/笔记/pandas总结.md) |
|   网络爬虫   | `requests`与`selenium`使用 | [click](https://github.com/lei940324/toy/blob/master/笔记/网络爬虫.md) |
|   `xpath`    | `xpath`基本语法与常见问题  | [click](https://nbviewer.jupyter.org/github/lei940324/toy/blob/master/%E7%AC%94%E8%AE%B0/xpath.ipynb) |
|  数据库基础  | `sql`基本语法与`mysql`命令 | [click](https://github.com/lei940324/toy/blob/master/笔记/SQL基本语法.md) |



## <span id="head10"> 📢其他优秀项目</span>

### <span id="head11"> 热门</span>


|          项目名           |                 功能                 |                         Introduction                         |
| ----------------------- | ---------------------------------- | :----------------------------------------------------------: |
|      Standard Readme      |  A standard style for README files   |   [click](https://github.com/RichardLitt/standard-readme)    |
|   python-small-examples   |     Python有趣的小例子一网打尽。     | [click](https://github.com/jackzhenguo/python-small-examples) |
|           Games           |  Some games created by python code.  |       [click](https://github.com/CharlesPikachu/Games)       |
|        HelloGitHub        | 分享 GitHub 上有趣、入门级的开源项目 |     [click](https://github.com/521xueweihan/HelloGitHub)     |
| GitHub-Chinese-Top-Charts |           GitHub中文排行榜           | [click](https://github.com/kon9chunkit/GitHub-Chinese-Top-Charts) |
| Python-100-Days | Python - 100天从新手到大师 | [click](https://github.com/jackfrued/Python-100-Days) |

### <span id="head12"> 小众</span>

|          项目名          |            功能             |                         Introduction                         |
| ---------------------- | ------------------------- | :----------------------------------------------------------: |
| spider-BaiduIndex-master |        百度指数爬虫         | [click](https://github.com/longxiaofei/spider-BaiduIndex/tree/master) |
|  typora-plugins-win-img  | windows下typora自动上传图片 |  [click](https://github.com/Thobian/typora-plugins-win-img)  |
|          GitToc          |     Readme自动生成目录      | [click](https://github.com/Holy-Shine/GitToc/blob/master/README_CN.md) |



## <span id="head13"> 🔧浏览器插件</span>

| 插件名            | 功能                                   |                    Introduction                     |
| ----------------- | -------------------------------------- | :-------------------------------------------------: |
| GitZip for Github | 可以快速从 GitHub 上快速下载文件或目录 | [click](https://github.com/GitZip/chrome-extension) |
| Octotree          | 快速查看GitHub 上项目结构              |     [click](https://github.com/ovity/octotree)      |



## <span id="head14">✨Development Tool</span>

|       工具名       |     功能      |                           图标icon                           |                           官网下载                           |
| :----------------: | :-----------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|     Qt Creator     | GUI界面可视化 | <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202003/31/182029-164220.png" width="50" align="absmiddle"> | [click](http://download.qt.io/official_releases/qtcreator/)  |
|      PyCharm       |  代码编辑器   | <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202003/31/182340-937174.png" width="50" align="absmiddle"> | [click](https://www.jetbrains.com/pycharm/download/#section=windows) |
| Visual Studio Code |  代码阅读器   | <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/14/193013-466582.png" width="50" align="absmiddle"> |           [click](https://code.visualstudio.com/)            |



## <span id="head15"> 🐶Author</span>

中国海洋大学经济学研究生，热爱python，喜欢编一些小玩意，有兴趣可以加我微信一起探讨。

<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/181334-564739.png"  width=200 />


## <span id="head16">💌 捐赠</span>

如果觉得项目能帮助到您，请考虑请作者喝一杯咖啡 😄

<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/183545-561589.png"  width=200 />&#8195;<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/183831-321249.png"  width=200 />