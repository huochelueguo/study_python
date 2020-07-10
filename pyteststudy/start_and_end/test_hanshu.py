# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_hanshu.py
@Time:NAME.py@Time:2020/7/10 18:03
"""

# 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
# 单独写在函数外部
import pytest


def setup_function():
    print('每个函数开始时都会执行')


def teardown_function():
    print(f'每个函数结束后都会执行')


def test_one():
    print(f'正在执行第一个测试用例')
    assert 5 in [1, 2, 4, 5, 6]


def test_two():
    print(f'正在执行第二个测试用例')
    assert 1 == 16


if __name__ == '__main__':
    pytest.main()
