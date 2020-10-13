# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_parameterizing.py
@Time:NAME.py@Time:2020/10/13 17:57
"""
# 参数化方式：使用pytest.mark.parameterzing
import pytest

data = [{1, 2, 3},
        {4, 5, 9},
        {2, 4, 5}]


@pytest.mark.parametrize(argnames='a, b, c', argvalues=data)
def test_one(a, b, c):
    assert a * b == c


