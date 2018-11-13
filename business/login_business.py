# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/12 11:11
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from handle.login_handle import LoginHandle


class LoginBusiness(object):
    def __init__(self, i):
        self.login_handle = LoginHandle(i)

    def login_pass(self):
        self.login_handle.send_username("544649790@qq.com")
        self.login_handle.send_password("qianyue1003")
        self.login_handle.click_login()

    def login_user_fail(self):
        self.login_handle.send_username("544649790!@qq.com")
        self.login_handle.send_password("qianyue1003!")
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost("账号未注册")
        return user_flag

    def login_password_fail(self):
        self.login_handle.send_username("544649790@qq.com")
        self.login_handle.send_password("qianyue1003!")
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost("登录密码错误")
        return user_flag
