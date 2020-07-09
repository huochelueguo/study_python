# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:geturl_无参.py
@Time:NAME.py@Time:2020/7/9 16:52
"""
# get方法：
# 无参时，只需要发送url即可
import requests


def geturl(url):

    response = requests.get(url)
    return response.text


res = geturl('http://test.api.pokekara.com/x/song/feed/latest')
print(type(res))
print(res)
