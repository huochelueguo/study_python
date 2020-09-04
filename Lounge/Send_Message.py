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
from websocket import create_connection

from Lounge.Join_Lounge import Join_Lounge
from Lounge.Get_Clientid import Get_Client


message = [
        "こんにちは！",
        "よろしくお願いします！",
        "うまい！",
        "やばい！",
        "www",
        "こんばんは！",
        "うんうん",
        "お邪魔します！",
        "いらっしゃい",
        "可愛い",
        "ありがとう！",
        "最高！",
        "はじめまして！",
        "初見です",
        "いいね！",
        "お疲れ様",
        "(′^ω^｀)",
        "(*・ω・)ﾉ",
        "(´ー｀*)"]
Join_Lounge().join(data_file='user_18', room_id='99b3a814-ee9a-11ea-adfb-5254009bf4c3')
