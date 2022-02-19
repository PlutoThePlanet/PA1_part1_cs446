import subprocess

# 1. CPU type and model
subprocess.call("cat /proc/cpuinfo >> pmortensen_systemDetails.txt", shell=True)  # cat from cpuInfo to given file name

# 2. Kernel version details
subprocess.call("cat /proc/version >> pmortensen_systemDetails.txt", shell=True)

# 3. Amount of time since last boot
subprocess.call("cat /proc/uptime --pretty >> pmortensen_systemDetails.txt", shell=True)  # length of time since been up

# 4. The time that the system was last booted (same format)- Note: this is not the same as 3
subprocess.call("cat /proc/uptime --since >> pmortensen_systemDetails.txt", shell=True)  # date since been up

# 5. The number of disk requests made
# file5 = open("proc/", "r")

# 6. The number of processes created since last boot
# file6 = open("proc/", "r")


'''
Example:
file1 = open("/proc/uptime", "r")
uptimeData = file1.readlines()
print(uptimeData)

OR 

subprocess.call("cat /proc/cpuinfo >> pmortensen_systemDetails.txt", shell=True)  # cat from cpuInfo to given file name

https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://stackoverflow.com/questions/21135694/using-greater-than-operator-with-subprocess-call

'''