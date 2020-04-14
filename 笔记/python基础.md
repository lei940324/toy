# python基础

## 列表list

```python
In [1]: a = [1, 2, 3, 4, 5, 3]; b = [6, 7, 8]

In [2]: a.append(50)                          # 在列表末尾添加元素
In [3]: a
Out[3]: [1, 2, 3, 4, 5, 3, 50]

In [4]: a.count(3)                            # 统计a中3出现的次数
Out[4]: 2

In [5]: a.extend(b)                           # a末尾添加b
In [6]: a
Out[6]: [1, 2, 3, 4, 5, 3, 50, 6, 7, 8]

In [7]: a.index(3)                            # 找到3的索引位置，从最前开始
Out[7]: 2

In [8]: a.insert(3,9)                         # 在索引3处插入9，其他后移
In [9]: a
Out[9]: [1, 2, 3, 9, 4, 5, 3, 50, 6, 7, 8]

In [10]: a.pop()                              # 移除最后一个元素
Out[10]: 8

In [11]: a.pop(3)                             # 将索引3位置的元素删除
Out[11]: 9

In [12]: a.remove(3)                          # 将值为3的元素删一个，从最前开始
In [13]: a
Out[13]: [1, 2, 4, 5, 3, 50, 6, 7]

In [14]: a.reverse()                          # 反向列表中的元素
In [15]: a
Out[15]: [7, 6, 50, 3, 5, 4, 2, 1]

In [16]: a.sort()                             # 对列表进行排序
In [17]: a
Out[17]: [1, 2, 3, 4, 5, 6, 7, 50]
```



## 字符串str

### 字符串方法

* 将字符串的第一个字符转换为大写/全小写/全大写

  ```python
  capitalize()，lower()，upper()
  ```

* 如果字符串至少有一个字符，并且所有字符都是字母则返回 True

  ```python
  isalpha()
  ```

* 如果字符串只包含数字则返回 True

  ```python
  isnumeric()
  ```

* 检测 str 在指定 beg和end范围内，包含返回开始的索引值，否则返回-1

  ```python
  find(str, beg=0, end=len(string))
  ```

* 把字符串中的str1替换成str2，如果max指定，则替换不超过max次。

  ```python
  replace(old, new, [max])
  ```

  

### 清理字符串

* 去除右边空格：`str.rstrip()`
* 去除左边空格：`str.lstrip()`
* 去除两边空格：`str.strip()`
* 去除右边冒号：``str.rstrip('：')``



### 对齐文本

```python
'Hello'.rjust(10)
'Hello'.ljust(10, '*')
'Hello'.center(10)
```



### 字符串格式化输出

```python
%m.nf                         # 浮点数输出
%d                            # 整数输出
%s                            # 字符串输出
\b                            # 退格
a='%.3f' %0.55                # 保留三位小数 
b='{:.2}fd{}fd'.format(a,a)   # 保留两位小数
```

| 3.1415926  | {:.2f}  |   3.14    |       保留小数点后两位       |
| :--------: | :-----: | :-------: | :--------------------------: |
| 3.1415926  | {:+.2f} |   +3.14   |    带符号保留小数点后两位    |
|     -1     | {:+.2f} |   -1.00   |    带符号保留小数点后两位    |
|  2.71828   | {:.0f}  |     3     |           不带小数           |
|     5      | {:0>2d} |    05     | 数字补零 (填充左边, 宽度为2) |
|     5      | {:x<4d} |   5xxx    | 数字补x (填充右边, 宽度为4)  |
|     10     | {:x<4d} |   10xx    | 数字补x (填充右边, 宽度为4)  |
|  1000000   |  {:,}   | 1,000,000 |     以逗号分隔的数字格式     |
|    0.25    | {:.2%}  |  25.00%   |          百分比格式          |
| 1000000000 | {:.2e}  | 1.00e+09  |           指数记法           |
|     18     | {:>10d} |   ‘ 18’   |   右对齐 (默认, 宽度为10)    |
|     18     | {:<10d} |   ‘18 ‘   |      左对齐 (宽度为10)       |
|     18     | {:^10d} |  ‘ 18 ‘   |     中间对齐 (宽度为10)      |



## 字典dict

```python
In [1]: d = {'name':'lei', 'age':18, 'sex':'man'}

In [2]: d.keys()                           # 得到字典key值
Out[2]: dict_keys(['name', 'age', 'sex'])

In [3]: d.values()                         # 得到字典值
Out[3]: dict_values(['lei', 18, 'man'])

In [4]: d.items()                          # 得到(key,values)元组组合的列表
Out[4]: dict_items([('name', 'lei'), ('age', 18), ('sex', 'man')])
    
In [5]: d.pop('name')                      # 删除键值
```

### Python字典设置默认值

```python
count_dict = {}
for word in word_list:   
    count_dict.setdefault(word, 0)
    count_dict[word] += 1
```



