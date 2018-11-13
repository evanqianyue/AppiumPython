# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/13 9:40
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import os


class DosCmd(object):

    def execute_cmd_result(self, command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            else:
                result_list.append(i.strip("\n"))
        return result_list

    def execute_cmd(self, command):
        os.system(command)


if __name__ == '__main__':
    dos = DosCmd()
    # print(os.popen("netstat -ano|findstr 8080").readlines())
    print(dos.execute_cmd_result("adb devices"))
    dos.execute_cmd("appium -p 4701 -bp 5700 -U 127.0.0.1:21513 --no-reset --session-override")
