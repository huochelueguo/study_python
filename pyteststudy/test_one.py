# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_one.py
@Time:NAME.py@Time:2020/7/10 16:46
"""
import pytest


class TestClass:
    def test_one(self):
        x = "this"
        print(x)
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    print('普通模式下才输出')
    a = TestClass()
    a.test_one()
    pytest.main()
