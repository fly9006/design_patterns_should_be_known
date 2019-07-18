### 备忘录模式



![](https://upload-images.jianshu.io/upload_images/14073259-02685a3383fa0854.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
备忘录模式
"""


class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def set_memnto(self, memento: Memento):
        self.state = memento.state

    def show(self):
        print(self.state)


class CareTaker:
    def __init__(self):
        self.memento = None

    def set_memento(self, memento: Memento):
        self.memento = memento


if __name__ == "__main__":

    o = Originator(state="on")
    o.show()
    c = CareTaker()
    c.set_memento(o.create_memento())

    o.state = "off"
    o.show()

    o.set_memnto(c.memento)
    o.show()

```

