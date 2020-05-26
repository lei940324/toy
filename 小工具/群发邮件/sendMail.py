# -*- coding: utf-8 -*-
"""
使用 QQ 邮箱发送邮件
@author: lei

"""
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


class sendEmail():
    def __init__(self, from_addr, password):
        """
        from_addr: 发信邮箱
        password: QQ 邮箱授权码
        """
        self.from_addr = from_addr
        self.password = password
        # 初始化
        self.msg = MIMEMultipart()
        smtp_server = 'smtp.qq.com'   # 发信服务器
        # 开启发信服务，这里使用的是加密传输
        self.server = smtplib.SMTP_SSL(host=smtp_server)
        self.server.connect(smtp_server, 465)
        # 登录发信邮箱
        self.server.login(self.from_addr, self.password)

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
            self.msg['To'] = Header(ToName)
        self.msg['Subject'] = Header(Subject)
        self.msg['From'] = Header(FromName)
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
        self.server.sendmail(self.from_addr, to_addr, self.msg.as_string())
        self.msg = MIMEMultipart()

    def quit(self):
        """ 关闭服务器 """
        self.server.quit()


if __name__ == "__main__":
    from_addr = 'xxx@qq.com'   # 发信邮箱
    password = 'xxx'   # QQ邮箱授权码，QQ邮箱设置 >> 账户 打开 SMTP
    to_addr = 'xxx@xxx.com'  # 收信方邮箱
    exc = sendEmail(from_addr, password)

    Text = '正文内容'
    exc.addText('邮件标题', Text, '发件人姓名', '收件人姓名')
    # exc.addFile('附件路径', '附件名')
    exc.send(to_addr)

    exc.quit()
