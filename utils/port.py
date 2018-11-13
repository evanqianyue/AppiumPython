# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/13 10:44
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from dos_cmd import DosCmd


class Port(object):
    def port_is_used(self, port_num):
        """

        :param port_num: 断开
        :return: 端口是非被占用，True被占用 False未被占用
        """
        self.dos = DosCmd()
        self.port_num = str(port_num)
        result = self.dos.execute_cmd_result("netstat -ano|findstr " + self.port_num)
        if len(result) > 0:
            return True
        else:
            return False

    def creat_port_list(self, start_port, device_list):
        """
        生成可用端口
        :param start_port:开始端口
        :param device_list:设备列表
        :return:
        """
        self.start_port = int(start_port)

        port_list = []
        # if device_list is not None:
        if len(device_list) >= 0:
            while len(port_list) != len(device_list):
                if self.port_is_used(self.start_port) is not True:
                    port_list.append(self.start_port)
                self.start_port += 1

            return port_list

        else:
            print("生成可用端口失败")
            return None


if __name__ == '__main__':
    port = Port()
    li = [1, 2, 3, 4]
    # print(port.port_is_used("8888"))
    print(port.creat_port_list("8887", li))
