# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/20 11:00
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from ParametrizedTestCase import ParametrizedTestCase
import unittest
from qy_1 import Test01


class TestOne(ParametrizedTestCase):

    def test_first(self):
        print('param =', self.param)
        self.assertEqual(1, 1)

    def test_two(self):
        print('param =', self.param)
        self.assertEqual(2, 2)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=1))

    suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=2))
    suite.addTest(ParametrizedTestCase.parametrize(Test01, param=3))

    unittest.TextTestRunner(verbosity=2).run(suite)
