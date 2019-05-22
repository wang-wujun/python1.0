"""
    线程属性
"""
from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun, name="aj2019")

# 主线程退出,分线程也退出
t.setDaemon(True)

t.start()
# 线程名称
t.setName("aj2009")  # 修改名称
print("Tread name:", t.getName())

# 线程生命周期
print("is alive:", t.is_alive())  # 线程执行结束,线程结束

#
