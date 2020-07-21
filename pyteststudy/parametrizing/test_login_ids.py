# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_login_ids.py
@Time:NAME.py@Time:2020/7/16 上午9:36
"""
import pytest

data = [
    {1, 2, 3},
    {4, 5, 9},
    {2, 5, 8}
]
list_ids = []
for (aa, bb, cc) in data:
    str1 = 'a:{} + b:{} = c:{}'.format(aa, bb, cc)
    list_ids.append(str1)
print(list_ids)


@pytest.mark.parametrize('a, b, c', data, ids=list_ids)
def test_one(a, b, c):
    sum1 = a + b
    assert sum1 == c


if __name__ == '__main__':
    pytest.main(['-v'])
