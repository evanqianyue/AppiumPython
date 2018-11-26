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

    def test_001(self):
        self.login_business.login_password_fail()
        # flag1 = True
        # flag2 = False
        # print("test case01 里面的参数", params)
        # print("this is case01\n")
        # self.assertEqual(1, 2, "数据错误")
        # self.assertEqual([12, 13], [12, 13], "数据错误")
        # self.assertNotEqual([12, 13], [12, 14], "数据错误")
        # self.assertTrue(flag1, "it's fasle")
        # self.assertTrue(flag2, "it's false")

    def test_002(self):
        self.login_business.login_user_fail()
        # self.assertTrue(True, "it's fasle")
        # print("test case02 里面的参数", params)
        # print("this is case02\n")

    def test_003(self):
        # self.login_business.login_password_fail()
        self.assertTrue(False, "it's fasle")

    def tearDown(self):
        print("this is tearDown\n")

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

    for j in threads:
        j.join()
        #time.sleep(3)
