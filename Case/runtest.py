# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/20 9:53
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import unittest
import time
import os
import smtplib
import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import multiprocessing
from utils.server import Server
from utils.write_user_command import WriteUserCommand
from email.mime.multipart import MIMEMultipart
from ParametrizedTestCase import ParametrizedTestCase
import test_case
import test_case2

# 设置基本的收取信息
smtpserver = 'smtp.supcon.com'  # 服务器地址
receiver = ['qianyue@supcon.com']  # 收件人（多个人中间用逗号间隔）
sender = 'qianyue@supcon.com'  # 邮件发送方,一般与user相同
user = 'qianyue@supcon.com'  # 邮件发送方的用户
password = ''  # 邮件发送方的密码


# =====定义发送邮件=====
def send_mail(file_new):
    # 带附件形式（建议用这种方式）
    sendfile = open(file_new, 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="testreport.html"'  # 可以自行定义附件名称

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'TestReport'  # 可自行定义邮件标题
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

    # HTML格式发送
    """f=open(file_new,'rb')
    mail_body=f.read()
    msg=MIMEText(mail_body,'HTML','utf-8')
    msg['Subject']=Header('自动化测试报告11234','utf-8') #邮件标题名称
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender,receiver, msg.as_string())
    smtp.quit()"""


# =====获取最新的测试报告=====
def new_report(test_report):
    lists = os.listdir(test_report)
    '''sort按key的关键字进行升序排列，
    lambda的入参fn为列表lists的元素，获取文件的最后修改时间，
        所以文件最终以文件时间从小到大排序'''
    lists.sort(key=lambda fn: os.path.getmtime(test_report + fn))  # 去掉fn，如果同级目录有其他文件夹，那么会报错
    print(('最新文件为：' + lists[-1]))
    new_report = os.path.join(test_report, lists[-1])
    return new_report


def get_count():
    write_user_file = WriteUserCommand()
    return write_user_file.get_file_lines()


def appium_init():
    server = Server()
    server.main()


def get_suite(i):
    # test_dir = '../Case/'  # ./ 表示当前目录
    # test_report = '../report/'  # ../表示上一目录
    # suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)

    suite = unittest.TestSuite()

    suite.addTest(ParametrizedTestCase.parametrize(test_case.CaseTest, param=i))
    suite.addTest(ParametrizedTestCase.parametrize(test_case2.CaseTest, param=i))
    print("this is suite", suite)
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    write_file = WriteUserCommand()
    device = write_file.get_value('user_info_' + str(i), 'deviceName')
    html_file = "../report/testReport" + str(i) + now + ".html"
    with open(html_file, "wb") as fp:
        HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试", description=device + "的自动化测试结果").run(suite)


if __name__ == '__main__':
    appium_init()
    threads = []

    for i in range(get_count()):
        # 多进程
        t = multiprocessing.Process(target=get_suite, args=(i,))

        # 多线程 会混，可能2个模拟器，设计的是2个用例，一个模拟器执行1个用例，另一个模拟器执行3个用例
        # t = threading.Thread(target=get_suite, args=(i,))

        threads.append(t)

    for j in threads:
        j.start()

    # new_report = new_report(test_report)
    # send_mail(new_report)
