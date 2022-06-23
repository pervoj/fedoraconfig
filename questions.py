from gettext import gettext as _

def yesno(question: str, defaultYes: bool = True) -> bool:
	# letter to use as "YES" answer
	YES = _("y")
	# letter to use as "NO" answer
	NO = _("n")
	default = f"{YES.upper()}/{NO.lower()}"
	if not defaultYes: default = f"{YES.lower()}/{NO.upper()}"
	while True:
		answer = input(f"{question} [{default}] ").strip().lower()
		if answer == "": return defaultYes
		if answer == YES.lower(): return True
		if answer == NO.lower(): return False
		print(_("Invalid entry! Please, try again:"))
