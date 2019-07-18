### 原型模式



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
原型模式
"""

from copy import deepcopy


class Resume:

    def __init__(self):

        self.name = ""
        self.sex = ""
        self.age = ""
        self.timearea = ""
        self.company = ""

    def set_name(self, name):
        self.name = name

    def set_sex(self, sex):
        self.sex = sex

    def set_age(self, age):
        self.age = age

    def set_timearea(self, timearea):
        self.timearea = timearea

    def set_company(self, company):
        self.company = company

    def display(self):
        print(self.name, self.sex, self.age, self.timearea, self.company)

    def copy(self):
        return self

    def deep_copy(self):
        return deepcopy(self)


if __name__ == "__main__":

    r = Resume()
    r.set_name("test")
    r.set_age("21")
    r.set_sex("man")
    r.set_timearea("china")
    r.set_company("micro")
    r.display()

    r1 = r.copy()
    r1.set_age("22")
    r1.display()

    r2 = r.deep_copy()
    r2.set_company("winner")
    r2.display()

    print(id(r), id(r1), id(r2))

```

