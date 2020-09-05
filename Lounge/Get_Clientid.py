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
        self.ws = create_connection(url=self.url, timeout=100, cookie=self.token)


    # def GET_Id(self):
    #     try:
    #         ws = create_connection(url=self.url, timeout=100, cookie=self.token)
    #         if ws.connected:
    #             res = ws.recv()
    #             ws.send()
    #             dict_res = json.loads(res)
    #             dict_clientid = dict_res['track_id']
    #             return dict_clientid
    #     except Exception as result:
    #         print(result)

    def get_id(self):
        if self.ws.connected:
            res = self.ws.recv()
            dict_res = json.loads(res)
            dict_clientid = dict_res['track_id']
            return dict_clientid
        else:
            print('连接失败，请重试')

    def send_message(self,data):

        # if self.ws.connected:
        data_json = json.dumps(data, indent=4, ensure_ascii=False)
        a =self.ws.send(data_json)
        print(a)
        # else:
        #     print('连接失败，请重试')


if __name__ == '__main__':
    uid = 'u1592560688671743535'
    token = 'MTU5MjU2MDY4OHxEM3ZNd0poRkpvWkN6QmQwdU03aThDZWZaOW1qb0RMOHJUZGREci1xakIxMnlSX0gtRWt0Q1ZSREhLREU2RGUtMHpvNnVGNmhLeVJGdkRfa2x0aFM1YktYTGZ1RUNDbWZ8075exn7Hw5Gcrvm1wSkHHkAy'
    # a = Get_Client(token, uid).get_id()
    # print(a)
    # print(type(a))
    data = {
        "msg_id": "2F05C12E-BB12-4A9E-A1CB-1148160FC741",
        "data": {
            "client_id": "49b14e99-eecc-11ea-9e59-5254009bf4c3",
            "message_id": "2FD0282D-BD5F-4854-8786-67C6DCC7CC42",
            "content": "123",
            "type": 1,
            "room_id": "2b302227-eecc-11ea-b5d0-5254009bf4c3"
        },
        "command": 4003
    }
    Get_Client().send_message(data=data)