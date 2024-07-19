from socket import *
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
import os

host = "0.0.0.0"
port = 7992
max_buf = 1024  
corebase = subprocess.check_output("nproc", shell=True, text=True)
MAX_WORKERS = int(corebase)*2  
EOT = b'__END_OF_TRANSMISSION__'  

def handle_client(sock, addr, initial_data):
    try:
        filename = initial_data.strip().decode('utf-8')
        print(f"Received file request from {addr}: {filename}")

        transfer_sock = socket(AF_INET, SOCK_DGRAM)
        transfer_sock.bind((host, 0))  

        new_port = transfer_sock.getsockname()[1]
        sock.sendto(str(new_port).encode('utf-8'), addr)

        handle_file_transfer(transfer_sock, filename, addr)

    except Exception as e:
        print(f"Exception occurred for client {addr}: {e}")


def handle_file_transfer(sock, filename, addr):
#    start_time = time.process_time()
    with open(filename, 'wb') as f:
        try:
            while True:
                data, client_addr = sock.recvfrom(max_buf)
                if data == EOT:
                    print(f"End of transmission from {client_addr}")
                    break
#                print(f"Received data from {client_addr}: {data[:50]}...")  # Debugging line
                if not data or client_addr != addr:
                    break
                f.write(data)
        except timeout:
            pass  
#    end_time = time.process_time()
#    print(f"File {filename} received and saved. CPU time used: {end_time - start_time} seconds")
    subprocess.call(['tar', '-xzvf', filename])
    sock.close()
    if filename=="allinfile_worker2.tar.gz" | filename=="allinfile_worker1.tar.gz":
        result = subprocess.run(['date', '+"%T.%N"'], capture_output=True, text=True)
        completion_time = result.stdout.strip()
        bash_command = f'export {'endtime'}="{completion_time}"'
        with open(os.getenv('HOME') + '/.bashrc', 'a') as bashrc:
            bashrc.write(f'\n{bash_command}\n')

def main():
    global sock
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((host, port))
    print(f"Server listening on {host}:{port}...")

    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    try:
        while True:
            data, addr = sock.recvfrom(max_buf)
#            print(f"Initial data from {addr}: {data}")  

            executor.submit(handle_client, sock, addr, data)

    except Exception as e:
        print(f"Exception occurred in main server loop: {e}")

    finally:
        sock.close()

if __name__ == '__main__':
    main()
