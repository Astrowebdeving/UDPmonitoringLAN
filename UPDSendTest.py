from socket import *
import sys
import os


s = socket(AF_INET,SOCK_DGRAM)
s2 = socket(AF_INET,SOCK_DGRAM)
host = "manager"
port = 7990
port2 = 8800
buf = 128

host2 = "0.0.0.0"
addr = (host,port)

addr2 = (host2, port2)


s2.bind(host2,port)

file_name=sys.argv[1]

os.system("python3 newtest.py")

s.sendto(file_name.encode('utf-8'),addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)

s.close()
f.close()