# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Join_Lounge.py
@Time:NAME.py@Time:2020/8/26 18:59
"""
# 加入房间接口，使用TOKEN/CLIENT_ID/room_id调用join接口
import time

import jsonpath
import requests
import json
import os
import yaml

from Lounge.Get_Clientid import Get_Clientid
from Lounge.Read_Usertoken import Read_Uid_Token

ROOM_NID = 1499626993153572864
ROOM_ID = '0d28518f-9b81-11ec-b37f-5254002d7e9a'
CLIENTID_PATH = 'E:/pythonworkspace/python_study/Lounge/user_data/clientid'


class Post(object):
    """
        加房post接口
    """

    def __init__(self, token, client_id, room_id):
        self.token = 'poke_session_id=' + token
        self.client_id = client_id
        self.room_id = room_id

    def post_join(self):
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


class Join_Lounge(object):
    """
        获取用户uid和token，再去请求client_id，之后去请求加房接口
    data_uid: uid列表
    data_token： token列表
    data_clientid： clientid列表
    """

    def join(self, data_file, room_id):
        # 获取用户uid和token
        data = Read_Uid_Token(data_file).read()
        data_uid = data[0]
        data_token = data[1]
        # 获取用户clientid
        data_clientid = []
        for i in range(len(data_uid)):
            id = Get_Clientid(data_token[i], data_uid[i]).get_clientid()
            data_clientid.append(id)
            # 输出client_id到文件中，后续其他操作可能会用到
            curr_path = os.path.split(__file__)[0]
            data_path = curr_path + '/user_data/clientid'
            with open(data_path, 'w', encoding='utf-8')as f:
                yaml.dump(data_clientid, f)
            # 使用clientid和token加入歌房
            try:
                res = Post(token=data_token[i], client_id=data_clientid[i], room_id=room_id).post_join()
            except Exception as result:
                print(f'join err:{result}')
        return res


if __name__ == '__main__':
    Join_Lounge().join(data_file='user_1', room_id=ROOM_ID)
