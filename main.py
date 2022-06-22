# Script config:
# ==============

# Fedora version
VERSION = "36"


import questions
import os
import subprocess
import sys


# check if `/etc/os-release` file exists
# with this we also check if we are on Linux
if not os.path.exists("/etc/os-release"):
	print("Error: File `/etc/os-release` not found!")
	print("       You are not on Fedora or your system is broken!")
	exit(1)

# check if we are on Fedora
distro = ""
version = ""
with open("/etc/os-release", "r", encoding = "utf-8") as f:
	for line in f.readlines(): # extract distro and version from the file
		pair = line.strip().split("=")
		if pair[0] == "ID": distro = pair[1]
		elif pair[0] == "VERSION_ID": version = pair[1]
# check matches
if distro != "fedora":
	print("Error: You are not on Fedora or your system is broken!")
	exit(1)
if version != VERSION:
	print(f"Error: This script is made for Fedora {VERSION}")
	exit(1)


os.system("clear")


# if we don't have sudo privileges, run again with sudo
if os.geteuid() != 0:
	print("This program needs sudo privileges.")
	print("We will ask you for your password.")
	if not questions.yesno("Do you agree?"):
		print("Error: This program needs sudo privileges.")
		exit(1)
	subprocess.call(['sudo', 'python', *sys.argv])
	exit()


print("The program will continue here!")
