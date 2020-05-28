# -*- coding: utf-8 -*-
"""
群发邮件，支持 QQ 邮箱(QQ)；阿里云(aliyun)；网易邮箱（163）邮件群发
QQ 邮箱有频率限制
阿里云每天 200 条免费额度

@author: lei

"""
import smtplib
import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


class ConnectError(Exception):
    pass


class SendError(Exception):
    pass


class sendEmail():
    def __init__(self, from_addr, password, types='aliyun'):
        """
        from_addr: 发信邮箱
        password: 邮箱授权码
        types: 邮箱类型，默认阿里云，支持:
               QQ 邮箱 - QQ
               阿里云 - aliyun
               163 邮箱 - 163
        """
        self.from_addr = from_addr
        self.password = password
        # 初始化
        self.msg = MIMEMultipart()
        if types == 'QQ':
            smtp_server, host = 'smtp.qq.com', 465
        elif types == 'aliyun':
            smtp_server, host = 'smtpdm.aliyun.com', 465
        elif types == '163':
            smtp_server, host = "smtp.163.com", 994
        else:
            raise TypeError('不支持该类型邮箱')

        try:
            # 开启发信服务，这里使用的是加密传输
            self.server = smtplib.SMTP_SSL(smtp_server, host)
            # self.server.connect(smtp_server, host)
            self.server.login(self.from_addr, self.password)
        except smtplib.SMTPConnectError:
            raise ConnectError('邮件发送失败，连接失败')
        except smtplib.SMTPAuthenticationError:
            raise ConnectError('邮件发送失败，认证错误:')

    def addText(self, Subject, Text=None, FromName=None, ToName=None):
        """
        Subject: 邮件标题
        Text: 正文内容
        FromName: 发件人
        ToName: 收件人
        """
        if FromName is None:
            FromName = self.from_addr
        if ToName is not None:
            self.msg['To'] = ToName
        self.msg['Subject'] = Subject
        self.msg['From'] = f'{FromName} <{self.from_addr}>'
        self.msg['Reply-to'] = self.from_addr
        self.msg['Message-id'] = email.utils.make_msgid()
        self.msg['Date'] = email.utils.formatdate()
        self.msg.attach(MIMEText(Text, 'plain', 'utf-8'))

    def addFile(self, filePath, fileName):
        """
        增加附件
        filePath: 附件路径
        fileName: 附件名
        """
        fileApart = MIMEApplication(open(filePath, 'rb').read())
        fileApart.add_header('Content-Disposition', 'attachment',
                             filename=fileName)
        self.msg.attach(fileApart)

    def send(self, to_addr):
        """
        发送邮件
        to_addr: 收信方邮箱
        """
        if isinstance(to_addr, str):
            to_addr = [to_addr]
        for name in to_addr:
            try:
                self.server.sendmail(self.from_addr, name,
                                     self.msg.as_string())
            except smtplib.SMTPSenderRefused:
                raise SendError('邮件发送失败，发件人被拒绝:')
            except smtplib.SMTPRecipientsRefused:
                raise SendError('邮件发送失败，收件人被拒绝:')
            except smtplib.SMTPDataError:
                raise SendError('邮件发送失败，数据接收拒绝:')
            except smtplib.SMTPException as e:
                raise SendError('邮件发送失败, {}'.format(str(e)))
            except Exception as e:
                raise SendError('邮件发送异常, {}'.format(str(e)))
        self.msg = MIMEMultipart()   # 重置邮件内容

    def quit(self):
        """ 关闭服务器 """
        self.server.quit()


if __name__ == "__main__":
    from_addr = 'xxx@qq.com'   # 发信邮箱
    password = 'abcdef'   # 邮箱授权码
    to_addr = ['xxx@qq.com']  # 收信方邮箱，列表形式
    exc = sendEmail(from_addr, password, 'QQ')

    for i in range(1):
        Text = '正文内容'
        exc.addText(f'标题{i+1}', Text, '发件人姓名', '收件人姓名')
        # exc.addFile(r'C:\Users\Administrator\Desktop\test.pdf', 'test.pdf')
        exc.send(to_addr)
        print(f'已发送{i+1}次')
        time.sleep(1)

    exc.quit()
