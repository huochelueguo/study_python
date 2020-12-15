# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Follow_People.py
@Time:NAME.py@Time:2020/12/14 14:30
歌房内批量关注用户【房主】
"""
import uuid
import requests

from Join_Lounge import Join_Lounge
from Lounge.Get_Clientid import Lounge
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
            requests.post(url=url, data=body, headers=header)

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
                ws = Lounge(token=token[i], uid=uid[i])
                ws.send_message(data=websocket_data)
            except Exception as e:
                print(f'{e}')


if __name__ == '__main__':
    room_id = "a136443d-3ecf-11eb-9498-5254009bf4c3"
    owner_uid = 'u1593329556843533000'
    # 加入房间
    Join_Lounge().join(data_file='user_1', room_id=room_id)
    # 关注房主
    Follow_People(room_id=room_id, user_data='user_1', owner_uid=owner_uid).follow_owner()

