from gettext import gettext as _
import os
from questions import yesno

actions = []


def do_install_codecs():
	print(_("Installing multimedia codecs…"))
	os.system("sudo dnf groupupdate -y multimedia --setop='install_weak_deps=False' --exclude=PackageKit-gstreamer-plugin > /dev/null 2>&1")
	os.system("sudo dnf groupupdate -y sound-and-video > /dev/null 2>&1")

def install_codecs():
	if yesno(_("Install multimedia codecs?")):
		return do_install_codecs

actions.append(install_codecs)
