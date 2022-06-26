#!/usr/bin/env python

import compile_locales
from config import PATH, GETTEXT_PACKAGE
import gettext
from os.path import join
import shutil

gettext.bindtextdomain(GETTEXT_PACKAGE, join(PATH, "mo"))
gettext.textdomain(GETTEXT_PACKAGE)

try:
	import main
except KeyboardInterrupt: print()

try:
	shutil.rmtree(join(PATH, "mo"))

	shutil.rmtree(join(PATH, "__pycache__"))
	shutil.rmtree(join(PATH, "action_parts", "__pycache__"))
except FileNotFoundError: pass
