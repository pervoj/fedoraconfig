from gettext import gettext as _
import os
import subprocess
import colors
from questions import yesno
import status
from action_parts.repositories import do_add_rpmfusion

actions = []


has_nvidia = subprocess.getoutput("lspci | grep -i vga | grep -i nvidia").strip() != ""

def do_nvidia_with_repositories():
	do_add_rpmfusion(True)
	do_nvidia()

def do_nvidia():
	print(_("Installing NVIDIA drivers…"))
	os.system("sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda > /dev/null 2>&1")

def nvidia():
	if yesno(_("Install NVIDIA GPU drivers?")):
		if not status.rpmfusion or not status.rpmfusion_nonfree:
			print()
			print(colors.HEADER + _( # try to keep the text width under 80
				"This option requires added RPM Fusion repositories."
			) + colors.ENDC)
			print()
			if yesno(_("Add RPM Fusion repositories and install NVIDIA GPU drivers?")):
				return do_nvidia_with_repositories
			else: return
		else: return do_nvidia

if has_nvidia: actions.append(nvidia)
