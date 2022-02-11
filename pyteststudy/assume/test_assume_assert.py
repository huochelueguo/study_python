#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/11 0011 10:24
# @Author  : sunze
# @File    : test_assume_assert.py


import pytest


def test_assert():
    print('开始执行普通assert')
    assert 1 + 4 == 5
    assert 1 + 3 == 3
    assert 2 + 5 == 7
    print('done')


def test_login():
    print('开始执行pytest.assume')
    pytest.assume(1 + 4 == 5)
    pytest.assume(1 + 3 == 3)
    pytest.assume(2 + 5 == 7)
    pytest.assume(2 + 5 == 9)
    print("测试完成")


if __name__ == '__main__':
    pytest.main()
