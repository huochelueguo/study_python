# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:Send_Message_Threading.py
@Time:NAME.py@Time:2021/1/9 18:06
@ 多线程发送评论： 大致思路：使用uid获取clientid，将用户的uid/token/clientid组成一组数据，N组数据组成一个线程，分别取触发send_message
"""
from Lounge.Send_Message import Send
import threading

class Send_Mess_Threading():

    def __init__(self, thread_count, user_data):
        self.thred_count = thread_count
        self.user_data = user_data

    def send_
