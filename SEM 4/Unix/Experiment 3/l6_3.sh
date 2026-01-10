echo "Enter the first string: "
read str1

echo "Enter the second string: "
read str2

if [ "$str1" = "$str2" ]; then
	echo "Strings are equal."
elif [ "$str1" \< "$str2" ]; then
	echo "The first string is smaller than the second string."
elif [ "$str1" \> "$str2" ]; then
	echo "THe first string is greater than the second string."
else
	echo "An unknown error occoured."
fi
