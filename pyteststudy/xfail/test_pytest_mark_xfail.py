# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_pytest_mark_xfail.py
@Time:NAME.py@Time:2020/7/16 19:58
"""
import pytest


def test_one():
    assert 1 == 2   # 无任何装饰器，因此报错


@pytest.mark.xfail
def test_two():
    assert 1 == 2   # 虽然结果为fail，但是因为有了xfail标记，因此没按照错误上报，输出为xfail


@pytest.mark.xfail
def test_three():
    assert 2 == 2   # 由于结果为pass，但是有xfail标记，因此输出为xpass


if __name__ == '__main__':
    pytest.main(['-v'])