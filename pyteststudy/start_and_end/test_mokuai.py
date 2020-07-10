# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_mokuai.py
@Time:NAME.py@Time:2020/7/10 18:14
"""
# setup_module是:同一个模块中（文件中）所有用例开始前只执行一次，teardown_module是所有用例结束后只执行一次
import pytest


def setup_function():
    print('每个函数开始时都会执行')


def teardown_function():
    print(f'每个函数结束后都会执行')


def setup_module():
    print('本文件中，开始运行时执行一次')


def teardown_module():
    print('本文件中，所有用例执行完成后会执行一次')


def test_one():
    print(f'正在执行第一个测试用例')
    assert 5 in [1, 2, 4, 5, 6]


def test_two():
    print(f'正在执行第二个测试用例')
    assert 1 == 1


if __name__ == '__main__':
    pytest.main()
