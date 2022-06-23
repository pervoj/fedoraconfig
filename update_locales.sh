template="po/template.pot"

# generate pot file
xgettext -f po/POTFILES -o $template

languages=$(cat po/LINGUAS)
for language in $languages
do
	if [[ ! -z "$language" ]]; then
		file="po/$language.po"
		if [[ -f "$file" ]]; then
			msgmerge -U $file $template 2> /dev/null
		else
    		msginit --no-translator -i $template -o $file 2> /dev/null
		fi
	fi
done

# remove pot file
rm $template
