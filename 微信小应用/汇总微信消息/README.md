<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/littlecodersh/ItChat"><img src="https://img.shields.io/badge/itchat-1.3.10-blue"></a>
<a href="https://github.com/pandas-dev/pandas"><img src="https://img.shields.io/badge/pandas-1.0.1-yellow"></a>

# Introduction

在微信上，我们经常需要汇总某些群体的信息。例如班长需要统计班里同学的各项信息，每个人都要给班长发信息，如果班里人数太多的话，就会非常繁琐。

鉴于此，开发这个小工具，帮助提高生活效率。



# display

因为本身没有太复杂的功能与选项，所以并没有做成GUI界面，主要通过命令行进行参数设定。

<div align=center><img src= "https://github.com/lei940324/Application_itchat/blob/master/%E6%B1%87%E6%80%BB%E5%BE%AE%E4%BF%A1%E6%B6%88%E6%81%AF/image/%E5%91%BD%E4%BB%A4%E8%A1%8C.png" width="550"></div>


# Usage

在当前路径下的命令行输入：

```shell
python main.py
```

程序运行需扫描二维码登陆微信

输入关键词样式为：姓名，电话，地址

> 注：中间用逗号隔开

微信信息格式例如：

**姓名：张三**

**电话：14565343245**

**地址：山东省青岛市...**

收到信息默认自动回复“已查收”，如需更改请输入2

