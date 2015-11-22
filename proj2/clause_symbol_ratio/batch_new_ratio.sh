#!/bin/bash

if [ "$#" -ne 1 ]
then
  echo "Please supply a folder name"
fi

for ((i=$1;i>=10;i--))
do
  bash new_ratio.sh $i
done
