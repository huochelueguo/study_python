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
                self.ws = ws
                res = ws.recv()
                dict_res = json.loads(res)
                dict_clientid = dict_res['track_id']
                return dict_clientid
        except Exception as result:
            print(result)

    # def send_message(self, data):
    #
    #     res = self.ws.send(data)
    #     return res


if __name__ == '__main__':
    uid = 'u1592560688671743535'
    token = 'MTU5MjU2MDY4OHxEM3ZNd0poRkpvWkN6QmQwdU03aThDZWZaOW1qb0RMOHJUZGREci1xakIxMnlSX0gtRWt0Q1ZSREhLREU2RGUtMHpvNnVGNmhLeVJGdkRfa2x0aFM1YktYTGZ1RUNDbWZ8075exn7Hw5Gcrvm1wSkHHkAy'
    a = Get_Client(token, uid).GET_Id()
    print(a)
    print(type(a))
    # data1 = {
    #   "command": 4003,
    #   "data": {
    #     "room_id": "0ef3b23b-eeb1-11ea-b5d0-5254009bf4c3",
    #     "uid": "u1592560688671743535",
    #     "type": 1,
    #     "client_id": "16fe9514-eeb1-11ea-9e59-5254009bf4c3",
    #     "content": "???"
    #   },
    #   "msg_id": "9ba6d529-e7ee-468b-aec3-a96dd1f99624"
    # }
    # a = Get_Client(token='', uid='').send_message(data=data1)

