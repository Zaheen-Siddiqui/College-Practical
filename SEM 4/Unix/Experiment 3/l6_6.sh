echo "Current directory is: $(pwd)"

echo "Contents of current directory:"
ls -l

echo "Enter the name of directory:"
read newDir

mkdir -p "$newDir"
echo "$newDir directory has been created."

echo "Enter the name of file in $newDir"
read NewFile

echo "Enter the content to write into the file: "
read filecontent
echo "$filecontent" > "$newDir/$NewFile"
echo "File has been created"
cp -r "$newDir" ~/newDirCopy
echo "$newDir has been copied to ~/newDirCopy"
echo "Operations Completed Successfully"
