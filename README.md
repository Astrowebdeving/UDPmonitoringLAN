# UDPmonitoringLAN
A synchronous 2 server 2 client system for monitoring devices on a local LAN. Can scale to multiple workers with one head machine.

Pull the repository to every machine. It is necessary to change the /etc/hosts file to include the subnet LAN ip address of the host machines and their roles. For example, on the manager the /etc/hosts will include 192.168.1.x manager \n 192.168.1.x worker1 \n 192.168.1.x worker2.

After this is done, call nohup python3 startingserverUDP.py & on all worker machines and UDPgoatserver.py on the manager machine. 
