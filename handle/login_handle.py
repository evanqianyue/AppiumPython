# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/12 11:02
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from page.login_page import LoginPage


class LoginHandle:
    def __init__(self, i):
        self.login_page = LoginPage(i)

    # 操作登录页面的元素
    def send_username(self, username):
        """

        :param username: 用户名
        :return: 无
        """
        self.login_page.get_username_element().send_keys(username)

    def send_password(self, password):
        """

        :param username: 用户名
        :return: 无
        """
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        """

        :return: 无
        """
        self.login_page.get_login_button_element().click()

    def click_register(self):
        """

        :return: 无
        """
        self.login_page.get_register_element().click()

    def click_forget_password(self):
        """

        :return:
        """
        self.login_page.get_forget_password_element().click()

    def get_fail_toast(self, message):
        """

        :return:获取toast，根据返回信息进行反数据
        """
        toast_element = self.login_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False
