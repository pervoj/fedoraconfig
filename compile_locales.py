from config import PATH, GETTEXT_PACKAGE
import os
import shutil

PO = os.path.join(PATH, "po")
MO = os.path.join(PATH, "mo")

# create mo directory
if os.path.exists(MO):
	shutil.rmtree(MO)
os.makedirs(MO)

# list all locales
with open(os.path.join(PO, "LINGUAS"), "r", encoding = "utf-8") as f:
	for line in f.readlines():
		language = line.strip()
		if len(language) <= 0: continue
		file = f"{language}.po"
		# prepare paths
		path_po = os.path.join(PO, file)
		dir_mo = os.path.join(MO, language, "LC_MESSAGES")
		path_mo = os.path.join(dir_mo, f"{GETTEXT_PACKAGE}.mo")
		# create language directory in mo dir
		os.makedirs(dir_mo)
		# generate mo file
		os.system(f"msgfmt {path_po} -o {path_mo}")
