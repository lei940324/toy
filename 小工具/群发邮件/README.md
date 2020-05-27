<a href="https://www.python.org/downloads/"><img  src="https://img.shields.io/badge/python-3.6%2B-brightgreen"></a>
<a href="https://mail.qq.com/"><img  src="https://img.shields.io/badge/邮箱-QQ 邮箱-brightgreen"></a>
<a href="https://mail.qq.com/"><img  src="https://img.shields.io/badge/邮箱-阿里云-brightgreen"></a>

### 使用 QQ 邮箱

使用 QQ 邮箱群发邮件，首先需要在 QQ 邮箱的**设置** >> **账户**，开启 SMTP 服务。

<div align=center><img src="https://gitee.com/lei940324/picture/raw/master/file/群发email/202005192037-1.png" width="646" ></div>

<div align=center><img src="https://gitee.com/lei940324/picture/raw/master/file/群发email/202005192038-2.png" width="732" ></div>

打开`QQMail`代码，修改各参数：

```python
from_addr = 'xxx@qq.com'   # 发信邮箱
password = 'xxx'   # QQ 邮箱授权码，QQ 邮箱设置 >> 账户 打开 SMTP
to_addr = 'xxx@xxx.com'  # 收信方邮箱
exc = sendEmail(from_addr, password)

Text = '正文内容'
exc.addText('邮件标题', Text, '发件人姓名', '收件人姓名')
# exc.addFile('附件路径', '附件名')
exc.send(to_addr)

exc.quit()
```



### 使用阿里云邮件

每天 200 封免费发信额度，超过额度按照实际使用量计费，单价为 2 元/1000 封。

需要有个人域名具体教程可参考：<https://blog.csdn.net/u014633966/article/details/87877846>