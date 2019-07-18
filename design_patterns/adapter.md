### 适配器模式



![](https://upload-images.jianshu.io/upload_images/14073259-eae0a8c112d98c8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
适配器模式
"""


class Target:
    def request(self):
        print("normal request")


class Adaptee:
    def specific_request(self):
        print("specific request")


class Adapter:
    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.specific_request()


if __name__ == "__main__":
    adapter = Adapter()
    target = adapter
    target.request()

```

