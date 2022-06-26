from gettext import gettext as _
import os
from questions import yesno, int_with_default

actions = []


def do_parallel_downloads(count):
	print(_("Enabling more parallel downloads…"))
	os.system(f"sudo echo -e '\\nmax_parallel_downloads={count}' >> /etc/dnf/dnf.conf")

def parallel_downloads():
	if yesno(_("Increase the count of maximal parallel downloads?")):
		count = int_with_default(_("On which number you want to set the maximal count?"), 10)
		return lambda: do_parallel_downloads(count)

actions.append(parallel_downloads)


def do_default_yes():
	print(_("Enabling default yes in DNF…"))
	os.system(f"sudo echo -e '\\ndefaultyes=True' >> /etc/dnf/dnf.conf")

def default_yes():
	if yesno(_("Set DNF default value to yes?"), False):
		return do_default_yes

actions.append(default_yes)


def do_fastest_mirror():
	print(_("Enabling the fastest mirror…"))
	os.system("sudo echo -e '\\nfastestmirror=True' >> /etc/dnf/dnf.conf")

def fastest_mirror():
	if yesno(_("Automatically find the fastest mirror?"), False):
		return do_fastest_mirror

actions.append(fastest_mirror)


def do_keep_cache():
	print(_("Enabling default yes in DNF…"))
	os.system(f"sudo echo -e '\\nkeepcache=True' >> /etc/dnf/dnf.conf")

def keep_cache():
	if yesno(_("Keep DNF cache?"), False):
		return do_keep_cache

actions.append(keep_cache)


def do_update():
	print(_("Updating packages…"))
	os.system(f"sudo dnf update -y > /dev/null 2>&1")

def update():
	if yesno(_("Update packages?"), True):
		return do_update

actions.append(update)
