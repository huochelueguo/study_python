# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Send_Message_Threading.py
@Time:NAME.py@Time:2021/1/9 18:06
@ 多线程发送评论：使用uid获取clientid，将用户的uid/token/clientid组成一组数据，N组数据组成一个线程，分别取触发send_message
"""
import time
import uuid
import random
import threading
from Lounge.Get_Clientid import Get_Clientid
from Lounge.Join_Lounge import Join_Lounge, ROOM_ID, CLIENTID_PATH
from Lounge.User_Add_Clientid import Add_Clientid


message = ["こんにちは！", "よろしくお願いします！", "うまい！", "やばい！", "www", "こんばんは！", "うんうん", "お邪魔します！",
           "いらっしゃい", "可愛い", "ありがとう！", "最高！", "はじめまして！", "初見です", "いいね！", "お疲れ様", "(′^ω^｀)",
           "666", "太牛逼了，必须赞一个", "给力！！！！", "小老弟儿，来跟华子不"]


class Send_Mess_Threading(object):

    def __init__(self,  user_data, room_id, thread_count=None,):
        self.thred_count = thread_count
        self.user_data = user_data
        self.room_id = room_id

    def send_txt(self):
        while True:
            send_message = random.choice(message)
            data = {
                "msg_id": str(uuid.uuid4()),
                "data": {
                    "client_id": self.user_data[2],
                    "message_id": str(uuid.uuid1()),
                    "content": send_message,
                    "type": 1,
                    "room_id": self.room_id
                },
                "command": 4003
            }
            try:
                ws = Get_Clientid(token=self.user_data[1], uid=self.user_data[0])
                ws.send_message(data=data)
                print(f'{self.user_data[0]} + success')
            except Exception as result:
                print(result)

    def send_thread(self):
        thread_list = []
        for i in range(self.thred_count):
            thread_list.append(threading.Thread(target=self.send_txt))
        for t in thread_list:
            # print(data)
            # print(thread_list)
            time.sleep(0.5)
            t.start()


if __name__ == '__main__':
    user_path = 'user_50'
    thread_count = 5
    clientid_path = CLIENTID_PATH
    room_id = ROOM_ID
    # 加入房间
    Join_Lounge().join(data_file=user_path, room_id=room_id)
    data = Add_Clientid(user_path=user_path, clientid_path=clientid_path).uid_token_clientid()
    for i in range(thread_count):
        Send_Mess_Threading(thread_count=thread_count, user_data=data[i], room_id=room_id).send_thread()


