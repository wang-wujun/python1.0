"""
    死锁的示例,延迟操作避免死锁
"""
import time
import threading


# 交易类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id  # 用户
        self.balance = balance  # 存款
        self.lock = lock

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看账户金额
    def get_balance(self):
        return self.balance


def transfer(from_, to, amount):
    if from_.lock.acquire():  # 锁住自己的账户,上锁成功返回True
        from_.withdraw(amount)  # 自己账户金额减少
        time.sleep(0.5)
        if to.lock.acquire():  # 对方账户上锁
            to.deposit(amount)  # 对方账户金额增加
            to.lock.release()  # 对方账户解锁
        from_.lock.release()  # 自己账户解锁
    print("转账完成")


# 创建两个账户
ls = Account("ls", 5000, threading.Lock())
hd = Account("hd", 3000, threading.Lock())

t1 = threading.Thread(target=transfer, args=(ls, hd, 2000))
t2 = threading.Thread(target=transfer, args=(hd, ls, 1000))
t1.start()
time.sleep(3)  # 延迟操作,防止同时锁.形成死锁
t2.start()
t1.join()
t2.join()

print("ls:", ls.get_balance())
print("hd:", hd.get_balance())
