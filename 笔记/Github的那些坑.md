- [Github 的那些坑](#head1)
	- [ 图片加载过慢或失败](#head2)
	- [Jupyter 文件加载过慢或失败](#head3)
	- [star 项目没有书签管理](#head4)
	- [Github 项目下载过慢](#head5)
	- [ 项目没有侧栏文件树](#head6)
		- [Octotree 简介](#head7)
		- [Octotree 主要功能](#head8)
		- [Octotree 使用说明](#head9)
		- [ Octotree的注意事项](#head10)
	- [ 只能下载项目全部文件](#head11)
	- [ 阅读代码费劲](#head12)
	- [ 项目语言标注问题](#head13)
	- [Git 忽略提交](#head14)
		- [ 规则作用](#head15)
		- [ 配置语法](#head16)
		- [Git 忽略文件提交的方法](#head17)
	- [下载 GitHub Desktop](#head18)
	- [编写 README.md 之坑](#head19)
		- [ 图片](#head20)
		- [ 表格](#head21)
		- [ 语法兼容](#head22)
		- [设置 shields.io](#head23)
# <span id="head1">Github 的那些坑</span>

> 说 GitHub 是程序员的 facebook 应该一点都不为过，相信需要用到它的朋友也不陌生了。上面有数不清楚的开源项目，就连我们下载的 Chrome 插件很多在 github 上都有源码，并且Github 上代码更新迭代的频率还是蛮快的。但是在我使用过程中，发现有不少大坑.......



## <span id="head2"> 图片加载过慢或失败</span>

网上搜的很多教程都是改`hosts`文件，但是改了之后也没有效果，后来发现是`IP`地址不能直接用他们给的，需要自己改。

在 <https://www.ipaddress.com/> 中输入要查询的网址就可以显示可用的`IP`地址，根据我的经验，主要修改以下几个网址的`IP`地址

```
www.github.com
raw.githubusercontent.com
avatars2.githubusercontent.com
camo.githubusercontent.com
```

这里以`www.github.com`为例进行查询，`IP`地址为`140.82.114.3`

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428130414.png" width="550" ></div>

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428130756.png" width="350" ></div>

> 注意，`IP`地址可能几个月变化一次，如果发现图片加载不成功，可以继续查询修改

**然后修改`hosts`文件**：对于`Windows`用户，`hosts`文件路径为`C:\Windows\System32\drivers\etc\`，使用文本编辑器打开，在最后一行添加：

```
140.82.114.3 www.github.com
199.232.68.133 raw.githubusercontent.com
199.232.68.133 camo.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
```

保存退出后，重启浏览器即可。



## <span id="head3">Jupyter 文件加载过慢或失败</span>

浏览项目时，发现.ipynb文件加载过慢，甚至一直加载失败，刷新n次还是解决不了。

**解决方法一：**

使用网站：<https://nbviewer.jupyter.org/> ，文本框内输入项目文件地址打开即可。

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428131937.png" width="750"></div>

**解决方法二：**

本机安装 jupyter notebook 的情况下直接下载文件并打开



## <span id="head4">star 项目没有书签管理</span>

当star 项目过多时，不易查找某项目，可以通过第三方网站：<https://app.astralapp.com/auth> ，登陆授权后进行书签管理。



## <span id="head5">Github 项目下载过慢</span>

使用网址：<https://g.widora.cn/> ，复制项目链接进行下载。

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428132725.png" width="650" ></div>



## <span id="head6"> 项目没有侧栏文件树</span>

GitHub 作为一款基于 Git 的代码管理工具和协同工具是很优秀的，然而作为代码浏览和搜索工具，就和 IDE 差的很远了。不然为什么到今天 GitHub 连个侧栏的文件树没有，很多开发者要专门去下载浏览器插件才能有文件树？为什么你还是需要`git clone`到本地在把代码装到你的 IDE 里才能愉快的阅读代码？是不是有想过如果能像 IDE 那样在 GitHub 上浏览代码多好？

这里介绍一款 Chrome 浏览器插件 Octotree，让你能像在 GitHub 上像你的 IDE 里一样浏览和搜索代码，让你的 Github 就像穿上了钢铁侠的战衣。

### <span id="head7">Octotree 简介</span>

Octotree 是一款可以使你在 github 查看项目时可以清晰明了的看到项目的结构以及具体代码，使下载代码更具有目的性，减少不必要代码的下载的 chrome 扩展程序。

### <span id="head8">Octotree 主要功能</span>

1. 类似 IDE 的非常方便的代码目录树
2. 使用 PJAX 的超快代码浏览（很快！）
3. 支持公有库和私有库

### <span id="head9">Octotree 使用说明</span>

1. 用户可以在chrome应用商店在线安装（需FQ，可以使用浏览器插件谷歌上网助手），也可以在本站离线下载安装。离线安装 Octotree 的方法参照：[怎么在谷歌浏览器中安装.crx扩展名的离线Chrome插件？](https://chromecj.com/utilities/2014-09/181.html) 

2. 添加成功以后打开 github，在项目左上侧有一个三角收缩符号，点击三角符号，即可看到项目结构图以及具体代码

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428134324.png"></div>



### <span id="head10"> Octotree的注意事项</span>

1. 需要初始化的时间，像 nodejs 这种稍微大一点的代码库要花大概1分钟多

2. 还是初始化的问题，并没有缓存，我自己做的话应该会有缓存，出错的时候再 fix 就好～




## <span id="head11"> 只能下载项目全部文件</span>

Github 上代码更新迭代的频率还是蛮快的，每次更新要么就是命令更新，要么就是上网页打包项目下载。但有时候可能一次更新只更新某个文件或文件夹，要是再重新整个项目打包下载就太麻烦了。

这里要介绍的浏览器插件 GitZip for github 可以快速从 GitHub 上快速下载文件。

**GitZip for github 插件使用方法：**

1. 用户可以在 chrome 应用商店在线安装或者从本站离线下载安装 GitZip for github 插件

2. 安装 GitZip for github 后，点击图标进行 Github 授权

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428135641.png" width="350" ></div>

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428135731.png" width="550" ></div>

3. 打开 GitHub 上的项目，在需要下载的文件或者文件夹空白处双击鼠标，这时该文件或文件夹前就会出现一个勾，表示已经选择，并且在浏览器右下角还会出现一个下载按钮。

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428135520.png"  ></div>

4. 点击下载按钮后，GitZip for github 会自动向服务器进行请求，将你需要的文件盒文件夹进行下包，下载到浏览器的默认下载文件夹处。

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428140646.png" width="350" ></div>

5. 而如果下载时提示次数用完，则是扩展中的 API 次数用完了。你可以重复步骤2获取 API 次数



## <span id="head12"> 阅读代码费劲</span>

作为编程人员，经常会阅读大神们的代码进行学习，像GitHub上有很多好的开源的代码供我们学习，所以呢，问题就来了，一般的方法阅读代码不光费劲，而且项目结构也不容易搞清楚。偶然发现了一个可以很好地查看代码的工具 Sourcegraph，觉得很好。

**在GitHub上利用 Sourcegraph 查看阅读代码**

进入 GitHub，找一个项目，点开一个文件，在工具栏里会看到多了一个 View File 的按钮，点击此按钮，如下图：

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428141534.png" width="650" ></div>

这样我们就可利用 Sourcegraph 很方便地查看代码了，而且项目结构也非常清晰。



## <span id="head13"> 项目语言标注问题</span>

本来写的 python 项目，结果系统自动识别为别的语言

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428142005.png" width="450" ></div>

需要在项目中加入`.gitattributes`文件

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428142130.png" width="750" ></div>

各语言模板可以参考：<https://github.com/alexkaratarakis/gitattributes>



## <span id="head14">Git 忽略提交</span>

在使用 Git 的过程中，我们希望有的文件比如日志，临时文件，编译的中间文件等不要提交到代码仓库，这时就要设置相应的忽略规则，来忽略这些文件的提交。

### <span id="head15"> 规则作用</span>

*  /mtk                  - 过滤整个文件夹

* *.zip                  - 过滤所有.zip文件

* /mtk/do.c         - 过滤某个具体文件

* !/mtk/one.txt   - 追踪（不过滤）某个具体文件     

> 注意：如果你创建.gitignore文件之前就push了某一文件，那么即使你在.gitignore文件中写入过滤该文件的规则，该规则也不会起作用，git仍然会对该文件进行版本管理。

### <span id="head16"> 配置语法</span>

* 以斜杠“/”开头表示目录；

* 以星号“*”通配多个字符；

* 以问号“?”通配单个字符

* 以方括号“[]”包含单个字符的匹配列表；

* 以叹号“!”表示不忽略(跟踪)匹配到的文件或目录。

> 注意： git 对于 .gitignore配置文件是按行从上到下进行规则匹配的

### <span id="head17">Git 忽略文件提交的方法</span>

在Git项目中定义 `.gitignore` 文件

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428143321.png" width="750" ></div>

这种方式通过在项目的某个文件夹下定义 `.gitignore` 文件，在该文件中定义相应的忽略规则，来管理当前文件夹下的文件的Git提交行为。

`.gitignore` 文件是可以提交到共有仓库中，这就为该项目下的所有开发者都共享一套定义好的忽略规则。

在 `.gitignore` 文件中，遵循相应的语法，在每一行指定一个忽略规则。

各语言模板可以参考：<https://github.com/github/gitignore>



## <span id="head18">下载 GitHub Desktop</span>

国内用户下载 GitHub Desktop 时，发现无法加载，可以使用浏览器插件：谷歌上网助手



## <span id="head19">编写 README.md 之坑</span>

### <span id="head20"> 图片</span>

写了一篇图文并茂的 README.md 文件，上传到网上，结果发现图片全部不能显示，原因是图片地址皆为本地，如果一个个复制粘贴又太过麻烦，所以建议使用图床。

**方法一：**

最开始，使用 Typora 的插件。项目网址：<https://github.com/Thobian/typora-plugins-win-img>

使用的上传服务器为 **Github**。优点是免费且方便，缺点也很明显，第一非常不稳定，经常上传失败，需要等一会再试；第二公众号不支持（别的如知乎平台没有试过），无法载入相应图片

于是考虑换个服务器，使用 **阿里云 OSS**，以上缺点没有了，但是相较方法二而言，不能自定义链接格式，于是最终选择使用方法二

**方法二：**

阿里云 OSS + PicGO

参考网址：<https://zhuanlan.zhihu.com/p/63557477>

有几点补充，其实无需购买包年包月套餐，正常写个博客公众号之类的，都用流量计费即可。阿里云 OSS 虽然收费，但是不多，使用了几个月，都没有几毛钱。

阿里云 OSS 收费主要有三部分：

1. 调用次数：1万次0.01元，可以忽略
2. 下载流量：最好不要在阿里云 OSS 存大容量文件进行下载，平时作为图床存图片的话，也是可以忽略
3. 流量费用：这个是产生的主要费用，别人查看图片都会消耗流量

PicGo 的自定义链接设置为：

```html
<div align=center><img src="$url" width="350" ></div>
```

这样放入的图片居中，且图片尺寸不会太大

### <span id="head21"> 表格</span>

使用网址：<https://tableconvert.com/>

将 `excel` 等文件中的数据转化为 `markdown`  语法的表格样式

### <span id="head22"> 语法兼容</span>

* Github 不支持 `html` 的部分语法，不支持公式显示，且加粗内容中有冒号时，在 Github 中会渲染失败，例如：  `** word:**`。
* 不支持目录，可以使用该项目：<https://github.com/Holy-Shine/GitToc/blob/master/README_CN.md>，为你的 Github 仓库的 Readme.md 自动生成一个目录，转换后的目录支持页内跳转。

> 若 README.md 文件中含有较多图片和公式，建议将主要内容放入博客或者自己搭建的网站内

### <span id="head23">设置 shields.io</span>

经常有疑问别人项目里的图标哪里设计的

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428144618.png" ></div>

原来在网址：<https://shields.io/category/build> ，使用 `html `语法插入 `markdown`

```html
<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/NetEaseGame/aircv"><img src="https://img.shields.io/badge/aircv-1.4.6-orange"></a>
<a href="https://github.com/bashtage/arch"><img src="https://img.shields.io/badge/arch-4.13-red"></a>
```

效果如下图：

<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://github.com/NetEaseGame/aircv"><img src="https://img.shields.io/badge/aircv-1.4.6-orange"></a>
<a href="https://github.com/bashtage/arch"><img src="https://img.shields.io/badge/arch-4.13-red"></a>