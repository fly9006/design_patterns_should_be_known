### 状态模式



![](https://upload-images.jianshu.io/upload_images/14073259-a0a885cc1742eb54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
状态模式
"""


class State:
    def write_program(self, work):
        pass


class Work:
    def __init__(self):
        self.current_hour = 9
        self.state = ForenoonState()

    def set_state(self, state: State):
        self.state = state

    def write_program(self):
        self.state.write_program(self)


class ForenoonState(State):
    def write_program(self, work: Work):
        if work.current_hour < 12:
            print("morning working")
        work.set_state(NoonState())
        work.write_program()


class NoonState(State):
    def write_program(self, work: Work):
        if work.current_hour < 13:
            print("have fun")
        else:
            print("need to rest")


if __name__ == "__main__":

    day_work = Work()
    day_work.current_hour = 9
    day_work.write_program()
    day_work.current_hour = 15
    day_work.write_program()

```

