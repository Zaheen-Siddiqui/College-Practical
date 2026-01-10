echo "Enter the path for dirctiory/file check"
read path

if [ -e "$path" ]; then
	if [ -d "$path" ]; then
		echo "'$path' exists and is a dirctiory"
	elif [ -f "$path" ]; then
		echo "'$path' exists and is a file"
	else
		echo "'$path' exists but is not a file or directory"
	fi
else
	echo "'$path' does not exist"
	echo "Do you want to create aa dirctiory or a file check(D/F)"
	read choice
	if [ "$choice" = "D" ] || [ "$choice" = "d" ]; then
		mkdir -p "$path"
		echo "Directory '$path' created."
	elif [ "$choice" = "F" ] || [ "$choice" = "f" ]; then
	mkdir -p "$(dirname "$path")"
	touch "$path"
	echo "File '$path' created."
	else
		echo "Incorrect option."
	fi
fi
