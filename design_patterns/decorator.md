### 装饰模式

![](https://upload-images.jianshu.io/upload_images/14073259-43a525be5365f230.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
装饰模式
"""


class Person:

    def __init__(self, myname):
        self.name = myname

    def show(self):
        print("我是: {}".format(self.name))


class Finery(Person):

    def __init__(self):
        super().__init__("")
        self.component = None

    def decorate(self, component: Person):
        self.component = component

    def show(self):
        pass


class Tshirts(Finery):

    def __init__(self):
        super().__init__()

    def show(self):
        print("T恤")
        if self.component:
            self.component.show()


class BigTrouser(Finery):

    def __init__(self):
        super().__init__()

    def show(self):
        print("裤子")
        if self.component:
            self.component.show()


if __name__ == "__main__":

    p = Person(myname="john")
    tt = Tshirts()
    bt = BigTrouser()
    tt.decorate(p)
    bt.decorate(tt)
    bt.show()

```

