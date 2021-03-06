# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/12 11:22
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import unittest
import HTMLTestRunner
import threading
import multiprocessing
from utils.server import Server
from business.login_business import LoginBusiness
from utils.write_user_command import WriteUserCommand
import time
import random
import sys


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParameTestCase, self).__init__(methodName)
        global params
        params = param


class CaseTest(ParameTestCase):

    @classmethod
    def setUpClass(cls):
        print("setupclass---->", params)
        cls.login_business = LoginBusiness(params)

    def setUp(self):
        print("this is setup\n")

    def test_01(self):
        self.login_business.login_password_fail()

    def test_02(self):
        self.login_business.login_user_fail()

    def test_03(self):
        # self.login_business.login_password_fail()
        self.assertTrue(False, "it's fasle")

    def tearDown(self):
        print("this is tearDown\n")
        # 这个是Python2的用法，Python3无效
        if sys.exc_info()[0]:
            seed = int(random.random() * 1000)
            now = time.strftime('%Y-%m-%d %H_%M_%S')
            screenshotName = "./screenshots/" + now + "test_03"+"Seed" + str(seed) + ".png"
            print("screenshotName:", screenshotName.split('./screenshots/')[1])
            self.login_business.login_handle.login_page.driver.save_screenshot(screenshotName)

    @classmethod
    def tearDownClass(cls):
        print("this is class tearDown\n")


def get_suite(i):
    print("get_suite里的", i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", param=i))
    suite.addTest(CaseTest("test_02", param=i))
    suite.addTest(CaseTest("test_03", param=i))
    # unittest.TextTestRunner().run(suite)

    write_file = WriteUserCommand()
    device = write_file.get_value('user_info_' + str(i), 'deviceName')
    html_file = "../report/testReport" + str(i) + ".html"
    with open(html_file, "wb") as fp:
        HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试", description=device + "的自动化测试结果").run(suite)


def appium_init():
    server = Server()
    server.main()


def get_count():
    write_user_file = WriteUserCommand()
    return write_user_file.get_file_lines()


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(CaseTest("test_01"))
    # suite.addTest(CaseTest("test_02"))

    # html_file = "../report/result.html"
    # with open(html_file, "wb") as fp:
    #     HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试", description="描述").run(suite)
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
        # time.sleep(3)
