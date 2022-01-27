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

ROOM_ID = '4e5f9110-7f28-11ec-9fcb-5254002d7e9a'
CLIENTID_PATH = 'E:/pythonworkspace/python_study/Lounge/user_data/clientid'
ROOM_NID = 1486554403070758912


class Post(object):
    """
    加房post接口
    """

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


class Join_Lounge(object):
    """
    遍历获取数据后，调用加房接口，按照顺序加房
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
            id = Get_Clientid(data_token[i], data_uid[i]).get_id()
            data_clientid.append(id)
            # 输出client_id到文件中，后续其他操作可能会用到
            curr_path = os.path.split(__file__)[0]
            data_path = curr_path + '/user_data/clientid'
            with open(data_path, 'w', encoding='utf-8')as f:
                yaml.dump(data_clientid, f)
            # 使用clientid和token加入歌房
            try:
                res = Post(token=data_token[i], client_id=data_clientid[i], room_id=room_id).Post_Join()
            except Exception as result:
                print(f'{result}')
        # print(data_clientid)
        return res


if __name__ == '__main__':
    Join_Lounge().join(data_file='user_1', room_id="f3b6d206-176b-11ec-8a1d-5254002d7e9a")
