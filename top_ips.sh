#!/bin/bash

# check for command line argument
if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` [domain]"
    exit 1
fi

awk '{ print $1}' /home/$1/var/$1.org/logs/transfer.log | sort  | uniq -c  | sort -nr | grep -v "^[[:space:]]*[[:digit:]][[:space:]]"