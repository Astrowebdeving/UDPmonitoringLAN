#!/usr/bin/bash
macaddress=$(ip -o link show dev eno1 | grep -Po 'ether \K[^ ]*')
ip=$(hostname -I | awk '{print $1}')
name=$(cat /etc/hosts | grep $ip | awk '{print $2}')
touch allinfile_${name}.txt

totalcpu=$(top -bn1 -d0.01 | grep "Cpu(s)" | awk 'NR==1 {print $2 + $4}')
totalram=$(free -h | awk '{print $3}' | tr -d 'fre, ' | sed 's/ //g' | awk 'NR<3 {print $1}')
totaldisk=$(df -m | awk '{sum+=$5;} END{print sum;}')
echo The cpu usage is $totalcpu, the total ram usage is $totalram, the total disk usage is $totaldisk. This is one machine $macaddress.> allinfile_${name}.txt