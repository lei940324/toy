<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/numpy/numpy"><img src="https://img.shields.io/badge/numpy-1.18.1-blue"></a>

# 介绍

将倾斜文本的图片进行矫正

效果图对比：

![image-20200406211034252](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/06/211825-538054.png)

# 要求

* python3.6+
* 第三方库：`numpy`

# 使用

修改图片名，注意图片名不能有中文，否则报错

命令行输入

```
python main.py
```

# 原理

通过霍夫变换、反三角函数获得斜率

**参考资料：**

https://www.jianshu.com/p/34d6dc466e81

**主要步骤：**

1. 输入图片
2. 灰度化
3. 腐蚀、膨胀
4. 边缘检测
5. 霍夫变换得到线条并画出
6. 计算角度
7. 仿射变换，将原图校正