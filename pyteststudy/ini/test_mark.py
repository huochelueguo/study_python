# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_mark.py
@Time:NAME.py@Time:2020/7/20 下午11:48
"""
import pytest


def test_one():
    assert 1 == 1


@pytest.mark.smoke
def test_two():
    assert 2 == 2


def test_three():
    assert 3 == 3


def test_four():
    assert 4 > 4


if __name__ == '__main__':
    pytest.main(['-m', "smoke"])
