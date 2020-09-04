# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Read_Usertoken.py
@Time:NAME.py@Time:2020/9/4 17:13
@从user_data中读取已有的用户id和token，返回元组
"""
import os
import yaml


class Read_Uid_Token(object):

    def __init__(self, path):
        curr_path = os.path.split(__file__)[0]
        data_path = curr_path + '/user_data/' + path
        self.path = data_path

    def read(self):
        with open(self.path, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data[0].get('uid_list'), data[1].get('token_list')


if __name__ == '__main__':
    r = Read_Uid_Token('user_18').read()
    print(r)