# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_lei.py
@Time:NAME.py@Time:2020/7/10 18:32
"""
import pytest


class Test_lei(object):

    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 5 in [1, 3, 5]

    def setup_class(self):
        print('类开始时执行该语句')

    def teardown_class( self ):
        print('类中用例结束时执行该语句')


if __name__ == '__main__':
    # g = Test_lei()
    pytest.main()
