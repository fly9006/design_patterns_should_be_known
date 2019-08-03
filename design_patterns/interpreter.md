### 解释器模式

![](https://upload-images.jianshu.io/upload_images/14073259-e98f5358a06229b4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
解释器模式
"""


class Context:

    def __init__(self):
        self.input = ""
        self.output = ""


class AbstractExpression:

    def interpret(self, context: Context):
        pass


class TerminalExpression(AbstractExpression):

    def interpret(self, context: Context):
        print("terminal interpret")


class NoneTerminalExpression(AbstractExpression):

    def interpret(self, context: Context):
        print("noneterminal interpret")


if __name__ == "__main__":
    context = ""
    interprets = [TerminalExpression(), NoneTerminalExpression(), TerminalExpression()]
    for i in interprets:
        i.interpret(context)

```



