from gettext import gettext as _
import os
from questions import yesno

actions = []


def do_add_flathub():
	print(_("Adding Flathub repository…"))
	os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")

def add_flathub():
	if yesno(_("Add Flathub repository to be able to download more apps?")):
		return do_add_flathub

actions.append(add_flathub)


def do_add_rpmfusion(nonfree):
	print(_("Adding RPM Fusion repository…"))
	os.system("sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm > /dev/null 2>&1")
	if nonfree: os.system("sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm > /dev/null 2>&1")
	os.system("sudo dnf groupupdate -y core > /dev/null 2>&1")

def add_rpmfusion():
	if yesno(_("Add RPM Fusion repository to be able to download more apps?")):
		nonfree = yesno(_("Are you fine with non-free apps?"))
		return lambda: do_add_rpmfusion(nonfree)

actions.append(add_rpmfusion)
