# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:send_danmu.py
@Time:NAME.py@Time:2020/12/2 16:40
"""
# encoding: utf8

import json
import random
import requests


url = 'http://test.api.pokekara.com/x/comment/publish?v=2.6.0'
session = requests.Session()
headers = {
    'Cookie': 'poke_session_id=MTYwNjkwMDY2MXw0NWxLTllZeTZLNURPMzY2UldTc0M2TU1pZmZSWTRCRkJfVWI5d1FNRW92c0liU19ZXzl3Q25Tc1NFVFExTTJFU0YxLVdXdzFjS0RfNkI5cFZXR0VtU0RHU1l1bVBTQzB8KFFs-qsUceqEPNABfzGlxizu1mGtXGCI4yfK-HZsabY=',
    'content-type': 'application/json'
}
dps = 4  # danmaku per second
duration = 150  # 最多 150s
mv_id = 1326783430907592704


def danmaku_payload(mv_id, time_ms, text, position=0, font_size=0):
    payload = {'content_type': 0, 'comment_moment': -1, 'comment_type': 0, 'color_scheme': 0, 'publish_type': 1,
               'time_point': time_ms, 'comment_to': mv_id, 'content': text, 'content_position': position,
               'content_font_size': font_size}
    return payload


def generate_text():
    t0 = random.choice(['QA', 'iOS', 'Android'])
    t1 = random.choice(['深情的', '愤怒的', '萌萌的', "很长很长很长很长的"])
    t2 = random.choice(['说', '打', '唱'])
    t3 = random.choice(['呆瓜', '呵呵', '**'])
    return ''.join([t0, t1, t2, t3])


for x in range(0, int(duration * dps)):
    seconds = x / dps
    text = generate_text()
    time_ms = int(seconds * 1000) + random.randint(0, 999)
    p = danmaku_payload(mv_id, time_ms, text, position=1)
    resp = session.post(url, headers=headers, data=json.dumps(p))
    try:
        data = resp.json()
        code = data['err_code']
        err_data = data['err_msg']
        if code != 0:
            print(f'{text}{time_ms} send failed: {err_data}')
        else:
            print(f'{text}{time_ms} send success')
    except Exception as e:
        print(e)
