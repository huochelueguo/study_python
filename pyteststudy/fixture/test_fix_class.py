# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_fix_class.py
@Time:NAME.py@Time:2020/7/11 11:45
"""
# fixture作用域为类，在测试类执行前执行一次，类似于setup_class/teardown_class
# 类中方法需要调用fixture时，self后补充fixture函数名称
import pytest


@pytest.fixture(scope='class')
def fix_class():
    print('fixture_class只在类测试用例执行前执行一次')
    a = 5
    b = 5
    return a, b


class Test_Fixture_Class(object):

    def test_one(self, fix_class):
        # 调用fixture，使用fix_class中的值
        assert fix_class[0] == fix_class[1]

    def test_two(self):
        # 不调用fixture，也可以正常执行
        assert 5 in [1, 2, 3]