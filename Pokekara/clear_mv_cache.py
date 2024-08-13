#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2024/8/13 15:32
# @Author : sunwenxiao
# @File : clear_mv_cache.py
# @Software: PyCharm
import requests

# 清除MV缓存


file_path = '/Users/sunwenxiao/Downloads/export_result.txt'
mv_list = []
with open(file_path) as f:
    txt = f.readlines()
for i in txt[1::]:
    mv_list.append(i.replace('\n', ''))


def clear_mv_cache(mv_id):
    url = 'https://api.pokekara.com/x/__debug__/clear_mv_mc?mv_id='
    clear_url = url + mv_id
    response = requests.get(clear_url)
    return mv_id, response.text


for i in mv_list:
    print(clear_mv_cache(i))