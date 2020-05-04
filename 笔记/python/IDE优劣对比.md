参考知乎：[世界上最好的Python编辑器是什么？我投PyCharm一票](https://zhuanlan.zhihu.com/p/50282051)

## spyder

![preview](https://pic3.zhimg.com/v2-d001ad10ff29f3a7110f53f849357c9e_r.jpg)

Spyder 是 Python 专用的一种开源 IDE，其独特之处在于专为数据科学工作流程进行了优化。它与 Anconda 软件包管理器捆绑在一起，后者是 Python 编程语言的标准发行版。Spyder 拥有所有必需的 IDE 特性，包括代码完整性及集成文件浏览器。

Spyder 专为数据科学项目创建，具备平滑的学习曲线，即学即会。在线帮助选项允许用户在并行开发项目的同时寻找关于库的专门信息。而且，这个 Python 专用 IDE 与 RStudio 类似。因此，在从 R 切换到 Python 时这是一个恰当的选择。

适用于 Python 库的 Spyder 集成支持（如 Matplotlib 和 SciPy）进一步证明，Spyder 是为数据科学家量身打造的。除了可感知的 IPython/Jupyter 集成之外，Spyder 还有一个独特的「variable explorer」特性，允许使用基于表格的布局展示数据。

### 优点

* 模拟 matlab 界面，可以实时查看各变量，非常适合数据分析
* 启动速度一般，快于 PyCharm
* anaconda 内置，无需额外安装，安装后就处理好集成环境，不用再处理环境依赖关系，也包含了`numpy`, `matplotlib` 和 `pandas` ，可以做些数据处理。
* 对初学者相对友好
* 界面整洁
* 数据科学项目的理想工具

### 缺点

* 运行多进程有 bug
* 运行 `pyqt5` 代码有问题
* 调试不如 PyCharm
* 不适用于非数据科学项目
* 对于高阶 Python 开发者而言太基础了

## PyCharm

![preview](https://pic2.zhimg.com/v2-198adcc00469a9d7b06012dd0897b755_r.jpg)

PyCharm 是 Python 的专用 IDE，地位类似于 Java 的 IDE Eclipse。功能齐全的集成开发环境同时提供收费版和免费版，即专业版和社区版。PyCharm 是安装最快的 IDE，且安装后的配置也非常简单，因此 PyCharm 基本上是数据科学家和算法工程师的首选 IDE。

对于喜欢 IPython 或 Anaconda 发行版的人而言，PyCharm 同样可以便捷地集成 Matplotlib 和 NumPy 等工具，这意味着我们在处理数据科学项目时可以便捷地使用数组查看器和交互式图表等。除此之外，IDE 还扩展了对 JavaScript 和 Angular JS 等语言的支持，这使得它同样也适合 Web 端的开发。

安装完成后，我们可以快速建立一个 Python 项目，并选择解释器和新的代码文件。可能我们会用 conda 等工具维护不同的环境，例如 TensorFlow 或 PyTorch 等，在建立新项目时只需要选择这些环境下的 Python 主程序就相当于选择了新环境。最后，除了提供直接 debug 和运行功能外，PyCharm 还提供对源代码和项目控制的支持。

### 优点

* 很方便针对大型的web框架修改调试
* 活跃的社区支持
* 支持全面的 Python 开发，不论是数据科学还是非数据科学项目
* 运行、编辑、debug Python 代码都不需要额外的支持

### 缺点

* 启动较慢
* 配置环境对初学者有一定困难



## vscode

![](https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200504192119.png)

在程序员圈子里，Visual Studio Code（以下简称VSCode）可以说是目前最火的代码编辑器之一了。

它是微软出品的一款**可扩展的轻量级开源编辑器**，并且支持全平台系统。这些特性使得VSCode颇受欢迎，这也使其成为了一个很棒的Python开发平台。

### 优点

* 启动迅速
* 丰富的插件
* 界面干净漂亮

### 缺点

* 更适合作为代码阅读器，而不是代码编辑器



## Jupyter Lab

![preview](https://pic1.zhimg.com/v2-7d85616b3fc6b377b1ed1eb61b62f098_r.jpg)

Jupyter Netbook 起源于 2014 年的 Ipython，它是一种基于服务器-客户端结构的网页应用。Jupyter Netbook 允许我们通过「Notebook」创建和操作代码文件，并且采用一种即时运行的方法，这是 Jupyter Notebook 最重要的特性。对于 Python 数据科学家而言，Jupyter Notebook 基本上是必需品，因为它提供了最直观、最精炼的交互式数据科学环境。

对于刚入门的数据科学家而言，Jupyter 是最简单也最完美的工具。我们在写完一个代码片段后就能直接运行这些局部代码查看效果，因此它的交互效果是最好的。此外，Jupyter Notebook 中的单元可以选择代码或者文档，也就是说选择文档后可以直接按照 MarkDown 的语法写代码或整个文件的注释、心得和背景知识等。

通过使用 Matplotlib 和 Seaborn 等可视化工具，我们可以直接在代码单元下输出想要的可视化图信息。当然我们也可以将整个 Notebook 文件导出为 PDF、HTML 或纯 Python 代码文件，这非常有利于文件在不同平台间的传播，因此像谷歌的 Colab 等平台也都默认使用 Notebook 的这种形式。与 Ipython 一样，Jupyter Notebook 是一系列项目的总称，包括 Notebook、Console 和 Qt console 等。

### 优点

* 提供了最直观、最精炼的交互式数据科学环境
* 允许使用 Notebook 直接创建博客或代码演示
* 在运行整体前可以运行并修正局部代码块
* anaconda 直接集成安装

### 缺点

* 不易调试