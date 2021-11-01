# -*- coding: utf-8 -*-
# @Time : 2021/10/29 17:15
# @Author : Limusen
# @File : demo_函数对象


# 　可以把函数当做变量取用
# func=内存地址
def func():
    print("from func")


# # 1. 可以复制
# f = func
# print(f,func)
# f()

# # 2.可以当作函数的参数传入
# def foo(x):
#     print(x)
#
# foo(func)  # foo（func的内存地址）

# # 3. 可以当作另外一个函数的返回值
# def foo(x): # x = func的内存地址
#     return x # return func的内存地址
#
#
# res = foo(func)  # foo(func的内存地址)
# print(res) # res= func的内存地址
#
# res()

# # 4.可以当作容器类型的一个元素
# l = [func,]
# print(l)
# l[0]()

# dic = {'k1': func}
# print(dic)
# dic['k1']()

def login():
    print("login功能")


def transfer():
    print("转账功能")


def check_banlance():
    print("查询余额")


while True:
    print("""
    0 退出
    1 登录
    2 转账
    3 查询余额    
    """)
    choice = input("请输入命令编号： ").strip()
