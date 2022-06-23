#!/usr/bin/env python

import compile_locales
from config import PATH, GETTEXT_PACKAGE
import gettext
from os.path import join

gettext.bindtextdomain(GETTEXT_PACKAGE, join(PATH, "mo"))
gettext.textdomain(GETTEXT_PACKAGE)

try:
	import main
except KeyboardInterrupt: print()
