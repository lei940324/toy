<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://www.aliyun.com/product/directmail?utm_content=se_1005171211"><img  src="https://img.shields.io/badge/邮箱-阿里云-red"></a>
<a href="https://mail.qq.com/"><img  src="https://img.shields.io/badge/邮箱-QQ 邮箱-blue"></a>
<a href="https://mail.163.com/"><img  src="https://img.shields.io/badge/邮箱-网易邮箱-blue"></a>


### 阿里云邮件（默认）

每天 200 封免费发信额度，超过额度按照实际使用量计费，单价为 2 元/1000 封。

#### 使用教程

1. 注册[阿里云账号](https://www.aliyun.com/product/directmail?utm_content=se_1005171211)，开通邮件推送。

2. 准备一个域名，随便买一个就行，最低8元一年，如何购买请参考：[域名笔记](https://github.com/lei940324/toy/blob/master/笔记/python/搭建网站/域名笔记.md)

3. 进入控制台，配置。

   具体教程可参考：[CSDN 博客：利用阿里云邮件推送免费发邮件](https://blog.csdn.net/u014633966/article/details/87877846)

打开 [sendMail](sendMail.py) 代码，修改各参数：

```python
from_addr = 'xxx@lei940324.xyz'   # 配置的发信地址
password = 'xxx'                  # 密码
to_addr = ['xxx@xxx.com']         # 收信方邮箱，可以是其他类型邮箱，列表类型
exc = sendEmail(from_addr, password)

Text = '正文内容'
exc.addText('邮件标题', Text, '发件人姓名', '收件人姓名')
# exc.addFile('附件路径', '附件名')
exc.send(to_addr)

exc.quit()
```



### QQ 邮箱

使用 QQ 邮箱群发邮件，首先需要在 QQ 邮箱的**设置** >> **账户**，开启 SMTP 服务。

<div align=center><img src="https://gitee.com/lei940324/picture/raw/master/file/群发email/202005192037-1.png" width="646" ></div>

<div align=center><img src="https://gitee.com/lei940324/picture/raw/master/file/群发email/202005192038-2.png" width="732" ></div>

打开 [sendMail](sendMail.py) 代码，修改各参数：

```python
from_addr = 'xxx@qq.com'   # 发信邮箱，必须为 QQ 邮箱 
password = 'xxx'           # QQ 邮箱授权码，QQ 邮箱设置 >> 账户 打开 SMTP
to_addr = ['xxx@xxx.com']  # 收信方邮箱，可以是其他类型邮箱，列表类型
exc = sendEmail(from_addr, password, types='QQ')

Text = '正文内容'
exc.addText('邮件标题', Text, '发件人姓名', '收件人姓名')
# exc.addFile('附件路径', '附件名')
exc.send(to_addr)

exc.quit()
```

经过测试，QQ 邮箱有频率限制，大约一分钟不能超过 10 条，这显然不能满足需求，因此推荐使用阿里云。

### 网易邮箱

开启 163 的 smtp 服务器

<div align=center><img src="https://gitee.com/lei940324/picture/raw/master/file/email/202005125344-1.png" width="750" ></div>

打开 [sendMail](sendMail.py) 代码，修改各参数：

```python
from_addr = 'xxx@163.com'   # 发信邮箱，必须为 163 邮箱 
password = 'xxx'            # 网易邮箱密码
to_addr = ['xxx@xxx.com']   # 收信方邮箱，可以是其他类型邮箱，列表类型
exc = sendEmail(from_addr, password, types='163')

Text = '正文内容'
exc.addText('邮件标题', Text, from_addr, to_addr[0])
# exc.addFile('附件路径', '附件名')
exc.send(to_addr)

exc.quit()
```

> 注：发件人姓名和收件人姓名必须为对应邮箱，否则报错 554