### 单例模式



![](https://upload-images.jianshu.io/upload_images/14073259-42b52188532f61fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
单例模式
"""


# use __new__ method
class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class TestClass(Singleton):
    a = 1


# use decorator
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton


@singleton
class Test2Class:
    a = 1


if __name__ == "__main__":

    t1 = TestClass()
    t2 = TestClass()
    t2.a = 2
    print(t1.a)
    print(t2.a)
    print(id(t1))
    print(id(t2))
    t3 = Test2Class()
    t4 = Test2Class()
    t3.a = 3
    print(t3.a)
    print(t4.a)
    print(id(t3))
    print(id(t4))

```

