# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:post_need_token.py
@Time:NAME.py@Time:2020/7/9 20:44
"""
import requests
import json


def posturl(url, headers, data):

    res = requests.post(url=url, headers=headers, data=data)
    return res.text

url = 'http://test.api.pokekara.com/api/user/relationship/follow'
header = {'cookie': 'poke_session_id=MTU5NDI5Njc5M3wtOTBGbVlhNFkzbjUtTE5fVzdjQ3oyci1GQTRuZlU1eFZsemxlanp5cUxxcXJFeFd0QzdfOGdGQmEyYTJMYlQyd0JvR08zVkxSTGlSMDNGRFFYMzRnUmhmTWpKcWRKSTV8N3iSb7cs1qS7uDw9jV1IOv_mt7bM9zITklMYjWYl12s='}
data = {'t_uid': 'u1188055067914391552'}
print(posturl(url, header, data))
