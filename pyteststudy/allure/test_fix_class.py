# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_fix_class.py
@Time:NAME.py@Time:2020/7/11 11:45
"""
import pytest
import allure


@pytest.fixture(scope='class')
def fix_class():
    print('fixture_class只在类测试用例执行前执行一次')
    a = 5
    b = 5
    return a, b


@allure.feature('登录模块测试')
class Test_Fixture_Class(object):

    @allure.story('测试用例1')
    def test_one(self, fix_class):
        # 调用fixture，使用fix_class中的值
        assert fix_class[0] == fix_class[1]

    @allure.story('测试用例2')
    def test_two(self):
        # 不调用fixture，也可以正常执行
        assert 5 in [1, 2, 3]
