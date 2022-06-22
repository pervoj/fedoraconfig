def yesno(question: str, defaultYes: bool = True) -> bool:
	default = "Y/n"
	if not defaultYes: default = "y/N"
	while True:
		answer = input(f"{question} [{default}] ").strip().lower()
		if answer == "": return defaultYes
		if answer == "y": return True
		if answer == "n": return False
		print("Invalid entry! Please, try again:")
