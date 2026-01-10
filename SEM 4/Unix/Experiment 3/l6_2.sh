elements=("Apple" "Banana" "Cherry" "Elderberry")

echo "Enter the element to search: "
read searc

found=0

for element in "${elements[@]}"
do
	if [ "$element" == "$searc" ]; then
		found=1
		break
	fi
done

if [ $found -eq 1 ]; then
	echo "Element '$searc' is in the list."
else
	echo "Element '$searc' is not in the list."
fi
