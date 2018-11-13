# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/13 9:11
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from appium import webdriver
import time
from utils.write_user_command import WriteUserCommand


class BaseDriver(object):
    def android_driver(self, i):
        # devicename
        # port
        print("this is android_driver", i)
        write_file = WriteUserCommand()
        device = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')

        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": device,
            "app": "D:\\appsfortest\\mukewang.apk",
            # "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
            # "recreateChromeDriverSessions": "true",
            "noReset": "True"
        }

        driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub", capabilities)
        time.sleep(10)
        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        pass
