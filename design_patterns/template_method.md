### 模板方法模式



![](https://upload-images.jianshu.io/upload_images/14073259-c6cf2e708ad076f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模板方法模式
"""

from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):

    @abstractmethod
    def primitive_operation_1(self):
        pass

    @abstractmethod
    def primitive_operation_2(self):
        pass

    def template_method(self):

        self.primitive_operation_1()
        self.primitive_operation_2()
        print("执行模板方法")


class ConcreteClassA(AbstractClass):

    def primitive_operation_1(self):
        print("A类方法1实现")

    def primitive_operation_2(self):
        print("A类方法2实现")


class ConcreteClassB(AbstractClass):
    def primitive_operation_1(self):
        print("B类方法1实现")

    def primitive_operation_2(self):
        print("B类方法2实现")

```

