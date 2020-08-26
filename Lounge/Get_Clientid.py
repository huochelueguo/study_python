# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Get_Clientid.py
@Time:NAME.py@Time:2020/8/26 17:17
"""
# 获取用户clent_id值

# 导入的模块是websocket_client，相似的比较多，容易混淆
import json
from websocket import create_connection


class Get_Client(object):

    def __init__(self, token, uid):
        self.token = token
        self.uid = uid
        self.url = 'ws://test.api.pokekara.com/ws?' + 'uid=' + self.uid

    def GET_Id(self):
        try:
            ws = create_connection(url=self.url, timeout=100, cookie=self.token)
            if ws.connected:
                res = ws.recv()
                dict_res = json.loads(res)
                dict_clientid = dict_res['track_id']
                return dict_clientid
        except Exception as result:
            print(result)


if __name__ == '__main__':
    uid = 'u1592560688671743535'
    token = 'MTU5MjU2MDY4OHxEM3ZNd0poRkpvWkN6QmQwdU03aThDZWZaOW1qb0RMOHJUZGREci1xakIxMnlSX0gtRWt0Q1ZSREhLREU2RGUtMHpvNnVGNmhLeVJGdkRfa2x0aFM1YktYTGZ1RUNDbWZ8075exn7Hw5Gcrvm1wSkHHkAy'
    a = Get_Client(token, uid).GET_Id()
    print(a)
    print(type(a))

