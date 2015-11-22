#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Please supply a folder name"
fi

echo Using folder \'$1\' as base files

next_folder_name=$(($1-1))
echo Copying to folder $next_folder_name
cp -r $1 $next_folder_name

echo Removing last line from all .cnf files in $next_folder_name
cd $next_folder_name
sed -i '$ d' *.cnf
