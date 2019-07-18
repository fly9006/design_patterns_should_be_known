### 代理模式

![](https://upload-images.jianshu.io/upload_images/14073259-a057ae019a6eef65.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
代理模式
"""


class SchoolGirl:

    def __init__(self, name):
        self.name = name


class GiveGift:

    def __init__(self, mm: SchoolGirl):
        self.mm = mm

    def give_dolls(self):
        pass

    def give_flowers(self):
        pass

    def give_chocolate(self):
        pass


class RichMan(GiveGift):

    def __init__(self, mm):
        super().__init__(mm)
        self.name = "rich man"

    def give_dolls(self):
        print(self.name, "送洋娃娃给", self.mm.name)

    def give_flowers(self):
        print(self.name, "送花给", self.mm.name)

    def give_chocolate(self):
        print(self.name, "送巧克力给", self.mm.name)


class Proxy(GiveGift):

    def __init__(self, mm: SchoolGirl):
        super().__init__(mm)
        self.gg = RichMan(mm)

    def give_dolls(self):
        self.gg.give_dolls()

    def give_flowers(self):
        self.gg.give_flowers()

    def give_chocolate(self):
        self.gg.give_chocolate()


if __name__ == "__main__":

    beauty = SchoolGirl("beautiful girl")
    proxy = Proxy(beauty)
    proxy.give_dolls()
    proxy.give_flowers()
    proxy.give_chocolate()


```