## 集合set

```python
a - b  # 差集
a & b  # 交集
a | b  # 并集
```

## open() 函数

[![Python 内置函数](https://www.runoob.com/images/up.gif) Python 内置函数](https://www.runoob.com/python/python-built-in-functions.html)

python open() 函数用于打开一个文件，创建一个 **file** 对象，相关的方法才可以调用它进行读写。

更多文件操作可参考：[Python 文件I/O](https://www.runoob.com/python/python-files-io.html)。

### 函数语法

```python
open(name[, mode[, buffering]])
```

参数说明：

- name : 一个包含了你要访问的文件名称的字符串值。
- mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
- buffering : 如果 buffering 的值被设为 0，就不会有寄存。如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

不同模式打开文件的完全列表：

| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |
| x    | 排它性创建，如果文件已存在则失败                             |

### file 对象方法

- **file.read([size])**：size 未指定则返回整个文件，如果文件大小 >2 倍内存则有问题，f.read()读到文件尾时返回""(空字串)。
- **file.readline()**：返回一行。
- **file.readlines([size])** ：返回包含size行的列表, size 未指定则返回全部行。
- **for line in f: print line** ：通过迭代器访问。
- **f.write("hello\n")**：如果要写入字符串以外的数据,先将他转换为字符串。
- **f.tell()**：返回一个整数,表示当前文件指针的位置(就是到文件头的比特数)。
- **f.seek(偏移量,[起始位置])**：用来移动文件指针。
  - 偏移量: 单位为比特，可正可负
  - 起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
- **f.close()** 关闭文件

> 更多内容参考：[Python File(文件) 方法](https://www.runoob.com/python/file-methods.html)



## 随机数生成

```python
random.randint(12,20)          # 均匀整数
random.uniform(10,20)          # 均匀区间
random.choice('abcdefg')       # 集合选取
random.choice([1,2,3,4,5,6])
random.sample([1,2,3,4,5,6],3) # 不重复3次
```



## 正则表达式

### 在线测试工具

https://tool.oschina.net/regex/



### 基础语法

```python
import re
string=''
pipei=re.compile('')
pipei.findall(string)
pipei.split(string)       # 分割
pipei.sub(';;',string)    # 替换
```

![image-20200309185248222](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/14/133821-55554.png)

![image-20200309185334562](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/14/133838-966799.png)

![image-20200309185506977](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/14/133828-828951.png)



### 关于正则的逻辑语句

1. 写一个正则表达式，要求匹配字符串同时满足条件A和条件B
   先写两个子表达式PatternA和PatternB，分别校验条件A和条件B。然后结合成一个新的表达式
   (?=PatternA)PatternB
2. 写一个正则表达式，要求匹配字符串满足条件A,但不可满足条件B
   (?!PatternB)PatternA
3. 写一个正则表达式，要求匹配字符串或者满足条件A或者满足条件B
   (PatternA|PatternB)



## win32库

### 窗口进程操作

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:49:20 2019

@author: Administrator
"""
from ctypes import *
import time
 
user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

# 获取最上层的窗口句柄
time.sleep(2)
hwnd = user32.GetForegroundWindow()
 

#获取全部进程
import psutil
pids = psutil.pids()
for pid in pids:
  p = psutil.Process(pid)
  print("pid-%d,pname-%s" %(pid,p.name()))
  
  
###################################################
#获取当前窗口信息
import win32gui, win32con
window = win32gui.GetForegroundWindow()  
now = win32gui.GetWindowText(window)  
if now != 'Spyder (Python 3.7)':
    win32gui.PostMessage(window, win32con.WM_CLOSE, 0, 0)    #关闭当前窗口
    
  
##################################################
import win32gui, win32api, win32con
hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)

win32gui.SetForegroundWindow(787322)     #控制当前窗口
win32gui.ShowWindow(722852, 9)     #强制显示
win32gui.PostMessage(2294282, win32con.WM_CLOSE, 0, 0)    #关闭当前窗口
win32gui.CloseWindow(722852)   #最小化窗口
#获取当前进程
spyder = win32gui.FindWindow(None, 'Spyder (Python 3.7)') 


####################################################
#关闭指定窗口
import win32gui
from win32.lib import win32con
import time

def handle_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        if 'Chrome' in win32gui.GetWindowText(hwnd):
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

if __name__ == '__main__':
    win32gui.EnumWindows(handle_window, None)
    time.sleep(5)
    # TODO If app didn't close, force close.
    
    
####################################################
#显示所有进程和句柄    
hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
    #if win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)
# =============================================================================
# for h,t in hwnd_title.items():
#     if t is not "":
#         print(h, t)
# =============================================================================

wechat = filter(lambda x:'微信'== x[1], hwnd_title.items())
for (key,value) in wechat:
    print('%s : %s' % (key,value))
```


