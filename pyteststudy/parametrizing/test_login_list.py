# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_login_list.py
@Time:NAME.py@Time:2020/7/15 上午9:04
"""
import pytest
import allure
import requests

data = [
    {'url1': 'http://test.api.pokekara.com/api/user/login',
     'body': {'platform': 4,
              'token': 'login',
              'id_token': '+8618500616906',
              'secret': '234567'}},
    {'url1': 'http://test.api.pokekara.com/api/user/login',
     'body': {'platform': 4,
              'token': 'login',
              'id_token': '+8618500616906',
              'secret': '111112'}}
]


@pytest.mark.parametrize('datas', data)     # 用一个参数接受数据，就是传入一个元组，元组里的数据运用索引的方法就可以提取出来；
def test_login(datas):
    print(datas)
    r = requests.post(url=datas['url1'], data=datas['body'])
    print(r.json())
    test = r.text
    assert 'success' in test


if __name__ == '__main__':
    pytest.main()
