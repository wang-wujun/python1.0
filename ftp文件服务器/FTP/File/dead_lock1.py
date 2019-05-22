"""
    RLock解决死锁
"""
from threading import Thread, RLock
import time

num = 0  # 共享资源
lock = RLock()  # 在一个线程内可以对锁进行重复的上锁


class MyThread(Thread):
    def fun01(self):
        global num
        with lock:  # 上锁
            num -= 1

    def fun02(self):
        global num
        if lock.acquire():
            num += 1
            if num > 5:
                self.fun01()
            print("Num = ", num)
            lock.release()

    def run(self):
        while True:
            time.sleep(2)
            self.fun02()


t = MyThread()
t.start()
t.join()
