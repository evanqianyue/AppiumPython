# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/13 14:06
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import yaml


class WriteUserCommand():
    def read_data(self):
        """
        获得yaml数据
        :return: 数据
        """
        with open('../config/userconfig.yaml', 'r', encoding="utf-8") as f:
            data = yaml.load(f)
        return data

    def get_value(self, key1, key2):
        data = self.read_data()
        value = data[key1][key2]
        return value

    def write_data(self, i, port, bp, device):
        """
        写入数据
        :return:
        """

        data = self.join_data(i, port, bp, device)
        with open('../config/userconfig.yaml', 'a', encoding="utf-8") as f:
            yaml.dump(data, f)

    def join_data(self, i, port, bp, device):
        data = {
            "user_info_" + str(i): {
                "port": port,
                "bp": bp,
                "deviceName": device

            }
        }
        return data

    def clear_data(self):
        with open('../config/userconfig.yaml', 'w', encoding="utf-8") as f:
            f.truncate()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)


if __name__ == '__main__':
    write_file = WriteUserCommand()
    # print(write_file.get_value('user_info_2', 'bp'))
    write_file.write_data("0", "3304", "3305", "127.0.0.1:5555")
