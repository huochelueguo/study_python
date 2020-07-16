# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_skipif01.py
@Time:NAME.py@Time:2020/7/16 17:22
"""
# 使用pytest.mark.skipif可以设置，当满足某个条件时跳过
import pytest


def test_one():
    a = 5
    b = 15
    assert a == b


@pytest.mark.skipif(2 > 11, reason='当2大于1时，不执行该用例')
def test_two():     # 2>11为false，因此不满足，所以执行该测试case
    a = 5
    b = 15
    assert a == b


if __name__ == '__main__':
    pytest.main()
