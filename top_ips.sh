#!/bin/bash

# check for command line argument
if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` [domain]"
    exit 1
fi

export DOMAIN=$1
export USERNAME=$1

if [[ -n "$2" ]]; then
	USERNAME=$2
fi

export TLD="UNKNOWN"
if [[ -f /home/$USERNAME/var/$DOMAIN.org/logs/transfer.log ]]; then
	TLD="org"
elif [[ -f /home/$USERNAME/var/$DOMAIN.com/logs/transfer.log ]]; then
	TLD="com"
elif [[ -f /home/$USERNAME/var/$DOMAIN.net/logs/transfer.log ]]; then
	TLD="net"
fi

echo "/home/$USERNAME/var/$DOMAIN.$TLD/logs/transfer.log"

if [[ $TLD != "UNKNOWN" ]]; then
	awk '{ print $1}' /home/$USERNAME/var/$DOMAIN.$TLD/logs/transfer.log | sort  | uniq -c  | sort -nr | grep -v "^[[:space:]]*[[:digit:]][[:space:]]"
else
	echo "Could not find log"
fi