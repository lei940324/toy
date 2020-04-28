## 背景

如果你用Microsoft Word写过长篇大论，那你一定有这样的经历：

想删除一个段落，又怕将来想恢复找不回来怎么办？有办法，先把当前文件“另存为……”一个新的Word文件，再接着改，改到一定程度，再“另存为……”一个新文件，这样一直改下去，最后你的Word文档变成了这样：

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428181726.png" width="350" ></div>

过了一周，你想找回被删除的文字，但是已经记不清删除前保存在哪个文件里了，只好一个一个文件去找，真麻烦。

看着一堆乱七八糟的文件，想保留最新的一个，然后把其他的删掉，又怕哪天会用上，还不敢删，真郁闷。

更要命的是，如果你写过毕业论文，那么你一定经历过论文最终版、最最终版、最最最终版的折磨......

<div align=center><img src="https://raw.githubusercontent.com/lei940324/picture/master/typora202004/15/201019-708257.jpeg"></div>

那么有什么办法呢？当然有，那就是使用Git

Git是什么？

Git是目前世界上最先进的分布式版本控制系统（没有之一）。

Git有什么特点？简单来说就是：高端大气上档次！

开始使用Git，这样你就结束了手动管理多个“版本”的史前时代，进入到版本控制的21世纪。

## 安装

在Windows上使用Git，可以从Git官网直接下载安装程序，然后按默认选项安装即可。

官网：<https://git-scm.com/downloads>

安装完成后，还需要最后一步设置，可以建立某新文件夹，进入文件夹内，右键点击`git`打开

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428182013.png" width="250" ></div></div>

<div align=center><img src="https://lei-picture.oss-cn-beijing.aliyuncs.com/img/20200428182050.png" width="550" ></div>

在命令行输入：

```shell
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

例如这里我的输入：

```shell
git config --global user.name "ouc"
git config --global user.email "892210386@qq.com"
```

> 注意：窗口内复制粘贴内容需要点击右键选择

## 工作原理

配置完成后就可以使用了，先介绍一下Git的工作流程

![img](https://mmbiz.qpic.cn/mmbiz_png/e1jmIzRpwWiaEynpFwWSmr59icj386rKKxiaCC3m4XHaxHaaqLkYlukTUALnHN74icx3VZyIM3uEXz7JA9ldicwe8BQ/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

- Workspace：工作区，就是你在电脑上看到的目录
- Index / Stage：暂存区，好比回收站，改动之后还给你一次反悔的机会
- Repository：仓库区（或本地仓库）：将改动正式存入的地方
- Remote：远程仓库：这里我们用不到，如果你想将文件传入网站（例如github），传入的地方就叫远程仓库

## 使用

首先初始化，在文件夹内打开git窗口输入：

```shell
$ git init
```

然后就可以写入文件了，这里假设写完了论文初稿。

![image-20200415230822867](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/15/230935-897293.png)

窗口输入命令：

```
git status   // 查看文件改动情况，可以跳过
git add .    // 将改动添加到暂存区，注意有一个点，点是通配符，提交所有修改
git commit -m '增加论文初稿'   // 将暂存区文件放入仓库
```

![image-20200415232014375](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/15/232014-404573.png)

这样就把文件改动存入仓库里了，下次与导师碰头，导师跟你提了n点意见，你需要逐一进行修改，于是经过你的奋战，终于将初稿改为终稿，这时就可以将改动存入仓库，重复以上操作：

```shell
git add .    
git commit -m '论文终稿'   
```

![image-20200415233413977](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/15/233518-562977.png)

### 版本回退

假设改了半天，发现还不如初稿写的好，希望回到上一版本，只需输入：

```shell
git reset --hard HEAD^
```

![image-20200415233821020](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/16/005140-283197.png)

可以发现，回到了之前初稿的版本，结果跟导师一番沟通后，导师又觉得终稿写的好，这不耍我玩吗，那怎么回到之前版本呢？可以通过命令查看

```shell
git reflog   // 查看之前的操作
```

结果为

```shell
ab4dfd2 (HEAD -> master) HEAD@{0}: reset: moving to HEAD^
5bd1aa3 HEAD@{1}: commit: 增加论文终稿
ab4dfd2 (HEAD -> master) HEAD@{2}: commit (initial): 增加论文初稿
```

可以发现**增加论文终稿**的操作在第二行，ID为5bd1aa3，只需输入

```shell
git reset --hard 5bd1aa3
```

神奇，论文终稿又回来了。

下面总结一下这几个命令

* git status：查看文件改动情况
* git add .：将所有改动添加到暂存区
* git commit -m 'info'： 将暂存区文件放入仓库，并加入说明
* git reset --hard HEAD^：回退到上个版本，如果回退到上上个版本，只需输入git reset --hard HEAD^^，也支持git reset --hard ID，其中ID为操作的ID号
* git reflog ：查看之前的操作ID号

最后要明确下，所有的版本控制系统，只能跟踪文本文件的改动，比如txt文件，网页，所有程序的代码等，Git也不例外，版本控制系统可以告诉你每次的改动，但是图片，视频，word这些二进制文件，虽能也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是知道图片从1kb变成2kb，但是到底改了啥，版本控制也不知道，所以改动word文件，提交的时候一定要写好注释，方便日后操作。

git的使用有一定专业性，但是学会它的基本操作，你一定会回不去。

