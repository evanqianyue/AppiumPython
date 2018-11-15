# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/12 10:42
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from utils.get_by_local import GetByLocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver


class LoginPage(object):
    # 获取登录页面所有页面元素信息
    def __init__(self, i):
        base_driver = BaseDriver()
        # self.driver = base_driver.get_driver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        """

        :return: 用户名输入框元素
        """
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        """

        :return: 密码输框元素
        """
        return self.get_by_local.get_element('password')

    def get_login_button_element(self):
        """

        :return: 登录按钮元素
        """
        return self.get_by_local.get_element('login_button')

    def get_forget_password_element(self):
        """

        :return: 忘记密码元素
        """
        return self.get_by_local.get_element('forget_password')

    def get_register_element(self):
        """

        :return: 忘记密码元素
        """
        return self.get_by_local.get_element('register')

    def get_toast_element(self, message):
        """

        :param message: 验证信息
        :return: toast元素
        """
        toast_element = ("xpath", "//*[contains(@text," + message + ")]")
        print(WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(toast_element)))
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(toast_element))
