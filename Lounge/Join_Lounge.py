# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Join_Lounge.py
@Time:NAME.py@Time:2020/8/26 18:59
"""
# 加入房间接口，使用TOKEN/CLIENT_ID/room_id调用join接口
import requests
import json

from Lounge.Get_Clientid import Get_Client
from Lounge.Read_Usertoken import Read_Uid_Token


class Join_Lounge(object):

    def __init__(self, token, client_id, room_id):
        self.token = 'poke_session_id=' + token
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
    # 获取用户uid和token
    data = Read_Uid_Token('user_18').read()
    data_uid = data[0]
    data_token = data[1]
    # 获取用户clientid
    data_clientid = []
    for i in range(len(data_uid)):
        id = Get_Client(data_token[i], data_uid[i]).GET_Id()
        data_clientid.append(id)
    print(data_clientid)
    # 使用clientid和token加入歌房
    room_id = 'cf6123f5-ee94-11ea-9231-5254009bf4c3'
    for i in range(len(data_uid)):
        res = Join_Lounge(token=data_token[i], client_id=data_clientid[i], room_id=room_id).Post_Join()
        print(res)


