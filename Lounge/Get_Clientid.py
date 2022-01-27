# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Get_Clientid.py
@Time:NAME.py@Time:2020/8/26 17:17
"""

# 导入的模块是websocket_client，相似的比较多，容易混淆
import json
from websocket import create_connection


class Get_Clientid(object):
    """
        歌房功能封装模块： 获取用户clientid
    """

    def __init__(self, token, uid):
        """
        类初始化时就连接ws
        :param token: 用户token
        :param uid: 对应用户uid
        """
        self.token = 'poke_session_id=' + token
        self.uid = uid
        self.url = 'ws://test.api.pokekara.com/ws'
        self.ws = create_connection(url=self.url, timeout=2000, header={
            'Cookie': self.token,
            'User-Agent': 'okhttp/4.9.0'
        })
        self.command_9001 = self.ws.recv()

    def get_clientid(self):
        """
        连接ws后，获取对应uid的clientid，存储在一个列表里面，后续操作中使用
            ***注意： 此处的client_id取的是track_id，不是client_id***
        """
        if self.ws.connected:
            dict_res = json.loads(self.command_9001)
            dict_clientid = dict_res['track_id']
            return dict_clientid
        else:
            print('连接失败，请重试')

    def send_message(self, data):
        """
        发送消息接口
        """
        data_json = json.dumps(data, indent=4, ensure_ascii=False)
        self.ws.send(data_json)
        # print(f'ws请求体{data}')
        # a = self.ws.recv()
        # print(f'ws消息回执：{a}')


if __name__ == '__main__':

    uid1 = 'u1631851507772944570'
    token1 = 'poke_session_id=MTYzMTg1MTUwN3xtQ19YRE92eUVkMExnZldoT25uSXQ0aVZaYXB0bjNmc2d0UGdKLWh2RG9yTk1oZE9JcUtlT01yTlB2X1RVOXhpOV9yek9Gdi1Uc3BGYzlVMVQzS2dPdkFHRlBTSHVEeXF8rl6wiQ4pNO8cIjUDQBbBJBVYQgjqkR1TvM9sfKGwTTI='
    # token1 = 'poke_session_id=MTYzMTc5NzA5OHxpZWZnYnRpS2FIOVBrSGtIb3UzR3hPZkluRm9tZEFEVHExUGxnMzZ0aFdEWkJXS05ER1VCeHZudnFuWnl6clJxelBaNk45U3NkZTNFRkNQU1p0ZzFXd3Z2czVvSTF3cjd8-cgiYxBE13XVwX1PoLKLoccv9BeyafYsLejgPk6KiT4='
    user = Get_Clientid(token=token1, uid=uid1)
    data = {
        "msg_id": "e21aaf6b-ef53-11ea-9e59-5254009bf4c3",
        "data": {
            "client_id": user.get_clientid(),
            "message_id": "2F221282D-BD5F-4854-8786-67C6DCC7CC42",
            "content": "12132",
            "type": 1,
            "room_id": "f3b6d206-176b-11ec-8a1d-5254002d7e9a"
        },
        "command": 4003
    }
    print(data)
    # user.send_message(data=data)