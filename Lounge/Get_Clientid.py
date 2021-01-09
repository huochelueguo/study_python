# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Get_Clientid.py
@Time:NAME.py@Time:2020/8/26 17:17
@歌房功能封装模块： 获取用户clientid
"""

# 导入的模块是websocket_client，相似的比较多，容易混淆
import json
import os
import yaml

from websocket import create_connection


class Get_Clientid(object):

    def __init__(self, token, uid):
        """
        类初始化时就连接ws
        :param token: 用户token
        :param uid: 对应用户uid
        """
        self.token = token
        self.uid = uid
        self.url = 'ws://test.api.pokekara.com/ws?' + 'uid=' + self.uid
        self.ws = create_connection(url=self.url, timeout=2000, cookie=self.token)

    def get_id(self):
        """
        连接ws后，获取对应uid的clientid，存储在一个列表里面，后续操作中使用
        """
        if self.ws.connected:
            res = self.ws.recv()
            dict_res = json.loads(res)
            dict_clientid = dict_res['track_id']
            return dict_clientid
        else:
            print('连接失败，请重试')

    def send_message(self,data):
        """
        发送消息接口
        """
        data_json = json.dumps(data, indent=4, ensure_ascii=False)
        self.ws.send(data_json)
        a = self.ws.recv()
        print(a)


if __name__ == '__main__':
    uid1 = 'u1592560688671743535'
    token1 = 'MTU5MjU2MDY4OHxEM3ZNd0poRkpvWkN6QmQwdU03aThDZWZaOW1qb0RMOHJUZGREci1xakIxMnlSX0gtRWt0Q1ZSREhLREU2RGUtMHpvNnVGNmhLeVJGdkRfa2x0aFM1YktYTGZ1RUNDbWZ8075exn7Hw5Gcrvm1wSkHHkAy'
    data = {
        "msg_id": "e21aaf6b-ef53-11ea-9e59-5254009bf4c3",
        "data": {
            "client_id": "b030ac51-ef5b-11ea-9e59-5254009bf4c3",
            "message_id": "2F221282D-BD5F-4854-8786-67C6DCC7CC42",
            "content": "12132",
            "type": 1,
            "room_id": "dc8823ba-23f7-11eb-8d3d-5254009bf4c3"
        },
        "command": 4003
    }
    user = Get_Clientid(token=token1, uid=uid1)
    user.send_message(data=data)