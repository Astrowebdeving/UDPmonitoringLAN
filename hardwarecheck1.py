import sys, os, time
#Following is importing the first column of data about system names to a listofsystems list of strings
listofsystems =[]
listof1kstorage = []
listofmemoryusage = []
listofavailable = []
listofusage=[]
listoflocations=[]
listofdates=[]
listoflists = [listofsystems, listof1kstorage, listofmemoryusage, listofavailable, listofusage, listoflocations, listofdates]
listoffiles = [f"sysname.txt", f"overallstorage.txt", f"amountused.txt", f"amountavailable.txt", f"usage.txt", f"location.txt", f"date.txt"]

count=1
for list in listoflists:
    path = f"/home/aistudent/first/second/third/{listoffiles[count-1]}"
    file = open(path, 'r')
    listofcontents=file.readlines()
    os.system(f'echo {listoffiles[count-1]} is being stored')
    for line in listofcontents:
        list.append(line.strip())
    file.close()
    count+=1
for list in listoflists:
    print(list)

