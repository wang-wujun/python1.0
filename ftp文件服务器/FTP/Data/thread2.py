from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec, name):
    print("线程传参")
    sleep(sec)
    print("%s 线程执行完毕" % name)


# 创建多个线程
jobs = []  # 创建多个线程放入列表
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={"name": "T%d" % i})
    jobs.append(t)
    t.start()

for i in jobs:  # 逐个回收线程
    i.join()
