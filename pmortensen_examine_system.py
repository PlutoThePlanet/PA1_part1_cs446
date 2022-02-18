# 1. CPU type and model
file1 = open("proc/", "r")

# 2. Kernel version details
file2 = open("proc/", "r")

# 3. Amount of time since last boot, as dd:hh:mm:ss (1 day 4 hours 21 minutes and 1 second would print as 01:04:21:01)
file3 = open("proc/", "r")

# 4. The time that the system was last booted (same format)- Note: this is not the same as 3
file4 = open("proc/", "r")

# 5. The number of disk requests made
file5 = open("proc/", "r")

# 6. The number of processes created since last boot
file6 = open("proc/", "r")
