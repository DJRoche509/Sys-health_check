#!/usr/bin/env python3
import shutil
import psutil

#this function receives a disk(parameter), checks it and returns true if it's more than 20% free and false if it's less
def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

#the check_cpu_usage checks the machine for one second. Will say the machine is healthy (True) if cpu usage is less than 75%
def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

#Main body of the script that checks if either of those two functions return false
if not check_disk_usage("/") or not check_cpu_usage():
	print("Error!")
else:
	print("Everything is OK")