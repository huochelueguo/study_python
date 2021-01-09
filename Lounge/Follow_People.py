# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Follow_People.py
@Time:NAME.py@Time:2020/12/14 14:30
歌房内批量关注用户【房主】
"""
import json
import uuid

import jsonpath
import requests

from Join_Lounge import Join_Lounge
from Lounge.Get_Clientid import Get_Clientid
from Read_Usertoken import Read_Uid_Token
from Lounge.Send_Message import Read_Client


class Follow_People(object):

    def __init__(self, room_id, user_data, owner_uid=None):
        """

        :param room_id: 房间ID
        :param user_data: 加入房间用户数据
        :param owner_uid: 房主UID
        """
        self.romm_id = room_id
        self.userdata = user_data
        self.owner_uid = owner_uid

    def follow_owner(self):
        client_list = Read_Client().read_clientid()
        uid_token = Read_Uid_Token(self.userdata).read()
        uid = uid_token[0]
        token = uid_token[1]
        # cookie =
        for i in range(len(uid)):
            # 先调用follow接口关注用户
            url = 'http://test.api.pokekara.com/api/user/relationship/follow'
            header = {'Content-Type': 'application/x-www-form-urlencoded',
                      'cookie': 'poke_session_id=' + token[i],
                      }
            body = {"t_uid": self.owner_uid,
                    "refer": 'lounge'
                    }
            try:
                res = requests.post(url=url, data=body, headers=header)
                data = res.json()
            except Exception as result:
                print(f'{result}')
            if 'success' == jsonpath.jsonpath(data, '$..err_msg')[0]:
                # 再调用websoeket发送4031
                websocket_data = {
                    "msg_id": str(uuid.uuid4()),
                    "data": {
                        "client_id": client_list[i],
                        "message_id": str(uuid.uuid1()),
                        "to_uid": self.owner_uid,
                        "type": 0,
                        "room_id": self.romm_id
                    },
                    "command": 4031
                }
                try:
                    ws = Get_Clientid(token=token[i], uid=uid[i])
                    ws.send_message(data=websocket_data)
                except Exception as e:
                    print(f'{e}')
            else:
                print('api关注失败')


if __name__ == '__main__':
    room_id = "7b61ef0b-3f8b-11eb-9c4b-5254009bf4c3"
    owner_uid = 'u1237326482846568448'
    # 加入房间
    res_data = Join_Lounge().join(data_file='user_50', room_id=room_id)
    lounge_status = json.loads(res_data)
    close_tip = "このルームは終了しました！他のルーム見てみましょう！"
    res_tip = jsonpath.jsonpath(lounge_status, '$..tip')
    # print(jsonpath.jsonpath(lounge_status, '$..tip'))
    if not res_tip:
        Follow_People(room_id=room_id, user_data='user_50', owner_uid=owner_uid).follow_owner()
    elif close_tip == res_tip[0]:
        print('房间已关闭')



