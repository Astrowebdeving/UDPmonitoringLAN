from socket import *
import time
from concurrent
import subprocess
import threading

host="0.0.0.0"

workerlist = ["worker1", "worker2"]
host2 = workerlist[0]
port = 7990
port2 = 8800


s2 = socket(AF_INET,SOCK_DGRAM)


addr2 = (host2, port2)

buf=128
Connected = True
while Connected:
    s = socket(AF_INET,SOCK_DGRAM)
    addr = (host,port)
    s.bind((host,port))
    start_time = time.process_time()
    data,addr = s.recvfrom(buf)
    print("Received File:", data.strip().decode('utf-8'))
    Filename = data.strip().decode('utf-8')
    f = open(data.strip(),'wb')

    data,addr = s.recvfrom(buf)
    try:
        while(data):
            f.write(data)
            s.settimeout(3)
            data,addr = s.recvfrom(buf)
    except timeout:
        f.close()
        s.close()
        print(Filename, "Downloaded")
        end_time = time.process_time()
        print(f"CPU time used: {end_time - start_time} seconds")
        subprocess.call(['tar', '-xzvf', Filename])
