# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/11 13:05
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""


# import sys
# sys.path.append("../AppiumPython")
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.read_ini import ReadIni
from utils.get_by_local import GetByLocal


def get_driver():
    capabilities = {
        "platformName": "Android",
        # "automationName": "UiAutomator2",
        "deviceName": "127.0.0.1:21503",
        "app": "D:\\appsfortest\\mukewang.apk",
        # "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
        # "recreateChromeDriverSessions": "true",
        "noReset": "True"

    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver


# 获取屏幕宽高
def get_size():
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    return width, height


# 定义向左滑动方法
def swipe_left():
    # (100,200)
    x1 = get_size()[0] * 9 / 10
    y = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y, x, y)


# 定义向右滑动方法
def swipe_right():
    # (100,200)
    x = get_size()[0] / 10
    y = get_size()[1] / 2
    x1 = get_size()[0] * 9 / 10
    driver.swipe(x, y, x1, y)


# 定义向上滑动方法
def swipe_up():
    # (100,200)
    x = get_size()[0] / 2
    y = get_size()[1] * 5 / 10
    y1 = get_size()[1] / 10
    driver.swipe(x, y, x, y1)


# 定义向下滑动方法
def swipe_down():
    # (100,200)
    x = get_size()[0] / 2
    y = get_size()[1] * 9 / 10
    y1 = get_size()[1] / 10
    driver.swipe(x, y1, x, y)


def swipe_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    else:
        swipe_right()


def go_login():
    print(driver.find_element_by_id("cn.com.open.mooc:id/tv_go_login"))
    driver.find_element_by_id("cn.com.open.mooc:id/tv_go_login").click()


def go_login_by_class():
    # driver.find_element_by_class_name('android.widget.TextView').click()
    element = driver.find_element_by_class_name('android.widget.TextView')
    print(element)
    elements = driver.find_elements_by_class_name('android.widget.TextView')
    print(len(elements))
    elements[4].click()


def login():
    driver.find_element_by_id("cn.com.open.mooc:id/account_edit").send_keys("544649790@qq.com")
    driver.find_element_by_id("cn.com.open.mooc:id/password_edit").send_keys("qianyue1003")
    driver.find_element_by_id("cn.com.open.mooc:id/login").click()


def login_utils():
    get_by_local = GetByLocal(driver)
    get_by_local.get_element('username').send_keys("544649790@qq.com")
    get_by_local.get_element('password').send_keys("qianyue1003")
    # time.sleep(3)
    # 不要加"automationName": "UiAutomator2",
    # get_by_local.get_element('password2').send_keys("password2")

    get_by_local.get_element('login_button').click()


def login_by_node():
    element = driver.find_element_by_id("cn.com.open.mooc:id/sv_scrollview")
    elements = driver.find_elements_by_class_name("android.widget.EditText")
    elements[0].send_keys("544649790@qq.com")
    elements[1].send_keys("qianyue1003")
    driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()


def login_by_uiautomator():
    driver.find_element_by_android_uiautomator('new UiSelector().text("544649790@qq.com")').clear()
    driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').send_keys("12111")
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').send_keys("21003")
    driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()


def login_by_xpath():
    # driver.find_element_by_xpath('//*[contains(@text,"忘记")]').click()
    # driver.find_element_by_xpath('//android.widget.TextView[@text="忘记密码"]').click()
    driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::*[@index="2"]').send_keys("123123")


def get_web_view():
    time.sleep(10)
    webview = driver.contexts
    print(webview)
    for view in webview:
        if view == 'WEBVIEW_cn.com.open.mooc':
            print(view)
            driver.switch_to.context(view)
            print("^^")
            break

    try:
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
    except Exception as e:
        driver.switch_to.context(webview[0])
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
        raise e
    print(view)


def get_toast():
    driver.find_element_by_id("cn.com.open.mooc:id/account_edit").send_keys("544649790@qq.com")
    tost_element = ("xpath", '//*[contains(@text,"请输入密码")]')
    print(WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(tost_element)))


driver = get_driver()
# driver.wait_activity("cn.com.open.mooc.index.splash.GuideActivity", 3)
# swipe_on("left")
# time.sleep(1)
# swipe_on("left")
# time.sleep(1)
# swipe_on("right")
# time.sleep(1)
# swipe_on("left")
# time.sleep(1)
# swipe_on("up")
# time.sleep(5)
# go_login()
# go_login_by_class()
# login()
# login_by_node()
# login_by_uiautomator()
# login_by_xpath()
# get_web_view()
time.sleep(10)
login_utils()
