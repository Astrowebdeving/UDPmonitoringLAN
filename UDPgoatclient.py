from socket import *
import sys
import subprocess
import os

s = socket(AF_INET, SOCK_DGRAM)
host = "manager"
port = 7992
max_buf = 1024  
EOT = b'__END_OF_TRANSMISSION__'  

addr = (host, port)
contentfiletest = subprocess.check_output("ip=$(hostname -I | awk '{print $1}')\n cat /etc/hosts | grep $ip | awk '{print $2}'", shell=True, text=True)
#file_name = sys.argv[1]
filelist = [f"updatedmemoryram_{contentfiletest.strip()}.csv", f"updatedstorage_{contentfiletest.strip()}.csv", f"updatedstorage3_{contentfiletest.strip()}.csv", f"allinfile_{contentfiletest.strip()}.txt", "test-100M.csv"]
os.system("python3 newtest.py")


def send(file_name):
    s = socket(AF_INET, SOCK_DGRAM)
    addr = (host, port)
    subprocess.call(['tar', '-czvf', file_name[:-3]+"tar.gz", file_name])
    file_name = file_name[:-3]+"tar.gz"

    s.sendto(file_name.encode('utf-8'), addr)

 
    data, server_addr = s.recvfrom(max_buf)
    new_port = int(data.decode('utf-8'))
    new_addr = (host, new_port)

    with open(file_name, "rb") as f:
        data = f.read(max_buf)
        while data:
            if s.sendto(data, new_addr):
                print("sending ...")
                data = f.read(max_buf)

    s.sendto(EOT, new_addr)
    s.close()
for file in filelist:
    send(file)