#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2025/6/18 16:38
# @Author : sunwenxiao
# @File : ten_game.py
# @Software: PyCharm

# 商城十连抽

import time
import requests

cookies = {
    'tgw_l7_route': 'a484a508d5069fdd52bc57c0ce38b496',
    'poke_session_id': 'MTc1MDIzNDM5NnxYTWV1ZU4wWmcxOU9rRFgzRjVVUDg3UVhDZldTVHFDSlpoOWhoQzdBMlV1MVJxbE1GdFVITHllOUhpSlNySWRlaG9wLTFKbVJYRXJHdkxNclliY0p4ZFNxR2hwekd5RXl8Gw-EQaUUb7BpXEALxQiCQbxv9l6kBccm0KUv4PelZCM=',
}

headers = {
    'Host': 'test.api.pokekara.com',
    'x-poke-session-id': 'MTc1MDIzNDM5NnxYTWV1ZU4wWmcxOU9rRFgzRjVVUDg3UVhDZldTVHFDSlpoOWhoQzdBMlV1MVJxbE1GdFVITHllOUhpSlNySWRlaG9wLTFKbVJYRXJHdkxNclliY0p4ZFNxR2hwekd5RXl8Gw-EQaUUb7BpXEALxQiCQbxv9l6kBccm0KUv4PelZCM=',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://test.api.pokekara.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Referer': 'https://test.api.pokekara.com/webkara/static/dev/cli/mall/dist/lottery.html?series_id=1001&series_level_id=10006&nav_height=44.0&nav_y=47.0&theme_name=Dark&v=4.1.23&unique_device_id=7517199466077126935&e_flags=%5B%22new_lucky_turn_D%22%2C%22fake_lounge_A%22%2C%22member_song_group_D%22%2C%22server_groupC%22%2C%22servernew_groupB%22%2C%22consumable_a%22%2C%22song_detail_tab_A%22%2C%22member_limit_v3_A%22%2C%22member_limit_v1_C%22%2C%22trial_guide_existing_user_B%22%2C%22354_feed_D%22%2C%22feed_groupA%22%2C%22trial_guide_new_user_B%22%2C%22submeta_groupA%22%2C%22cdn_3_D%22%2C%22ad_exp_B%22%2C%22song_ab_value_B%22%2C%22login_groupC%22%2C%22422_luodiye_D%22%2C%22lg_tag_B%22%5D&lang=ja_CN&appid=com.maetimes.ios.Karaoke&__debug=1&app_on_mac=false&app_theme=Dark&appsflyer_id=1748594469263-9612673&carrier=--&carrier_mcc=65535&carrier_mnc=65535&device_model=iPhone&device_type=iPhone13%2C2&idfa=00000000-0000-0000-0000-000000000000&idfv=E9C6AB12-6737-4B9C-A811-BF0D6E5B04DA&is_active=1&nama_version=8.9.0&osn=iOS&osv=18.3.2&phonetype=iphone&screen_height=844.0&screen_scale=3.0&screen_width=390.0&theme_follow_system=false&xsi=2CF1AE62-1C21-468B-9B15-919D63E33869',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': 'tgw_l7_route=a484a508d5069fdd52bc57c0ce38b496; poke_session_id=MTc1MDIzNDM5NnxYTWV1ZU4wWmcxOU9rRFgzRjVVUDg3UVhDZldTVHFDSlpoOWhoQzdBMlV1MVJxbE1GdFVITHllOUhpSlNySWRlaG9wLTFKbVJYRXJHdkxNclliY0p4ZFNxR2hwekd5RXl8Gw-EQaUUb7BpXEALxQiCQbxv9l6kBccm0KUv4PelZCM=',
}

params = {
    'request_id': '1750235825282158',
    'series_id': '1001',
    'series_level_id': '10006',
    'nav_height': '44.0',
    'nav_y': '47.0',
    'theme_name': 'Dark',
    'v': '4.1.23',
    'unique_device_id': '7517199466077126935',
    'e_flags': '%5B%22new_lucky_turn_D%22%2C%22fake_lounge_A%22%2C%22member_song_group_D%22%2C%22server_groupC%22%2C%22servernew_groupB%22%2C%22consumable_a%22%2C%22song_detail_tab_A%22%2C%22member_limit_v3_A%22%2C%22member_limit_v1_C%22%2C%22trial_guide_existing_user_B%22%2C%22354_feed_D%22%2C%22feed_groupA%22%2C%22trial_guide_new_user_B%22%2C%22submeta_groupA%22%2C%22cdn_3_D%22%2C%22ad_exp_B%22%2C%22song_ab_value_B%22%2C%22login_groupC%22%2C%22422_luodiye_D%22%2C%22lg_tag_B%22%5D',
    'lang': 'ja_CN',
    'appid': 'com.maetimes.ios.Karaoke',
    '__debug': '1',
    'app_on_mac': 'false',
    'app_theme': 'Dark',
    'appsflyer_id': '1748594469263-9612673',
    'carrier': '--',
    'carrier_mcc': '65535',
    'carrier_mnc': '65535',
    'device_model': 'iPhone',
    'device_type': 'iPhone13%2C2',
    'idfa': '00000000-0000-0000-0000-000000000000',
    'idfv': 'E9C6AB12-6737-4B9C-A811-BF0D6E5B04DA',
    'is_active': '1',
    'nama_version': '8.9.0',
    'osn': 'iOS',
    'osv': '18.3.2',
    'phonetype': 'iphone',
    'screen_height': '844.0',
    'screen_scale': '3.0',
    'screen_width': '390.0',
    'theme_follow_system': 'false',
    'xsi': '2CF1AE62-1C21-468B-9B15-919D63E33869',
    'request_refer': 'h5',
}

json_data = {
    'lottery_id': 10006,
    'lottery_type': 2,
}


for i in range(5):
    response = requests.post(
        'https://test.api.pokekara.com/x/mall/lottery/start',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.json())
    time.sleep(3)