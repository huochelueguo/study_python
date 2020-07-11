# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_two.py
@Time:NAME.py@Time:2020/7/11 15:45
"""
import pytest


class Test_login(object):

    def test_one(self, login_data2):
        print ('开始执行测试用例')
        assert login_data2[0] == 5


if __name__ == '__main__':
    pytest.main()