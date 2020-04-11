<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/pandas-dev/pandas"><img src="https://img.shields.io/badge/pandas-1.0.1-yellow"></a>
<a href="https://github.com/python-openxml/python-docx"><img src="https://img.shields.io/badge/python--docx-0.2.4-orange"></a>

# Introduction

中国海洋大学毕业论文，自动修改格式、增加封面

需要将正文word文档放入文件夹内，正文包括中英文摘要，目录，引言.....致谢等，正文格式需要自行调整，默认引言在正文第7页。

在命令行输入

```shell
python func.py
```


# 不足

由于页码与目录格式设置较复杂，运行完还需修改内容：

* 封面信息

* 修改页码

  <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/120111-367528.png" width="650">

  <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/120621-190856.png" width="250">

  <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/120633-350260.png" width="650">

  <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/120638-775111.png" width="650">

* 修改页码之后，更新目录页码，更改目录格式

  <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/120647-296212.png" width="650">

  <img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/11/120650-863927.png" width="250">



# 常见问题汇总

* 论文里页眉是否有题目，引言之前不要有页眉，横线也不要有。
* 封面字体最好加粗  有不加粗的  实在加粗不好看不加也没问题
* 看一下页码是否有  有转成pdf之后没有了的
* 有的公式转为pdf后变为乱码，注意查看
* 全文行距 大多数1.5倍行距 
* 中文摘要的题目有加的有没加的无所谓  关键词前是否空两格也无所谓，但空着更好看，一般来说要空着  英文标题字体黑体还是time都行
* 表尽量在一页上 跨页的最好再用续表格式  很多同学的表都乱七八糟的  估计是转换的问题  很多没加续表就跨页的 最好加续表
* 表格尽量不要截图 自己做  截的图及其不清楚  影响观感
* 参考文献 序号后要不要有空格  最好全部一致   有前后不一致的比较难看   
* 封皮日期一般填送审日期
* 表格与图字体比正文小一号，其中图中汉字字体为宋体，数字和字母的字体为Times NewRoman。线用1磅粗的线，刻度线在坐标轴内侧，不要有网格线。
* 公式序号与正文文字匹配
* 修改内容后，记得刷新一下目录