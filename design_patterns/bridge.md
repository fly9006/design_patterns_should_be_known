### 桥接模式



![](https://upload-images.jianshu.io/upload_images/14073259-a111d334c409c825.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
桥接模式
"""


class MobileSoftware:

    def run(self):
        pass


class MobileGame(MobileSoftware):

    def run(self):
        print("run game")


class MobileAddresslist(MobileSoftware):

    def run(self):
        print("run address list")


class MobileBrand:

    def __init__(self):
        self._software = None

    def install_software(self, software: MobileSoftware):
        self._software = software

    def run(self):
        pass


class MobileBrandM(MobileBrand):

    def __init__(self):
        super().__init__()

    def run(self):
        if self._software:
            self._software.run()


class MobileBrandN(MobileBrand):

    def __init__(self):
        super().__init__()

    def run(self):
        if self._software:
            self._software.run()


if __name__ == "__main__":

    brand = MobileBrandM()
    brand.install_software(MobileGame())
    brand.run()
    brand.install_software(MobileAddresslist())
    brand.run()

```



