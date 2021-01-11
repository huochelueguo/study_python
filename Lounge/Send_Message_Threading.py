# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Send_Message_Threading.py
@Time:NAME.py@Time:2021/1/9 18:06
@ 多线程发送评论： 大致思路：使用uid获取clientid，将用户的uid/token/clientid组成一组数据，N组数据组成一个线程，分别取触发send_message
"""
import uuid
import random
from Get_Clientid import Get_Clientid
from Join_Lounge import Join_Lounge
from Lounge.Send_Message import Send
import threading
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
        # thread_1 = threading.Thread(target=self.send_txt())
        # thread_1.start()
        for i in range(self.thred_count):
            thread_list.append(threading.Thread(target=self.send_txt))
        for t in thread_list:
            print(data)
            print(thread_list)
            t.start()
        # for t in thread_list:
        #
        #     t.join()


if __name__ == '__main__':
    user_path = 'user_1'
    clientid_path = '/Users/sunwenxiao/PycharmProjects/study_python/Lounge/user_data/clientid'
    room_id = "592217b4-5360-11eb-8e43-5254009bf4c3"
    # 加入房间
    Join_Lounge().join(data_file=user_path, room_id=room_id)
    # 无限循环发送评论
    # while True:
    #     data = Add_Clientid(user_path=user_path, clientid_path=clientid_path).uid_token_clientid()
    #     print(data[0])
    #     data_1 = data[0]
    #     Send_Mess_Threading(thread_count=1, user_data=data_1, room_id=room_id).send_thread()
    data = Add_Clientid(user_path=user_path, clientid_path=clientid_path).uid_token_clientid()
    count = 2
    for i in range(count):
        Send_Mess_Threading(thread_count=count, user_data=data[i], room_id=room_id).send_thread()

    # thread_list = []
    # for i in range(count):
    #     # thread_list.append(Send_Mess_Threading(thread_count=count, user_data=data[i], room_id=room_id).send_txt())
    #     thread_list.append(threading.Thread(target=Send_Mess_Threading(user_data=data[i], room_id=room_id).send_txt()))
    #     print(thread_list)
    # for th in thread_list:
    #     th.start()
    # for t in thread_list:
    #     t.join()


