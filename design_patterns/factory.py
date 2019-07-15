#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单工厂模式
"""


class Operator:
    """
    基类
    """
    def __init__(self):
        self.pa = 0
        self.pb = 0

    def get_result(self):
        pass


class AddOperator(Operator):
    """
    子类：实现两个数值相加
    """
    def __init__(self):
        super().__init__()

    def get_result(self):
        return self.pa + self.pb


class SubOperator(Operator):
    """
    子类：实现两个数值相减
    """
    def __init__(self):
        super().__init__()

    def get_result(self):
        return self.pa - self.pb


class MulOperator(Operator):
    """
    子类：实现两个数值相乘
    """
    def __init__(self):
        super().__init__()

    def get_result(self):
        return self.pa * self.pb


class DivOperator(Operator):
    """
    子类：实现两个数值相除
    """
    def __init__(self):
        super().__init__()

    def get_result(self):
        return self.pa / self.pb


class UndefinedOperator(Operator):
    """
    子类：未定义的运算方法
    """
    def __init__(self):
        super().__init__()

    def get_result(self):
        print("wrong operator character, try again~")
        return 0


class Factory:
    """
    工厂类
    """
    def __init__(self):
        self.operators = {"+": AddOperator(), "-": SubOperator(), "*": MulOperator(), "/": DivOperator()}

    def get_operator(self, ch):
        """
        给定条件的入参，返回匹配到的方法实例
        :param ch:
        :return:
        """
        return self.operators.get(ch, UndefinedOperator())


if __name__ == "__main__":

    pa = input("pa:  ")
    pb = input("pb:  ")
    ch = input("ch:  ")
    factory = Factory()
    operator = factory.get_operator(ch)
    operator.pa = float(pa)
    operator.pb = float(pb)
    print("result: ", operator.get_result())
