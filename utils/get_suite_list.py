# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/20 12:56
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import os
import sys
import re
import unittest
import time
import random


class GetSuiteList(object):
    def get_list(self):
        lists = []
        for fileName in os.listdir("./Case/"):
            # pattern = re.compile(r'^test_*?.$py')
            # result = pattern.findall(i)
            # if fileName.startswith("test_") and fileName.endswith(".py"):
            if re.findall("^test_.*?py$", fileName):
                filename = fileName.replace(".py", ".CaseTest")
                lists.append(filename)
        return lists


if __name__ == '__main__':
    print(GetSuiteList().get_list())
    # list2 = ['test_case.py', '1test_case.pyc', 'test_case.pyt', 'test_case2.py']
    # for i in list2:
    #     if re.findall("^test_.*?py$", i):
    #         print(i)
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
