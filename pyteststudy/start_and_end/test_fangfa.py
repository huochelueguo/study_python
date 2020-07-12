# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_fangfa.py
@Time:NAME.py@Time:2020/7/10 18:43
"""
# 类中方法执行使用setup teardown
import pytest


class Test_lei(object):

    # def __init__(self):
    #     print('非执行pytest时，才会输出本句话')

    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 5 in [1, 3, 5]

    def setup_class(self):
        print('类开始时执行该语句')

    def teardown_class(self):
        print('类中用例结束时执行该语句')

    def setup(self):
        print('类中的每个方法执行前，会执行本句话')

    def teardown(self):
        print('类中每个方法结束后，会执行本句话')


if __name__ == '__main__':
    # g = Test_lei()
    # print(g)
    pytest.main()
