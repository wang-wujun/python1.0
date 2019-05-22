"""
    自定义线程类
"""
from threading import Thread
from time import sleep, ctime


class Mythread(Thread):
    def __init__(self, target=None, args=(), kwargs=None, name=None):
        super().__init__()
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self, ):
        self.target(*self.args, **self.kwargs)


# *******************************************
# 通过完成上面的MyThread类让整个程序可以正常执行
# 当调用start时player作为一个线程功能函数运行
# 注意,函数的名称和参数不确定,player只是测试函数)
# ******************************************
def player(sec, song):
    for i in range(2):
        print("Playing %s:%s" % (song, ctime()))
        sleep(sec)


t = Mythread(target=player, args=(3,), kwargs={"song": "凉凉"}, \
             name="happy")
t.start()
t.join()
