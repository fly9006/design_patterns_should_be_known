### 命令模式



![](https://upload-images.jianshu.io/upload_images/14073259-593030191854baec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
命令模式
"""


class Receiver:

    def action(self):
        print("excute the command")


class Command:

    def __init__(self, receiver: Receiver):
        self.recerver = receiver

    def excute(self):
        pass


class ConcreteCommand(Command):

    def __init__(self, receiver: Receiver):
        super().__init__(receiver)

    def excute(self):
        self.recerver.action()


class Invoker:

    def __init__(self):
        self.command = None

    def set_command(self, command: ConcreteCommand):
        self.command = command

    def excute_command(self):
        self.command.excute()


if __name__ == "__main__":

    r = Receiver()
    c = ConcreteCommand(r)
    i = Invoker()
    i.set_command(c)
    i.excute_command()

```

