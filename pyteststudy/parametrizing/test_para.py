# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_para.py
@Time:NAME.py@Time:2020/7/11 20:26
"""
import pytest

data = [
    {1, 2, 3},
    {4, 5, 9},
    {2, 5, 8}]


@pytest.mark.parametrize('a, b, add', data)     # 使用和参数数量一致得变量来接收，位置参数与实际测试数据一一对应即可
def test_one(a, b, add):
    print(f':{a}+{b}={a+b}')
    actual = a + b
    assert actual == add


if __name__ == '__main__':
    pytest.main()
