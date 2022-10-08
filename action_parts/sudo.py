from gettext import gettext as _
import os
import re
from questions import yesno, int_with_default

actions = []


def do_asterisks():
	print(_("Enabling asterisks while typing sudo password…"))
	os.system(f"sudo cp /etc/sudoers /etc/sudoers.bkp")
	ex = re.compile("Defaults +env\_reset")
	with open("/etc/sudoers", "r") as f:
		content = f.read()
	m = ex.search(content)
	with open("/etc/sudoers", "w") as f:
		f.write(content.replace(m.group(), f"{m.group()},pwfeedback"))

def asterisks():
	if yesno(_("Show asterisks while typing sudo password?")):
		return do_asterisks

actions.append(asterisks)
