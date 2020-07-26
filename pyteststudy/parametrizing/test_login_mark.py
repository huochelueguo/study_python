# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_login_mark.py
@Time:NAME.py@Time:2020/7/26 下午11:27
"""
# 可以再pytest.ini文件中设置marker，在测试case中填写不同的marker，可以根据指定marker执行用例
import pytest

data = [
    {1, 2, 3},
    {2, 4, 6},
    {3, 5, 8}
]
list_ids = []
for a, b, c in data:
    str = 'a:{} b:{} c{}'.format(a, b, c)
    list_ids.append(str)
print(list_ids)


@pytest.mark.parametrize('a, b, c', data, ids=list_ids)
class Test_login(object):

    @pytest.mark.smoke
    def test_one(self, a, b, c):
        assert a + b == c

    @pytest.mark.smoke
    def test_two(self, a, b, c):  # 就算是没有调用部分参数也要传入，不使用即可；
        assert a > b

    def test_three(self, a, b, c):  # 由于没有marker，因此如果pytest.ini配置了其他mark，这个用例就不会执行
        assert a + b < c


if __name__ == '__main__':
    pytest.main()
