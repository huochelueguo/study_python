# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_pytest_xfail.py
@Time:NAME.py@Time:2020/7/16 19:46
"""
import pytest


def test_one():
    a = 5
    if a > 10:
        print('true')
        return True
    else:
        print('false')
        return False


def test_two():
    print('在xfail之前内容，不受影响正常执行')
    if test_one():
        assert 5 == 5
    else:   # 由于test_one返回的为false，因此执行xfail,本测试用例不执行，标记为xfail
        pytest.xfail(reason='标记为错误，后续不再执行')
        assert 5 == 5


def test_three():
    assert 5 == 5


if __name__ == '__main__':
    pytest.main(['-v'])
