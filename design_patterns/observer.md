### 观察者模式



![](https://upload-images.jianshu.io/upload_images/14073259-5e01ad4190249874.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
观察者模式
"""


class Observer:

    def update(self):
        pass


class Subject:

    def __init__(self):
        self.state = ""
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        pass

    def notify(self):
        for o in self.observers:
            o.update()


class ConcreteObserver(Observer):

    def __init__(self, name, subject: Subject):
        self.name = name
        self.subject = subject

    def update(self):
        print(f"观察者{self.name}的新状态是{self.subject.state}")


class ConcreteSubject(Subject):

    def __init__(self, state):
        super().__init__()
        self.state = state


if __name__ == "__main__":

    s = ConcreteSubject(state="X")
    s.attach(ConcreteObserver(name="A", subject=s))
    s.attach(ConcreteObserver(name="B", subject=s))
    s.attach(ConcreteObserver(name="C", subject=s))
    s.notify()

```



