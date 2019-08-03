### 中介者模式

![](https://upload-images.jianshu.io/upload_images/14073259-40bdc7addbfc1b3a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
中介者模式
"""


class Colleague:

    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        pass


class Mediator:

    def send(self, message, colleague: Colleague):
        pass


class Colleague1(Colleague):

    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def notify(self, message):
        print(f"colleague1 get message: {message}")


class Colleague2(Colleague):

    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def notify(self, message):
        print(f"colleague2 get message: {message}")


class ConcrateMediator(Mediator):

    def __init__(self):
        self.c1 = None
        self.c2 = None

    def send(self, message, colleague: Colleague):
        if colleague == self.c1:
            self.c2.notify(message)
        elif colleague == self.c2:
            self.c1.notify(message)


if __name__ == "__main__":

    mediator = ConcrateMediator()
    c1 = Colleague1(mediator)
    c2 = Colleague2(mediator)

    mediator.c1 = c1
    mediator.c2 = c2

    c1.send("hello c2")
    c2.send("hi c1")


```

