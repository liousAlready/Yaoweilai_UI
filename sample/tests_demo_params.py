# -*- coding: utf-8 -*-
# @Time : 2021/10/20 17:38
# @Author : Limusen
# @File : demo_params


import pytest


class TestDemo:

    def setup_class(self):
        print("开始测试...")

    def teardown_class(self):
        print("结束测试...")

    def add(self, a, b):
        return a + b

    # def adds(self, a, b, c=None):
    #     print('\n a:{} , b:{} , c:{}'.format(a, b, c))
    #     assert self.adds(a, b) == c
    #
    # @pytest.mark.parametrize("a", (1, 2, 3, 4, 5))
    # def test_adda(self, a):
    #     print("\n a :", a, end=" ")
    #     assert self.test_adda(a, 1) == a + 1

    @pytest.mark.parametrize('a,b,c', [(1, 2, 3), (4, 5, 9), ('1', '2', '12')])
    def test_addb(self, a, b, c):
        print('\n a:{} , b:{} , c:{}'.format(a, b, c))
        assert self.add(a, b) == c

    # ids 的作用
    data = [(1, 2, 3), (4, 5, 9), ('1', '2', '12')]
    ids = [f'data{d}' for d in range(len(data))]  # => 生成与数据数量相同的名称列表

    @pytest.mark.parametrize('a, b, c', data, ids=ids)
    def test_add(self, a, b, c):
        print(f'\na,b,c的值:{a},{b},{c}')
        assert self.add(a, b) == c

    # @pytest.mark.parametrize("arg_1", [4399, 2012, 1997])
    # @pytest.mark.parametrize("arg_2", ['AAAA', 'BBBB', 'CCCC'])
    # def test_add_by_func_aaa(self, arg_1, arg_2):
    #     print("arg_1:{}  arg_2:{}".format(arg_1, arg_2))
    #     assert True


class Test_Demo():
    @pytest.mark.parametrize("a, b, result", [(1, 1, 2), (2, 8, 10)])
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result


data = [(1, 1, 2),
         (2, 8, 10),
         (99, 1, 100)
         ]

class Test_Demo1():
    @pytest.mark.parametrize("a, b, result", data)
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result

if __name__ == '__main__':
    pytest.main(['-s', '-v'])
