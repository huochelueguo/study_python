# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_skipif03.py
@Time:NAME.py@Time:2020/7/16 17:37
"""
# 当多个case的跳过方式都是一个时，可以先把skip赋值给变量，多处调用即可
import pytest

allskip = pytest.mark.skipif(2 > 1, reason='赋值给变量后统一使用的skip')


@allskip
def test_one():
    assert 5 == 5


@allskip
def test_two():
    assert 5 == 5


def test_three():
    assert 5 == 5


if __name__ == '__main__':
    pytest.main()
