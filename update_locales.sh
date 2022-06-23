gettext_package="fedoraconfig"
template="po/$gettext_package.pot"

# generate pot file
xgettext -f po/POTFILES -o $template -c
sed -i "s/PACKAGE VERSION/fedoraconfig/g" $template

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
