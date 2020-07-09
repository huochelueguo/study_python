# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:posturl.py
@Time:NAME.py@Time:2020/7/9 17:59
"""
# 模拟登录接口
import requests
import json


def login_phone(url, data):

    res = requests.post(url, data)

    return res.text


url = 'http://test.api.pokekara.com/api/user/login'
body = {'platform': 4,
        'token': 'login',
        'id_token': '+8618500616906',
        'secret': '111111'
        }
respone = login_phone(url, body)    # 将传入body放入字典中一起传入
# 返回值为json,通过json.loads转换为字典，可以进行操作
# print(respone)
# print(type(respone))
dict_res = json.loads(respone)
print(dict_res)
print(type(dict_res))
print(f'用户的token为：')
print(dict_res['data']['poke_session_id'])
