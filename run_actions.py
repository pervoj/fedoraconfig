from actions import actions
from functions import clear

runners = []

for action in actions:
	clear()
	runner = action()
	if (runner != None): runners.append(runner)

clear()

for runner in runners:
	runner()

clear()
