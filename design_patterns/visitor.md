### 访问者模式



![](https://upload-images.jianshu.io/upload_images/14073259-8d7b8528f2c42e2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
访问者模式
"""


class Visitor:

    def visit_concrate_element_a(self, concrate_element_a):
        pass

    def visit_concrate_element_b(self, concrate_element_b):
        pass


class ConcrateVisitor1(Visitor):

    def visit_concrate_element_a(self, concrate_element_a):
        print(f"{self.__str__()} visit {concrate_element_a.__str__()}")

    def visit_concrate_element_b(self, concrate_element_b):
        print(f"{self.__str__()} visit {concrate_element_b.__str__()}")


class ConcrateVisitor2(Visitor):

    def visit_concrate_element_a(self, concrate_element_a):
        print(f"{self.__str__()} visit {concrate_element_a.__str__()}")

    def visit_concrate_element_b(self, concrate_element_b):
        print(f"{self.__str__()} visit {concrate_element_b.__str__()}")


class Element:

    def accept(self, visitor: Visitor):
        pass


class ConcrateElemntA(Element):

    def accept(self, visitor: Visitor):
        visitor.visit_concrate_element_a(self)


class ConcrateElemntB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrate_element_b(self)


class ObjectStructure:

    def __init__(self):
        self.elements = []

    def add_element(self, element: Element):
        self.elements.append(element)

    def remove_element(self, element: Element):
        self.elements.remove(element)

    def accept(self, visitor: Visitor):

        for e in self.elements:
            e.accept(visitor)


if __name__ == "__main__":

    o = ObjectStructure()
    o.add_element(ConcrateElemntA())
    o.add_element(ConcrateElemntB())

    v1 = ConcrateVisitor1()
    v2 = ConcrateVisitor2()

    o.accept(v1)
    o.accept(v2)

```



