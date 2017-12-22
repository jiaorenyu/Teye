#!/bin/bash
if [ $# != 1 ]; then
	echo "usage: ./deploy.sh install_path"
	exit 1
fi


install_path=$1
mkdir -p $install_path/conf
mkdir -p $install_path/logs
mkdir -p $install_path/run

files="*"

for file in $files; do
	echo $file
	cp -r $file $install_path
done
