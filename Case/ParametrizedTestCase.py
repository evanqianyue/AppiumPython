# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/20 10:58
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import unittest


class ParametrizedTestCase(unittest.TestCase):
    """

     继承之后，重写一下，把这个参数传递到unittest里面

    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_class, param=None):
        testloader = unittest.TestLoader()

        testnames = testloader.getTestCaseNames(testcase_class)

        suite = unittest.TestSuite()

        for name in testnames:
            suite.addTest(testcase_class(name, param=param))

        return suite
