# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

# Email地址和口令:
gaodun_email = 'ethan.dai@gaodun.cn'
gaodun_email_password = 'Daishun1234'
# 收件人地址:
kitty_email = 'kitty.zhang@gaodun.cn'
like_email='anthony.li@gaodun.cn'
# 输入SMTP服务器地址:
gaodun_smtp_server = 'smtp.exmail.qq.com'


def sendmail(content):

    # 输入内容
    msg_input = content

    # 伪装格式
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    msg_email = MIMEText(msg_input, 'plain', 'utf-8')
    msg_email['From'] = _format_addr('我是收件人 <%s>' % like_email)
    msg_email['To'] = _format_addr('我是发件人 <%s>' % 'golden@gaodun.com')
    msg_email['Subject'] = Header('我是标题', 'utf-8').encode()

    # 发送邮件
    import smtplib
    server = smtplib.SMTP(gaodun_smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(gaodun_email, gaodun_email_password)
    server.sendmail(gaodun_email, [gaodun_email], msg_email.as_string())
    server.quit()




