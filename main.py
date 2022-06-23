from gettext import gettext as _
from config import VERSION
import questions
import os
import subprocess
import sys


# check if `/etc/os-release` file exists
# with this we also check if we are on Linux
if not os.path.exists("/etc/os-release"):
	print(_("Error: File `/etc/os-release` not found!"))
	print(_("       You are not on Fedora or your system is broken!"))
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
	print(_("Error: You are not on Fedora or your system is broken!"))
	exit(1)
if version != VERSION:
	print(_(f"Error: This script is made for Fedora {VERSION}!"))
	exit(1)


os.system("clear")


# if we don't have sudo privileges, run again with sudo
if os.geteuid() != 0:
	print(_("This program needs sudo privileges."))
	print(_("We will ask you for your password."))
	print()
	if not questions.yesno(_("Do you agree?")):
		print()
		print(_("Error: This program needs sudo privileges."))
		exit(1)
	print()
	subprocess.call([
		"sudo",
		f"-p" + _("Please, enter your password: "),
		"python",
		*sys.argv
	])
	exit(0)


print("The program will continue here!")
