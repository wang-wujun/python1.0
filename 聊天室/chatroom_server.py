from socket import *
import os, sys

# 服务器地址
ADDR = ("0.0.0.0", 8989)
user = {}
# 进去聊天室
def do_login(s,name,addr):
    if name in user:
        s.sendto("该用户名已被使用".encode(),addr)
        return
    s.sendto(b"OK",addr)

    # 通知其他人
    msg = "欢迎%s进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])

    # 存入用户数据
    user[name] = addr
# 创建网络连接
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    do_request(s)

# 请求处理
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        msg = data.decode().split(" ")
        if msg[0] == "L":
            do_login(s,msg[1],addr)
        print(data.decode())



if __name__ == "__main__":
    main()
