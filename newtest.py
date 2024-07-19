import os

os.system(f"echo Outputting Disk Space Usage")
os.system(f"./newshelltest.sh")
os.system(f"echo Outputting CPU processes and usage")
os.system(f"./secondshelltest.sh")
os.system(f"echo Outputting memory usage processes")
os.system(f"./memoryshell.sh")
os.system("./allinfile.sh")