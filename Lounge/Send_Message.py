# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Send_Message.py
@Time:NAME.py@Time:2020/9/4 17:59
@随机发送聊天消息
"""
import random
import uuid
import os
import yaml

from Lounge.Get_Clientid import Get_Clientid
from Lounge.Join_Lounge import Join_Lounge
from Lounge.Read_Usertoken import Read_Uid_Token

message = ["こんにちは！", "よろしくお願いします！", "うまい！", "やばい！", "www", "こんばんは！", "うんうん", "お邪魔します！",
           "いらっしゃい", "可愛い", "ありがとう！", "最高！", "はじめまして！", "初見です", "いいね！", "お疲れ様", "(′^ω^｀)",
           "666", "太牛逼了，必须赞一个", "给力！！！！", "小老弟儿，来跟华子不"]


class Read_Client(object):
    """
    从clientid文件中读取出clientid，返回列表
    """

    def read_clientid(self):
        curr_path = os.path.split(__file__)[0]
        client_path = curr_path + '/user_data/clientid'
        with open(client_path, 'r')as f:
            client_id = yaml.load(f, Loader=yaml.FullLoader)
        return client_id


class Send(object):

    def __init__(self, roomm_id, user_data):
        self.roomid = roomm_id
        self.userdata = user_data

    """
    发送文本接口
    """

    def send_txt(self):
        list = Read_Client()
        client_list = list.read_clientid()

        r = Read_Uid_Token(self.userdata).read()
        uid = r[0]
        token = r[1]
        # print(uid)
        # print(token)
        for i in range(len(uid)):
            # 随机读取评论内容
            content = random.choice(message)
            data = {
                "msg_id": str(uuid.uuid4()),
                "data": {
                    "client_id": client_list[i],
                    "message_id": str(uuid.uuid1()),
                    "content": content,
                    "type": 1,
                    "room_id": self.roomid
                },
                "command": 4003
            }
            try:
                ws = Get_Clientid(token=token[i], uid=uid[i])
                ws.send_message(data=data)
            except Exception as result:
                print('重新连接')
                Get_Clientid(token=token[i], uid=uid[i])


if __name__ == '__main__':
    room_id = "f3b6d206-176b-11ec-8a1d-5254002d7e9a"
    # 加入房间
    Join_Lounge().join(data_file='user_1', room_id=room_id)
    # 无限循环发送评论
    while True:
        roomid = room_id
        Send(roomid, user_data='user_1').send_txt()
