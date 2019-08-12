### 抽象工厂模式



![](https://upload-images.jianshu.io/upload_images/14073259-c30dcf09e0ee6556.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
抽象工厂模式
"""


class IUser:

    def get_user_name(self):
        pass


class SqlserverUser(IUser):

    def get_user_name(self):
        return print("sqlserver user")


class AccessUser(IUser):

    def get_user_name(self):
        return print("access user")


class IDepartment:

    def get_department_name(self):
        pass


class SqlserverDepartment(IDepartment):

    def get_department_name(self):
        return print("sqlserver department")


class AccessDepartment(IDepartment):

    def get_department_name(self):
        return print("access department")


class IFactory:

    def create_user(self):
        pass

    def create_department(self):
        pass


class SqlserverFactory(IFactory):

    def create_user(self):
        return SqlserverUser()

    def create_department(self):
        return SqlserverDepartment()


class AccessFactory(IFactory):

    def create_user(self):
        return AccessUser()

    def create_department(self):
        return AccessDepartment()


if __name__ == "__main__":
    factory = SqlserverFactory()
    user = factory.create_user()
    department = factory.create_department()
    user.get_user_name()
    department.get_department_name()

```

