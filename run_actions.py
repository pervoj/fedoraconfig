from gettext import gettext as _
import colors
from actions import actions
from functions import clear

runners = []

for index, action in enumerate(actions):
	clear()
	print(
		colors.OKBLUE +
		_("[question {} of {}]").format(index + 1, len(actions)) +
		colors.ENDC
	)
	print()
	print(colors.WARNING + _( # try to keep the text width under 80
		"If you don't know what the option means, just press Enter to select the default\n"+
		"answer. The default answers are chosen to suit as many people as possible."
	) + colors.ENDC)
	print()
	runner = action()
	if (runner != None): runners.append(runner)

clear()

print(colors.WARNING + _( # try to keep the text width under 80
	"Now wait a while until everything is ready."
) + colors.ENDC)
print()

for runner in runners:
	runner()

clear()
