#!/usr/bin/bash


read -p "Enter name: " NAME

if [ "$NAME" = "KAK" ]; then
	echo "My name is $NAME"
else
	echo "Wrong name"
fi
