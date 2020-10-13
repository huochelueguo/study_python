# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_fixture.py
@Time:NAME.py@Time:2020/10/13 15:34
"""
# 参数化方式：使用pytest.fixture

import pytest


@pytest.fixture(params=[1, 2, 3])
def fixture_param(request):
    return request.param


def test_one(fixture_param):
    print(fixture_param)
    assert 1 == fixture_param