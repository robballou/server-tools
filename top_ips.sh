#!/bin/bash

# check for command line argument
if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` [domain]"
    exit 1
fi

export TLD="UNKNOWN"
if [[ -f /home/$1/var/$1.org/logs/transfer.log ]]; then
	$TLD="org"
elif [[ -f /home/$1/var/$1.com/logs/transfer.log ]]; then
	$TLD="com"
elif [[ -f /home/$1/var/$1.net/logs/transfer.log ]]; then
	$TLD="net"
fi

if [[ $TLD -ne "UNKNOWN" ]]; then
	awk '{ print $1}' /home/$1/var/$1.$TLD/logs/transfer.log | sort  | uniq -c  | sort -nr | grep -v "^[[:space:]]*[[:digit:]][[:space:]]"
else
	echo "Could not find log"
fi