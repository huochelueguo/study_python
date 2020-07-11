# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_fix_aotouse.py
@Time:NAME.py@Time:2020/7/11 12:14
"""
import pytest


@pytest.fixture(autouse='True')
def fix_aotouse():
    print('aoto为true')
    a = 5
    b = 5
    return a, b


def test_one(fix_aotouse):
    c = fix_aotouse[0]
    d = fix_aotouse[1]
    assert d == c
    print('虽然autouse为true，但是如果要使用fixture的返回值，函数还是要写fixture名称')


def test_two():
    assert 3 in [1, 2, 4, 6]


if __name__ == '__main__':
    pytest.main()
