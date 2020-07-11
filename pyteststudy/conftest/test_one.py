# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_one.py
@Time:NAME.py@Time:2020/7/11 15:44
"""
import pytest


def test_login(login_data):
    print('开始执行测试用例')
    assert login_data == 2


if __name__ == '__main__':
    pytest.main()

