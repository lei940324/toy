<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/pandas-dev/pandas"><img src="https://img.shields.io/badge/pandas-1.0.1-yellow"></a>
<a href="https://github.com/scipy/scipy"><img src="https://img.shields.io/badge/scipy-1.4.1-brightgreen"></a>
<a href="https://github.com/bashtage/arch"><img src="https://img.shields.io/badge/arch-4.13-red"></a>
<a href="https://pypi.org/project/PyQt5/"><img src="https://img.shields.io/badge/pyqt5-5.10-orange"></a>

# Introduction

在写论文的时候，我们经常要对各序列做描述性分析，例如下图所示：

![image-20200411114625651](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/114626-160258.png)

虽然没有什么技术难度，但是做起来总会有些繁琐，于是突发奇想，做一个统计性描述生成器，并使用pyqt5生成GUI界面。



# display

主要包括：

- 工具栏：导入数据、开始运行、清空、初始化
- 参数设定
  - date：勾选表示第一列为日期序列，在进行计算统计量时会将其删除；若取消勾选，则不会删除第一列数据
  - 各参数后的空格需要按照顺序，依次填入“1、2、3......"，只能填入整数或不填，其他情况程序报错
- 运行情况说明

<div align=center><img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/114700-497681.png" width="450"></div>



# Usage

在当前路径下的命令行输入：

```shell
python main.py
```

**第一步：导入数据**

输入成功的话，会有导入成功的提示

**第二步：设置顺序**

需要从1开始，按顺序输入

**第三步：开始运行**

点击运行即可。

>  注意：最终结果保存在当前路径下的output.xlsx文件中，如需更改路径，需要修改源码



# Code

代码主体主要有两部分：

* [func.py](https://github.com/lei940324/toy/blob/master/小工具/description/func.py)：各统计量计算
* [myMainWindow.py](https://github.com/lei940324/toy/blob/master/小工具/description/myMainWindow.py)：GUI界面



# Development Tool

- <span>**Qt Creator**</span><img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202003/31/182029-164220.png" width="50" align="absmiddle"><span>：GUI界面可视化</span>

- <span>**PyCharm**</span><img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202003/31/182340-937174.png" width="50" align="absmiddle"><span>：代码编辑器</span>

- <span>**Visual Studio Code**</span><img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/09/000635-457642.png" width="50" align="absmiddle"><span>：代码阅读器</span>



# reference

* 书籍《Python Qt GUI与数据可视化编程》

