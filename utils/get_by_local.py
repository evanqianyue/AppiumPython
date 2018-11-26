# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/12 9:36
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from read_ini import ReadIni
import random
import time


class GetByLocal(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, section, key):
        read_ini = ReadIni()
        local = read_ini.get_value(section, key)
        if local is not None:
            by = local.split(">")[0]
            local_by = local.split(">")[1]
            try:
                if by == "id":
                    return self.driver.find_element_by_id(local_by)

                elif by == "class_name":
                    return self.driver.find_element_by_class_name(local_by)

                else:
                    return self.driver.find_element_by_xpath(local_by)

            except:
                # seed = int(random.random() * 1000)
                # now = time.strftime('%Y-%m-%d %H_%M_%S')
                # screenshotName = "./screenshots/" + now + "Seed" + str(seed) + ".png"
                # print("screenshotName:", screenshotName.split('./screenshots/')[1])
                # self.driver.save_screenshot(screenshotName)
                return None

        else:
            return None
