# UDPmonitoringLAN
A synchronous 2 server 2 client system for monitoring devices on a local LAN. Can scale to multiple workers with one head machine.

Pull the repository to every machine. It is necessary to change the /etc/hosts file to include the subnet LAN ip address of the host machines and their roles. For example, on the manager the /etc/hosts will include 192.168.1.x manager \n 192.168.1.x worker1 \n 192.168.1.x worker2.

After this is done, call nohup python3 startingserverUDP.py & on all worker machines and nohup python3 UDPgoatserver.py & on the manager machine from the repository. This will finish the environment set up. 

To call for data and to update the stored data, simply use python3 startingclientUDP.py to call startingserverUDP.py to begin its process which calls the UDPgoatclient.py file which will initiate the data collection, compression, and transfer. 
On the manager node, the updated data will be present. 
