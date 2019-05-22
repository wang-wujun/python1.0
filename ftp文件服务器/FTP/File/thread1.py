"""
    线程示例
"""

import threading
from time import sleep
import os

a = 1
# 线程函数
def music():
    global a
    print("a = ",a)
    a =100
    for i in range(5):
        sleep(2)
        print("播放 爱如潮水",os.getpid())


# 创建线程对象
t = threading.Thread(target=music)
t.start()
# 主进程任务
for i in range(3):
    sleep(2)
    print("播放 过火",os.getpid())
    print("主:",a)
t.join()
print("end;",a)