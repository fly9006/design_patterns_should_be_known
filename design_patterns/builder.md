### 建造者模式



![](https://upload-images.jianshu.io/upload_images/14073259-0784d46b83f57b34.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
建造者模式
"""


class Product:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):

        for p in self.parts:
            print(p)


class Builder:

    def builder_part_a(self):
        pass

    def builder_part_b(self):
        pass

    def get_result(self):
        pass


class ConcreteBuilder1(Builder):

    def __init__(self):
        self.product = Product()

    def builder_part_a(self):
        self.product.add("part A")

    def builder_part_b(self):
        self.product.add("part B")

    def get_result(self):
        return self.product


class ConcreteBuilder2(Builder):

    def __init__(self):
        self.product = Product()

    def builder_part_a(self):
        self.product.add("part X")

    def builder_part_b(self):
        self.product.add("part Y")

    def get_result(self):
        return self.product


class Director:

    def construct(self, builder: Builder):
        builder.builder_part_a()
        builder.builder_part_b()


if __name__ == "__main__":

    director = Director()
    b1 = ConcreteBuilder1()
    b2 = ConcreteBuilder2()

    director.construct(b1)
    p1 = b1.get_result()
    p1.show()

    director.construct(b2)
    p2 = b2.get_result()
    p2.show()

```

