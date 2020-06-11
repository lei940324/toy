<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/openatx/uiautomator2"><img src="https://img.shields.io/badge/uiautomator2-2.7.1-brightgreen"></a>
<a href="https://github.com/NetEaseGame/aircv"><img src="https://img.shields.io/badge/aircv-1.4.6-orange"></a>
<a href="https://github.com/python-pillow/Pillow"><img src="https://img.shields.io/badge/Pillow-7.0.0-red"></a>



  > 这里有一点要注意的是 aircv 依赖于 cv2 库，**有个很坑的地方是**，不能直接通过 pip install cv2 进行安装，而应该是 pip install opencv-python，就可以安装了。

## 介绍

使用图像识别进行刷取，更加稳定，主要是提供一个图像识别应用的思路。

### 关卡选取

王者荣耀的冒险模式里有个挑战模式，第一次过关可以获得比较多的金币，后面重新挑战还是会获得少量金币，这不算是 bug，只要你不嫌烦手动蛮力也可以刷金币。

推荐关卡：堕落的祸源 - 稷下战场（大师）

<img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/06/132139-811784.png" width="500">

一把可以加 56 金币，大约 100 秒左右一局，在开挂前建议你手动通关体验一下，至少自动操作可以通关，此为游戏原理。不过挂机想通关稷下战场一般需要满符文，所以如果没有达到条件，可以刷：陨落的废都 - 魔女回忆，此关卡使用纯输出英雄 20 秒左右可以打 BOSS，50 秒左右可以通关，每次重复通关可以获得奖励 19 金币。

测试的时候我用的英雄是：赵云，鲁班，扁鹊

### 操控原理

使用 python-uiautomator2 操控手机，只支持安卓手机，具体准备工作可以参考：[手机自动化测试（准备篇）](https://blog.csdn.net/u013289615/article/details/90480832)。

因为王者荣耀无法通过 uiautomator2 获取控件，所以本文思路是通过 uiautomator2 获取手机截图，接入腾讯 OCR 进行文字识别，并得到其文字位置，进而点击对应坐标并保存按钮截图，最后完成其按钮操作。以后的循环就只根据图像识别，进行模糊匹配获取当前屏幕信息，不再进行 OCR 识别。

uiautomator2 库本身带有 OCR 识别功能，但是并没有对应的 API 接口，需要自己找，于是从腾讯开发者里找到了文字 OCR，结果发现并没有对应的 python3SDK 接口，真是坑，只好自己编个程序获取数据了，具体原理不细说了，不是本文的重点，有兴趣的可以认真看看[tencentOCR.py](tencentOCR.py)，没兴趣的也要进入[tencentOCR.py](tencentOCR.py)进行参数设定，找到代码里**appid，secret_id，secret_key**自己更改一下，[腾讯 AI 中心](https://open.youtu.qq.com/#/open)申请一个账号，在控制台能看到这几个变量，每个账号都有专属的 ID。

## 使用方法

1. 使用数据线连接手机，保证开发者选项已打开，uiautomator2 能与手机正常连接，可以连接多台手机

2. 手机打开王者，并将界面打开至闯关

<img src= "https://raw.githubusercontent.com/lei940324/picture/master/typora202004/06/133305-447174.png" width="500">


3. 根据闯关的不同，调整`main.py`代码中`timer`参数值，默认为 98 秒

4. 命令行输入：

   ```
   python main.py
   ```