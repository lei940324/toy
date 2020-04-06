# 介绍

将pdf水印去掉，仅适用于黑白色，因为彩色会出现过度锐化现象

效果图：

![image-20200406193543968](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/06/193550-696399.png)

# 要求

* python3.6+
* 第三方库：`pdf2image`、`fitz`、`wand`

# 实现原理

1. 将pdf转为图片
2. 将图片进行锐化处理，根据字体颜色对比去除水印
3. 将转化的图片转为pdf

# 环境配置

* 安装pdf2image: pip install pdf2image

* Windows安装配置poppler

  Windows用户必须为Windows安装poppler (http://blog.alivate.com.au/poppler-windows/)，然后将bin/文件夹添加到环境变量，并且需要重启电脑才会生效

## 安装wand库

环境：win10、python3

需要安装wand 、imagemagick和ghostscript

wand的安装很简单：直接cmd 运行pip install wand

然后安装imagemagick ，从这里下载[网页链接](https://www.imagemagick.org/script/download.php#windows)，注意是32位还是64位，这个需要和python的位数一致。

安装过程注意勾选Install development headers and libraries for C and C++ 。安装后设置MAGICK_HOME环境变量，值为imagemagick的安装路径，并将安装路径加入path。

详情可参照此页面[网页链接](http://docs.wand-py.org/en/0.4.4/guide/install.html#install-imagemagick-windows)。

最后安装ghostscript，这里下载[网页链接](https://ghostscript.com/download/gsdnld.html)，选择AGPL release，注意32位还是64位。

安装过程很简单，一路点击next，如果不想安装在c盘，可以改变安装路径，这个没有影响。

```python
from wand.image import Image
from wand.color import Color
 
with Image(filename="1.pdf",resolution=120) as img:
    img.format = 'jpeg'
    img.compression_quality = 90
    img.background_color = Color("white")
    img.save(filename='converted.jpeg')
```

## 安装fitz库

直接pip install fitz会报错

需要下载traits进行安装，下载地址https://www.lfd.uci.edu/~gohlke/pythonlibs/#traits

需要选取对应py版本，然后

```shell
pip install traits-6.0.0-cp37-cp37m-win_amd64.whl
```

在python导入fitz库依然报错

解决方法：

```shell
pip install PyMuPDF
```

# 使用

首先根据水印深浅，调整main.py文件中文件名与value值，value默认108

然后在命令行输入

```shell
python main.py
```



# 颜色对比选取

value值越大越清晰，一般为108到130，越小越能去水印，但越不清晰

* 90为佳

![image-20200406191544967](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/06/191602-630465.png)

* 120为佳

  ![image-20200406191643950](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/06/191648-202081.png)![image-20200406191710897](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/06/191711-947065.png)

