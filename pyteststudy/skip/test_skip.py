# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_skip.py
@Time:NAME.py@Time:2020/7/16 17:14
"""
# 使用pytest.mark.skip可以跳过指定的测试用例
import pytest


def test_one():
    a = 5
    b = 15
    assert a == b


@pytest.mark.skip(reason='测试跳过不执行')
def test_two():
    a = 5
    b = 15
    assert a == b


if __name__ == '__main__':
    pytest.main()
