### 职责链模式



![](https://upload-images.jianshu.io/upload_images/14073259-29981b68de6f5322.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
职责链模式
"""


class Request:

    def __init__(self):
        self.type = None
        self.content = None
        self.number = 0


class Manager:

    def __init__(self, name):
        self.name = name
        self.superior = None

    def set_superior(self, superior):
        self.superior = superior

    def handle_request(self, request: Request):
        pass


class CommonManager(Manager):

    def __init__(self, name):
        super().__init__(name)

    def handle_request(self, request: Request):

        if request.type == "请假":
            print(f"{self.name}批准{request.content}请求")
        else:
            if self.superior:
                self.superior.request(request)


class Major(Manager):

    def __init__(self, name):
        super().__init__(name)

    def handle_request(self, request: Request):

        if request.type == "长假":
            print(f"{self.name}批准{request.content}请求")
        else:
            if self.superior:
                self.superior.request(request)


class GeneralManager(Manager):

    def __init__(self, name):
        super().__init__(name)

    def handle_request(self, request: Request):
        print(f"{self.name}批准{request.content}请求")


if __name__ == "__main__":

    manager = CommonManager("经理")
    major = Major("总监")
    general_manager = GeneralManager("总经理")
    manager.set_superior(major)
    major.set_superior(general_manager)

    r = Request()
    r.type = "请假"
    r.content = "某某人请假"
    r.number = 1
    manager.handle_request(r)

```

