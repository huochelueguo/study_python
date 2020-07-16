# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_skipif02.py
@Time:NAME.py@Time:2020/7/16 17:29
"""
# 当有多个skipif时，满足其中一个就跳过
import pytest
# 一个方法有多个skip的情况：


@pytest.mark.skipif(2 > 11, reason='当2大于1时，不执行该用例')
@pytest.mark.skipif(1 == 1, reason='结果为true，跳过该case')
def test_two():
    a = 5
    b = 15
    assert a == b   # 由于上方2个skip,其中一个为true，因此执行跳过，多个skip为or的关系


# 当上级满足跳过时，下级中的skip忽略，同样skip
@pytest.mark.skipif(1 == 1, reason='结果为true，跳过该case')
class Test_three(object):

    @pytest.mark.skipif(2 > 11, reason='当2大于1时，不执行该用例')
    def test_four(self):
        assert 5 == 5   # 由于类满足了跳过，既是方法中不满足跳过，也执行跳过


if __name__ == '__main__':
    pytest.main()
