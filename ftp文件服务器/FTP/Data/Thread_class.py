"""
    自定义线程类
"""

from threading import Thread


class ThreadClass(Thread):
    def __init__(self, attr):
        self.attr = attr
        super().__init__()

    def fun01(self):
        print("步骤一")

    def fun02(self):
        print("步骤二")

    def run(self):
        self.fun01()
        self.fun02()


t = ThreadClass("xxxx")
t.start()
t.join()
