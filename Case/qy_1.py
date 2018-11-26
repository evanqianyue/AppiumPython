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


class Test01(ParametrizedTestCase):
    def test_01_case(self):
        print("这个是test01case里面的参数", self.param)

    def test_02_case(self):
        print("这个是test01case里面的参数", self.param)
