# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/12 13:34
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import threading


def sum(a, b):
    print(a + b)


thread = []

for i in range(3):
    # print(i)
    t = threading.Thread(target=sum, args=(i, 2))
    thread.append(t)

for j in thread:
    j.start()
