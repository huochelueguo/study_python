# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_login.py
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
              'secret': '111111'}}
]


@pytest.mark.parametrize('datas', data)
def test_login(datas):
    print(datas)
    r = requests.post(url=datas['url1'], data=datas['body'])
    print(r.json())
    code = r.status_code
    assert code == 200


# @pytest.mark.parametrize('a', data)
# def test_login2(a):
#     r = requests.post(url=a['url'], data=a[1])
#     print(r.json())
#     code = r.status_code
#     assert code == 200


if __name__ == '__main__':
    pytest.main()
