### 外观模式



![](https://upload-images.jianshu.io/upload_images/14073259-5f0aad0ee1ac752b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
外观模式
"""


class System:
    pass


class SubSystemOne(System):

    def method_one(self):
        print("1子系统方法一")


class SubSystemTwo(System):

    def method_two(self):
        print("2子系统方法二")


class SubSystemThree(System):

    def method_three(self):
        print("3子系统方法三")


class SubSystemFour(System):

    def method_four(self):
        print("4子系统方法四")


class Facade:

    def __init__(self):
        self.sys_one = SubSystemOne()
        self.sys_two = SubSystemTwo()
        self.sys_three = SubSystemThree()
        self.sys_four = SubSystemFour()

    def method_group_a(self):
        print("A方法组:")
        self.sys_one.method_one()
        self.sys_two.method_two()
        self.sys_four.method_four()

    def method_group_b(self):
        print("B方法组:")
        self.sys_two.method_two()
        self.sys_three.method_three()

if __name__ == "__main__":

    facade = Facade()
    facade.method_group_a()
    facade.method_group_b()

```

