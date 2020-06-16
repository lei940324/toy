> 所有人都告诉你怎么活，只有自己没有搞清楚该如何活。相信自己，我们每个人都是主角❤️

<p align="center">
<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/125615-184630.png"  width=200/>
</p>
<h1 align="center">toy</h1>
<p align="center">
Guido van Rossum ❤️   人生苦短，我用 python
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


## <span id="head1"> 📃 介绍</span>

学习 python、matlab 时积累的笔记以及编写的小工具。

若发现图片无法加载，可以参考 [Github 的那些坑](https://github.com/lei940324/toy/blob/master/笔记/Git/Github的那些坑.md) 进行解决。

## <span id="head2"> 🔨 安装依赖库</span>

```shell
pip install -r requirements.txt
```

-----

## <span id="head3"> 💕 目录</span>

- [📣 玩具](#head4)
	- [小工具](#小工具)
	- [微信小应用](#head6)
	- [spider](#head7)
	- [手机自动化操作](#head8)
	- [其他](#head9)
- [📝 笔记](#head10)
	- [ Git](#head11)
	- [ python](#head12)
	- [其他](#其他)
- [ 📢 star 项目](#head13)
	- [规范指南](#head14)
	- [ 排名索引](#head15)
	- [ 新手入门](#head16)
	- [Chrome 插件](#head17)
	- [ 资源分享](#head18)
	- [ 爬虫](#head19)
	- [ 第三方库](#head20)
	- [ icons](#head21)
- [✨ Development Tool](#head22)
- [🐶 Author](#head23)
- [💌 捐赠](#head24)
- [📍 License](#head25)

----

## <span id="head4">📣 玩具</span>

### 小工具

* [论文统计性描述生成器](小工具/description)：统计量自动标星，GUI 界面操作
* [毕业论文格式调整器](小工具/ouc_thesis_format)：适用于中国海洋大学的毕业论文格式调整
* [pdf 去水印](小工具/pdf去水印)：将 pdf 转为图片，通过对比度进行处理  
* [文本倾斜矫正](小工具/文本倾斜矫正)：图片格式的倾斜文本矫正
* [word 套打](小工具/word套打)：信息存于 excel 中，批量生成 word 文件
* [群发邮件](小工具/群发邮件)：支持 QQ 邮箱；阿里云；网易邮箱

### <span id="head6"> 微信小应用</span>

基于`itchat`库开发的小应用

* [汇总微信消息](微信小应用/汇总微信消息)：汇总某些群体的信息
* [拼接微信好友头像](微信小应用/拼接微信好友头像)：获取微信好友头像，并进行拼接
* [分析微信好友信息](微信小应用/分析微信好友信息)：包括性别、地区分布分析

### <span id="head7"> spider</span>

网络爬虫的例子，项目地址：<https://github.com/lei940324/spider>

#### 基础入门

* [网络爬虫入门](https://github.com/lei940324/spider/blob/master/基础入门/网络爬虫——入门.md)：`requests`与`selenium`的单线程教程
* [网络爬虫总结](https://github.com/lei940324/spider/blob/master/基础入门/网络爬虫总结.md)：`requests`与`selenium`使用

#### 模板

* [单线程](https://github.com/lei940324/spider/blob/master/模板/GetUrl.py)：网址无响应，默认自动重连 5 次
* [多线程](https://github.com/lei940324/spider/blob/master/模板/ThreadGetUrl.py)：依赖于单线程模板

#### 微博

* [登陆微博](https://github.com/lei940324/spider/blob/master/微博/loginWeibo.py)：使用`requests`获取 cookie 信息
* [微博高级搜索](https://github.com/lei940324/spider/blob/master/微博/微博高级搜索)：通过微博自带的高级搜索功能进行数据爬取

#### selenium 应用

* [谷歌浏览器初始化设置](https://github.com/lei940324/spider/blob/master/selenium/chrome_init.py)：设定带有参数的谷歌浏览器
* [selenium 模板](https://github.com/lei940324/spider/blob/master/selenium/template.py)：依赖于谷歌浏览器初始化设置

### <span id="head8">手机自动化操作</span>

使用`uiautomator2`库进行手机操作，适用于`Android`手机

* [抓取朋友圈](手机自动化操作/抓取朋友圈)：模拟滑屏进行抓取，并将内容分词与词云展示
* [王者荣耀刷金币](手机自动化操作/王者荣耀刷金币)：通过图像识别增加稳定性
* [刷 66 阅读+趣头条](手机自动化操作/66阅读+趣头条.py)：刷完 66 阅读自动刷趣头条

### <span id="head9"> 其他</span>

* [econometrics](https://github.com/lei940324/econometrics)：陈强高级计量经济学笔记
* [Quantile](https://github.com/lei940324/Quantile)：介绍分位数回归，包括分位数 Granger 因果检验、QVAR 及脉冲响应函数  
* [情感分析](情感分析)：将文本分词处理后，与情感词典匹配得分，得到情感极性分类与强度。

## <span id="head10"> 📝 笔记</span>

### <span id="head11"> Git</span>

* [Git 入门](笔记/Git/Git入门.md)：学会最简单的 Git 操作
* [Github 的那些坑](笔记/Git/Github的那些坑.md)：使用 Github 时遇到的坑

### <span id="head12"> python </span>

* [编程之道](笔记/python/编程之道.md)：代码风格、编程之谈、经验分享
* [python 基础](笔记/python/python基础.md)：字典、列表、正则表达式等
* [pandas 总结](笔记/python/pandas总结.md)：`pandas` 基本与进阶操作
* [xpath 入门](https://nbviewer.jupyter.org/github/lei940324/toy/blob/master/笔记/python/xpath.ipynb)：`xpath` 基本语法与常见问题
* [数据库基础](笔记/python/SQL基本语法.md)：`sql` 基本语法与 `mysql` 命令
* [搭建个人网站](笔记/python/搭建网站/搭建个人网站.md)：使用阿里云服务器（Windows Server）+ `Django` + `apache`
* [IDE 优劣对比](笔记/python/IDE优劣对比.md)：对比 python 常见 IDE，包括 spyder、PyCharm、Jupyter、Vscode。
* [第三方库文档](笔记/python/第三方库文档.md)：常用第三方库的文档教程网站

### 其他

* [termux](笔记/termux.md)：Termux 是一个 Android 下一个高级的终端模拟器,开源且不需要 root，支持 apt 管理软件包，十分方便安装软件包，完美支持 Python、 PHP、 Ruby、 Nodejs、 MySQL等。随着智能设备的普及和性能的不断提升，如今的手机、平板等的硬件标准已达到了初级桌面计算机的硬件标准，用心去打造 DIY 的话完全可以把手机变成一个强大的极客工具。
* [玩转阿里云](笔记/玩转阿里云.md)：介绍阿里云服务器 ECS、云存储 OSS、域名、CDN、邮件推送等服务
* [程序员必知必会的英语单词](笔记/程序员必知必会的英语单词.md)：平时看文档积累的英语单词

&emsp;

## <span id="head13"> 📢 star 项目</span>

### <span id="head14">规范指南</span>

* [document-style-guide](https://github.com/ruanyf/document-style-guide)：中文技术文档的写作规范
* [zh-google-styleguide](https://github.com/zh-google-styleguide/zh-google-styleguide)：Google 开源项目风格指南 (中文版)
* [one-python-craftsman](https://github.com/piglei/one-python-craftsman)：来自一位 Pythonista 的编程经验分享，内容涵盖编码技巧、最佳实践与思维模式等方面。
* [Python-Guide-CN](https://github.com/Prodesire/Python-Guide-CN)：Python 最佳实践指南。 The Chinese translation of "Hitchhiker's Guide to Python". 作者是 requests 库的作者
* [Standard Readme](https://github.com/RichardLitt/standard-readme)：A standard style for README files

### <span id="head15"> 排名索引</span>

* [GitHub-Chinese-Top-Charts](https://github.com/kon9chunkit/GitHub-Chinese-Top-Charts)：GitHub 中文排行榜，帮助你发现高分优秀中文项目、更高效地吸收国人的优秀经验成果；榜单每周更新一次
* [HelloGitHub](https://github.com/521xueweihan/HelloGitHub)：分享 GitHub 上有趣、入门级的开源项目

### <span id="head16"> 新手入门</span>

* [python-small-examples](https://github.com/jackzhenguo/python-small-examples)：告别枯燥，60 秒学会一个 Python 小例子
* [Python-100-Days](https://github.com/jackfrued/Python-100-Days)：Python - 100 天从新手到大师

### <span id="head17">Chrome 插件</span>

* [ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes)：谷粒-Chrome 插件英雄榜, 为优秀的 Chrome 插件写一本中文说明书, 让 Chrome 插件英雄们造福人类~
* [GitZip for Github](https://github.com/GitZip/chrome-extension)：可以快速从 GitHub 上快速下载文件或目录
* [Octotree](https://github.com/ovity/octotree)：  快速查看 GitHub 上项目结构

### <span id="head18"> 资源分享</span>

* [practical-programming-books](https://github.com/EZLippi/practical-programming-books)：这里收录比较实用的计算机相关技术书籍，可以在短期之内入门的简单实用教程、一些技术网站以及一些写的比较好的博文
* [awesome-python-applications](https://github.com/mahmoud/awesome-python-applications)：Free software that works great, and also happens to be open-source Python.
* [Student-resources](https://github.com/ivmm/Student-resources)：介绍的是利用学生身份可以享受到的相关学生优惠权益，但也希望各位享受权利的同时不要忘记自己的义务，不要售卖、转手自己的学生优惠资格，使得其他同学无法受益。
* [awesome-python-cn](https://github.com/jobbole/awesome-python-cn)：Python 资源大全中文版，包括：Web 框架、网络爬虫、模板引擎、数据库、数据可视化、图片处理等，由伯乐在线持续更新。
* [Baidu-XunleiVIP](https://github.com/VIP-Share/Baidu-XunleiVIP)：百度网盘超级会员，迅雷会员、爱奇艺会员账号每日分享，还有优酷，腾讯，芒果等 VIP。AND。百度网盘(百度云)不限速工具分享。
* [free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN)：免费的计算机编程类中文书籍

### <span id="head19"> 爬虫</span>

* [PythonSpiderNotes](https://github.com/lining0806/PythonSpiderNotes)：Python 入门网络爬虫之精华版
* [awesome-python-login-model](https://github.com/Kr1s77/awesome-python-login-model)：python 模拟登陆一些大型网站，还有一些简单的爬虫

### <span id="head20"> 第三方库</span>

* [pandas-tutorial](https://github.com/hangsz/pandas-tutorial)：适合初级到中级晋升者的 pandas 教程
* [joyful-pandas](https://github.com/datawhalechina/joyful-pandas)：Pandas 教程，完整梳理 Pandas 的主线内容，杜绝浅尝辄止，保证涉及每个部分的核心概念和函数。
* [opencv_tutorials](https://github.com/JimmyHHua/opencv_tutorials)：Opencv4.0 with python（包含中文版）
* [OpenCV-Python-Tutorial](https://github.com/ex2tron/OpenCV-Python-Tutorial)：OpenCV-Python 图像处理教程
* [PyTorchDocs](https://github.com/fendouai/PyTorchDocs)：PyTorch 官方中文教程，包含 60 分钟快速入门教程，强化教程，计算机视觉，自然语言处理，生成对抗网络，强化学习。
* [PyQt](https://github.com/PyQt5/PyQt)：PyQt Examples（PyQt 各种测试和例子） PyQt4 PyQt5
* [PyQt5-Chinese-tutorial](https://github.com/maicss/PyQt5-Chinese-tutorial)：PyQt5 中文教程，这个教程比较好的地方是，能讲解每一段代码的含义。虽然 PyQt 的函数命名已经非常语义化了，但是对于新手来说，有这一步还是更好的。
* [wxpy](https://github.com/youfou/wxpy)：微信机器人 / 可能是最优雅的微信个人号 API ✨✨
* [uiautomator2](https://github.com/openatx/uiautomator2)：Android Uiautomator2 Python Wrapper，Android 手机自动化控制，

### <span id="head21"> icons</span>

* [bytesize-icons](https://github.com/danklammer/bytesize-icons)：Tiny style-controlled SVG iconset (101 icons, 12kb)
* [SuperTinyIcons](https://github.com/edent/SuperTinyIcons)：nder 1KB each! Super Tiny Icons are miniscule SVG versions of your favourite website and app logos
* [feather](https://github.com/feathericons/feather)：Simply beautiful open source icons

&emsp;

## <span id="head22">✨ Development Tool</span>

|       工具名       |     功能      |                           图标 icon                           |                           官网下载                           |
| :----------------: | :-----------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|     Qt Creator     | GUI 界面可视化 | <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202003/31/182029-164220.png" width="50" align="absmiddle"> | [click](http://download.qt.io/official_releases/qtcreator/)  |
|      PyCharm       |  代码编辑器   | <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202003/31/182340-937174.png" width="50" align="absmiddle"> | [click](https://www.jetbrains.com/pycharm/download/#section=windows) |
|      anaconda      |  代码编辑器   | <img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200504130345.png" width=50/> |    [click](https://www.anaconda.com/products/individual)     |
| Visual Studio Code |  代码阅读器   | <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/14/193013-466582.png" width="50" align="absmiddle"> |           [click](https://code.visualstudio.com/)            |

&emsp;

## <span id="head23">🐶 Author</span>

中国海洋大学经济学研究生，热爱 python，喜欢编一些小玩意，有兴趣可以加我微信一起探讨。

<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/181334-564739.png"  width=200 />


## <span id="head24">💌 捐赠</span>

如果觉得项目能帮助到您，请考虑请作者喝一杯咖啡 😄

<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/183545-561589.png"  width=200 />&#8195;<img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/12/183831-321249.png"  width=200 />

## <span id="head25">📍 License</span>

[MIT](https://github.com/lei940324/toy/blob/master/LICENSE) © 热心市民石头