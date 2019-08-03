### 享元模式



![](https://upload-images.jianshu.io/upload_images/14073259-344b9d984c9f76a9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
享元模式
"""


class User:

    def __init__(self, name):
        self.name = name


class Website:

    def use(self, user: User):
        pass


class ConcrateWebsite(Website):

    def __init__(self, name):
        self.name = name

    def use(self, user: User):
        print(f"website:{self.name}, usert:{user.name}")


class WebsiteFactory:

    def __init__(self):
        self.flyweights = {}

    def get_website_category(self, key):
        if key not in self.flyweights.keys():
            self.flyweights.update({key: ConcrateWebsite(key)})
        return self.flyweights[key]

    def get_website_count(self):
        return len(list(self.flyweights.keys()))


if __name__ == "__main__":

    f = WebsiteFactory()

    fx = f.get_website_category("blog")
    fx.use(User("john"))

    fy = f.get_website_category("blog")
    fy.use(User("tom"))

    print(f.get_website_count())




```

