# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_fix_function.py
@Time:NAME.py@Time:2020/7/10 20:39
"""
# fixture的参数为空时，默认作用域为function
# fixture是有返回值得，没有返回值默认为None。
# 用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。
# https://www.cnblogs.com/huizaia/p/10331469.html
import pytest


@pytest.fixture()
def login():
    print('这是登录操作')
    a = 2
    return a


def test_needlogin(login):  # 要将fixture函数值传入
    print('需要登录的接口，先要执行登录操作')
    assert login == 2   # 直接将fixture的函数名当作返回值


def test_nologin():
    print('不需要登录，直接进行测试')
    assert 2 == 2


if '__name__' == '__main__':
    pytest.main()


