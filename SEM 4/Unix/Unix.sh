#!/bin/bash

echo "Hello, what is your name?"
read name
echo "Welcome, $name!"

if [ "$name" != "" ]; then
	echo "$name, hope you're learning a lot about shell scripting!"
else
	echo "Please enter your name next time."
fi
