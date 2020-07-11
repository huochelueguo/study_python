# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_lot_fixture.py
@Time:NAME.py@Time:2020/7/10 21:00
"""
# 一个fixture可以返回多个值，一个测试函数也可以承接过个fixture
# 一个fixture返回多个值，可以使用字典来承接
import pytest


@pytest.fixture()
def login():
    print('this is fixture')
    a = 5 + 5
    b = 5 * 5
    return a, b


def test_needlogin(login):

    # 使用fixture的返回值是使用其函数名，因此可以直接函数名[字典索引]
    t1 = login[0]
    print(f't1 = {t1}')
    t2 = login[1]
    print(f't2 = {t2}')
    assert t1 == t2


if '__name__' == '__main__':
    pytest.main()


# 一个测试函数也可以承接过个fixture
import pytest


@pytest.fixture()
def login2():
    print('this is fixture222')
    a = 5 + 5
    return a


@pytest.fixture()
def login3():
    print('this is fixture333')
    b = 5 + 5
    return b


def test_needlogin2(login2, login3):    # 根据括号中fixture函数得顺序，依次调用

    # 使用fixture的返回值是使用其函数名，因此可以直接函数名[字典索引]
    assert login2 == login3


if '__name__' == '__main__':
    pytest.main('[ test_lot_fixture::test_needlogin2]')
