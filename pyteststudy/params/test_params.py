# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_params.py
@Time:NAME.py@Time:2020/7/11 15:02
"""
# 在fixture中传入params，执行test时就回按照params的个数执行多次
import pytest


@pytest.fixture(params=['数据组1', '数据组2'])   # params中的参数，测试用例都会执行一遍
def fix_params(request):    # 固定使用request，使用时为request.param
    print(f'这是一个有多个前置参数的fixture{request.param}')
    yield 1
    print('yeild之后得内容，测试用例执行完成后会执行')


def test_one(fix_params):
    print('执行测试用例')
    assert fix_params == 1


if __name__ == '__main__':
    pytest.main()