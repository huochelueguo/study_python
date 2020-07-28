# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_ordering.py
@Time:NAME.py@Time:2020/7/28 上午9:07
"""
# 使用pytest.mark.run(order=x)可以控制用例的执行顺序，但是要注意用例互相的依赖情况
# 执行顺序规则：
# --如果全部为正数：数字越小越先执行
# --如果全部为负数：数字越小越先执行
# --同时存在正负数：先执行正数部分，再执行负数部分
# --存在没有标记的用例：最后再执行，先执行带有order的case
import pytest


class Test_one(object):

    @pytest.mark.run(order=-2)
    def test_one(self):
        assert 1 == 1

    @pytest.mark.run(order=-20)
    def test_two(self):
        assert 2 > 3

    @pytest.mark.run(order=-12)
    def test_three(self):
        assert 5 > 2


if __name__ == '__main__':
    pytest.main()
