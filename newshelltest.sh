#!/usr/bin/bash
touch storage.txt
touch storage.csv
macaddress=$(ip -o link show dev eno1 | grep -Po 'ether \K[^ ]*')
ip=$(hostname -I | awk '{print $1}')
name=$(cat /etc/hosts | grep $ip | awk '{print $2}')
touch "updatedstorage_${name}.csv"
dateinfo=$(date)

df -m | grep t | cat> storage.txt
awk '{OFS=","};NR>1 {print $1,$2,$3,$4,$5,$NF}' storage.txt > storage.csv
awk -v data="$dateinfo" -F"," 'BEGIN{OFS = ","}{$7=data; print}' storage.csv > "updatedstorage_${name}.csv"
touch "sysname_${name}.txt"
touch "overallstorage_${name}.txt"
touch "amountused_${name}.txt"
touch "amountavailable_${name}.txt"
touch "usage_${name}.txt"
touch "location_${name}.txt"
touch "date_${name}.txt"

awk 'NR>1 {print $1}' storage.txt > "sysname_${name}.txt"
awk 'NR>1 {print $2}' storage.txt > "overallstorage_${name}.txt"
awk 'NR>1 {print $3}' storage.txt > "amountused_${name}.txt"
awk 'NR>1 {print $4}' storage.txt > "amountavailable_${name}.txt"
awk 'NR>1 {print $5}' storage.txt > "usage_${name}.txt"
awk 'NR>1 {print $6}' storage.txt > "location_${name}.txt"
awk -F"," 'NR>1 {print $7}' "updatedstorage_${name}.csv" > "date_${name}.txt" 