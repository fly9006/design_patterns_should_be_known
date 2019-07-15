### 策略模式

策略模式是一种定义一系列算法的方法，从概念上来看，所有这些算法完成的都是相同的工作，只是实现不同，它可以以相同的方式调用所有的算法，减少了各种算法类与使用算法类之间的耦合。



![](https://upload-images.jianshu.io/upload_images/14073259-7a57e5f773d6a95c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
策略模式
"""

import math


class CashSuper:
    """
    基类
    """
    def accept_cash(self, money):
        return 0.0

    @staticmethod
    def to_float(param):
        if isinstance(param, float):
            return param
        try:
            return float(param)
        except BaseException as e:
            raise e


class CashNormal(CashSuper):
    """
    正常收费子类
    """
    def accept_cash(self, money: float):
        return money


class CashRebate(CashSuper):
    """
    促销打折子类
    """
    def __init__(self, rebate):
        self.rebate = self.to_float(rebate)

    def accept_cash(self, money: float):
        return money * self.rebate


class CashReturn(CashSuper):
    """
    满减子类
    """
    def __init__(self, money_condition, money_return):
        self.money_condition = self.to_float(money_condition)
        self.money_return = self.to_float(money_return)

    def accept_cash(self, money: float):
        if money > self.money_condition:
            return money - (math.floor(money / self.money_condition) * self.money_return)


class CashContextError(BaseException):
    pass


class CashContext:
    """
    上下文
    """
    def __init__(self, cash_type):
        self.cash_type = cash_type
        self.cs = self.__get_cash_strategy()

    def __get_cash_strategy(self):
        cs = None
        if self.cash_type == "正常收费":
            cs = CashNormal()
        elif self.cash_type == "满300减100":
            cs = CashReturn(money_condition="300", money_return="100")
        elif self.cash_type == "8折":
            cs = CashRebate(rebate="0.8")
        return cs

    def get_result(self, money):
        if not isinstance(self.cs, CashSuper):
            raise CashContextError("error: unvalid cash type")
        return self.cs.accept_cash(self.cs.to_float(money))


if __name__ == "__main__":
    cash_type = "8折"
    price = 100
    num = 3
    cc = CashContext(cash_type=cash_type)
    result = cc.get_result(price * num)
    print(result)

```

