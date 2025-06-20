#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2025/6/18 16:38
# @Author : sunwenxiao
# @File : ten_game.py
# @Software: PyCharm

# 商城十连抽

import time
from random import random

import requests


headers = {
    'Host': 'test.api.pokekara.com',
    'x-poke-session-id': 'MTc1MDQwMjU3M3xDay02MkdveUZBSmFNeFdkWG5sMXg4WXBqSUY5M1d6RDFDRmxFcDYwT08xTDJjdGVRMDg0c1pQSTE5d3F6U09yQ2NnVzlPVFlONFRiUzc4Tldvd2dTaHF1TTVWSHdleVZ84Gw28z0nGqRrghlx8VaBRsPpoF-EslA4b_kPC_rgH2k=',
    'Origin': 'https://test.api.pokekara.com'}

params = {
    'request_id': '1750235825282158',
    'series_id': '1001',
    'series_level_id': '10006',
}

json_data = {
    'lottery_id': 10003,
    'lottery_type': 2,
}


for i in range(100):
    response = requests.post(
        'https://test.api.pokekara.com/x/mall/lottery/start',
        params=params,
        headers=headers,
        json=json_data,
    )
    print(f'当前执行第{i+1}次')
    print(response.json())
    time.sleep(1)