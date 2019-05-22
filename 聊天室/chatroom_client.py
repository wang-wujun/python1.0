from socket import *
import os, sys

# 服务器地址
ADDR = ("127.0.0.1", 8989)


# 创建网络连接
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() == "ok":
            print("您已经入聊天室")
            break
        else:
            print(data.decode())



if __name__ == '__main__':
    main()

