# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Join_Lounge.py
@Time:NAME.py@Time:2020/8/26 18:59
"""
# 加入房间接口，使用UID/TOKEN/CLIENT_ID调用join接口
import requests
import json
from Lounge.Get_Clientid import Get_Client

class Join_Lounge(object):

    def __init__(self, token, client_id, room_id):
        self.token = token
        self.client_id = client_id
        self.room_id = room_id


    def Post_Join(self):
        url = 'http://test.api.pokekara.com/x/lounge/join?'
        header = {'Content-Type': 'application/json',
                  'cookie': self.token,
                  }
        body = {"client_id": self.client_id,
                "room_id": self.room_id
                }
        json_body = json.dumps(body)
        res = requests.post(url=url, data=json_body, headers=header)
        return res.text

if __name__ == '__main__':
    uid = 'u1592560688671743535'
    token = 'poke_session_id=' +'MTU5MjU2MDY4OHxEM3ZNd0poRkpvWkN6QmQwdU03aThDZWZaOW1qb0RMOHJUZGREci1xakIxMnlSX0gtRWt0Q1ZSREhLREU2RGUtMHpvNnVGNmhLeVJGdkRfa2x0aFM1YktYTGZ1RUNDbWZ8075exn7Hw5Gcrvm1wSkHHkAy-INMx1yZYd1ExzKvwHA='
    client_id = Get_Client(token, uid).GET_Id()
    print(client_id)
    room_id = '42dab49a-e78e-11ea-9a68-5254009bf4c3'
    a = Join_Lounge(token, client_id, room_id).Post_Join()
    print(a)