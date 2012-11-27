#!/bin/bash

# check for command line argument
if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` [domain]"
    exit 1
fi

tail -f /home/$1/var/$1.org/logs/transfer.log