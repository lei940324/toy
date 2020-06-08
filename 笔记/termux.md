详情参考：[Termux 高级终端安装使用配置教程](https://www.sqlsec.com/2018/05/termux.html)

## 更换国内源

```bash
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list

sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list

sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list

pkg update
```



## ssh 连接

### 安装openssh

申请读写权限

```sh
termux-setup-storage
```

安装openssh

```sh
apt update
apt install openssh
```

------

### 配置登录密钥

如果你的电脑生成过密钥，可以跳过这步。如果没有，在电脑依次执行以下命令。

```sh
ssh-keygen
```

然后进入电脑`.ssh`目录，将**id_rsa.pub**文件拷贝到手机的`/sdcard`目录下。

可以用adb命令push

```sh
cd ~/.ssh/
adb push id_rsa.pub /sdcard/
```

------

### 添加公钥信息

确保**id_rsa.pub**存在于`/sdcard/`目录下，进入手机Termux。依次输入以下命令。

```sh
cd ~/.ssh
cp /sdcard/id_rsa.pub ./
cat id_rsa.pub >> authorized_keys
```

至此，已添加公钥信息到手机。

手机查看当前ip

```sh
$ ifconfig -a
Warning: cannot open /proc/net/dev (Permission denied). Limited output.
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1  (UNSPEC)

rmnet_data5: flags=65<UP,RUNNING>  mtu 1410
        inet 10.171.116.147  netmask 255.255.255.248
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)

tun0: flags=81<UP,POINTOPOINT,RUNNING>  mtu 20000
        inet 192.18.0.1  netmask 255.255.255.255  destination 192.18.0.1
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500
(UNSPEC)

wlan1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.43.1  netmask 255.255.255.0  broadcast 192.168.43.255
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 3000  (UNSPEC)
```

启动sshd服务

```sh
sshd
```

至此，手机端已经安装好openssh，并已启动服务。

保证电脑与手机处在同一网络，这里我是选择和手机在一个热点

PC 端输入：

```
ssh 10.171.116.147 -p 8022
```



## 安装软件

### 基础工具

```
pkg install vim curl wget git tree -y
```



### 终端配色方案

```bash
sh -c "$(curl -fsSL https://html.sqlsec.com/termux-install.sh)"  
```

Android6.0 以上会弹框确认是否授权访问文件,点击`始终允许`授权后 Termux 可以方便的访问SD卡文件。

手机 App 默认只能访问自己的数据，如果要访问手机的存储，需要请求权限，如果你刚刚不小心点了拒绝的话，那么可以执行以下命令来重新获取访问权限:

Bash

```bash
termux-setup-storage
```

脚本允许后先后有如下两个选项:

Bash

```bash
Enter a number, leave blank to not to change: 14
Enter a number, leave blank to not to change: 6
```



### 安装 python

```
pkg install python
```

#### 升级 pip

```bash
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

# 更换下载源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



#### 安装 lxml

```
pkg install libxml2 libxslt
pip install lxml -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```



#### 安装 pillow

```
pkg install -y python ndk-sysroot clang make libjpeg-turbo
```



#### 安装 uiautomator2

```
pip install uiautomator2 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```



```
import uiautomator2 as u2

u2.connect_wifi('192.168.43.143')
print(d.info)
```

#### 安装其他

```
pip install openpyxl jieba requests
```



### Termux:API

```
pkg install termux-api
```



### 安装 ADB

https://github.com/MasterDevX/Termux-ADB

github 无法访问的话，需要更改下载地址