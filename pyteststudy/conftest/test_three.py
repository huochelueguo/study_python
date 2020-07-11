# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_three.py
@Time:NAME.py@Time:2020/7/11 16:15
"""
import pytest


def test_three(login_data3):
    print('执行..')
    assert login_data3 == 5


if __name__ == '__main__':
    pytest.main()

