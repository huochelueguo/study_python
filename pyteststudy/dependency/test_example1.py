# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_example1.py
@Time:2022/5/16 下午3:07
"""
import pytest


class Test_A:

    @pytest.mark.dependency()
    def test_a(self):
        assert 1 == 2

    @pytest.mark.dependency()
    def test_b(self):
        assert 2 == 2

    @pytest.mark.dependency(depends=["Test_A::test_a", 'test_b'])  # 多个depends时，按照列表放入
    def test_c(self):  # 因为test_a执行结果为fail，因此test_c将会跳过，不执行
        assert 3 == 3

    @pytest.mark.dependency(depends=['Test_A::test_b'])
    def test_d(self):
        pass


class Test_B:
    # @pytest.mark.dependency()
    # def test_a(self):
    #     print('this is test_a')

    @pytest.mark.dependency(depends=['test_example2.py::Test_C::test_c'], scope='package')
    # 因为有参数scope，因此将只在本类中找依赖，不会去别的类中寻找
    def test_b(self):
        print('this is test_b')


class TestPackage:
    # 依赖的dependency为同目录下其他文件时，depends格式需要为文件名::类名（如果有）::方法名；scope为package
    # 运行结果：Skipped: test_a depends on test_example2.py::Test_C::test_c
    @pytest.mark.dependency(depends=['test_example2.py::Test_C::test_c'], scope='package')
    def test_a(self):
        print('this is test_a')

    def test_b(self):
        print('this is test_a')
        assert 1 == 2



if __name__ == '__main__':
    pytest.main('dependency')
