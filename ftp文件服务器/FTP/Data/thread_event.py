"""
    线程Event(互斥)
"""
from threading import Thread,Event
from time import sleep

s = None  #　全局变量用于通信
e = Event() #　事件对象

def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() #　共享资源操作完毕

t = Thread(target=杨子荣)
t.start()
print("说对口令就是自己人")

e.wait()  #　阻塞等待
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他...")

t.join()