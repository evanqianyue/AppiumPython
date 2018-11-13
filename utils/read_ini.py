# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/12 9:10
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import configparser
#
# read_ini = configparser.ConfigParser()
# read_ini.read("../config/LocalElement.ini")
# print(read_ini.get('login_element', 'username'))


class ReadIni(object):

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = "../config/LocalElement.ini"
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read("../config/LocalElement.ini")
        return read_ini

    # 通过key获取对应的value
    def get_value(self, key, section=None):
        if section is None:
            section = "login_element"
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value("password2"))
