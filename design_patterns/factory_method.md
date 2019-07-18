### 工厂方法模式



![](https://upload-images.jianshu.io/upload_images/14073259-a2b46d85dd9f5102.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
工厂方法模式
"""


class LeiFeng:

    def sweep(self):
        print("扫地")

    def wash(self):
        print("洗衣")

    def buyrice(self):
        print("买米")


class Undergraduate(LeiFeng):
    pass


class Volunteer(LeiFeng):
    pass


class LeiFengFactory:

    def create_lei_feng(self):
        pass


class UndergraduateFactory(LeiFengFactory):

    def create_lei_feng(self):
        return Undergraduate()


class VolunteerFactory(LeiFengFactory):

    def create_lei_feng(self):
        return Volunteer()


if __name__ == "__main__":

    undergraduate_factory = UndergraduateFactory()
    student = undergraduate_factory.create_lei_feng()
    student.sweep()
    student.wash()
    student.buyrice()

```



