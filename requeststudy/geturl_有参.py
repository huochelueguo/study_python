# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:geturl_有参.py
@Time:NAME.py@Time:2020/7/9 17:11
"""
import requests
import json


def geturl(url, para):  # 仅需传入一个参数时，使用para接收传入参数即可

    res = requests.get(url, para)
    return res.text


def geturl2(url, data):

    res = requests.get(url, data)
    return res.text


res1 = geturl('http://test.api.pokekara.com/x/song/info', 'song_id=168443026', )
print(f'白日歌曲的信息为：')
print(res1)
data = {        # 传入多个参数时，可以字典组织，之后将字典传入
    'page_index': 1,
    'page_size': 5
}
res2 = geturl2('http://test.api.pokekara.com/x/song/feed/hq_total', data)
print('获取高质量伴奏前5条')
print(res2)
# 将str返回值转换为json
res2_json = json.loads(res2)
print(res2_json)

