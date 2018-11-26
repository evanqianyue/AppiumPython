# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/13 10:34
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

from dos_cmd import DosCmd
from port import Port
import threading
import time
from write_user_command import WriteUserCommand


class Server(object):
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_device()
        # self.command_list = self.create_command_list()
        self.write_file = WriteUserCommand()

    def get_device(self):
        """

        :return: 设备信息
        """
        device_list = []
        result_list = self.dos.execute_cmd_result("adb devices")
        if len(result_list) > 1:
            for i in result_list:
                if 'List' in i:
                    continue
                else:
                    device_info = i.split("\t")
                    if device_info[1] == 'device':
                        device_list.append(device_info[0])
            return device_list
        else:
            return None

    def create_port_list(self, start_port):
        """
        创建可用端口
        :return:
        """
        port = Port()
        port_list = port.creat_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        # appium -p 4700 -bp 4701 -U 127.0.0.1:21503

        command_list = []
        appium_post_list = self.create_port_list(4700)
        bootstrap_post_list = self.create_port_list(5700)
        device_list = self.device_list
        # for i in range(len(device_list)):
        command = "appium -p " + str(appium_post_list[i]) + " -bp " + str(bootstrap_post_list[i]) + " -U " + str(
            device_list[i]) + " --no-reset --session-override"

        # 带日志
        # command = "appium -p " + str(appium_post_list[i]) + " -bp " + str(bootstrap_post_list[i]) + " -U " + str(
        #     device_list[i]) + " --no-reset --session-override --log D:/test02.log"

        command_list.append(command)
        self.write_file.write_data(i, appium_post_list[i], bootstrap_post_list[i], device_list[i])
        return command_list

    def start_server(self, i):
        self.start_list = self.create_command_list(i)
        self.dos.execute_cmd(self.start_list[0])

    def main(self):
        thread_list = []
        self.kill_server()
        self.write_file.clear_data()

        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
            print("Appium Server: %d start ok!" % i)
            # appium_start.start()
        for t in thread_list:
            t.start()

        # 时间太短会导致已经开始运行测试套件，但是Appium未完全启动
        time.sleep(25)

    def kill_server(self):
        server_list = self.dos.execute_cmd_result("tasklist | findstr node.exe")
        if len(server_list) > 0:
            self.dos.execute_cmd("taskkill -F node.exe")


if __name__ == '__main__':
    server = Server()
    # print(server.get_device())
    # print(server.create_port_list(8887))
    # print(server.create_command_list())
    server.main()
    # server.kill_server()
