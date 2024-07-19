#!/usr/bin/bash
touch storage3.txt
touch storage3.csv
macaddress=$(ip -o link show dev eno1 | grep -Po 'ether \K[^ ]*')
ip=$(hostname -I | awk '{print $1}')
name=$(cat /etc/hosts | grep $ip | awk '{print $2}')
touch "updatedstorage3_${name}.csv"
dateinfo=$(date)

top -bn 1 | sed -n '/PID/,$p' | grep -v top | grep s |  cat > storage3.txt
awk '{OFS=","};NR>1 {print $1,$2,$3,$9,$10,$13}' storage3.txt > storage3.csv
awk -v data="$dateinfo" -F"," 'BEGIN{OFS = ","}{$7=data; print}' storage3.csv > "updatedstorage3_${name}.csv"
touch "sPID_${name}.txt"
touch "userfound_${name}.txt"
touch "PRstoring_${name}.txt"
touch "cpupercentage_${name}.txt"
touch "mempercentage_${name}.txt"
touch "location3_${name}.txt"
touch "date3_${name}.txt"
awk 'NR>1 {print $1}' storage3.txt > "sPID_${name}.txt"
awk 'NR>1 {print $2}' storage3.txt > "userfound_${name}.txt"
awk 'NR>1 {print $3}' storage3.txt > "PRstoring_${name}.txt"
awk 'NR>1 {print $4}' storage3.txt > "cpupercentage_${name}.txt"
awk 'NR>1 {print $5}' storage3.txt > "mempercentage_${name}.txt"
awk 'NR>1 {print $6}' storage3.txt > "location3_${name}.txt"
awk -F"," 'NR>1 {print $7}' "updatedstorage3_${name}.csv" > "date3_${name}.txt"