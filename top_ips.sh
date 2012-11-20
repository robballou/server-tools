#!/bin/bash

awk '{ print $1}' /home/$1/var/$1.org/logs/transfer.log | sort  | uniq -c  | sort -nr | grep -v "^[[:space:]]*[[:digit:]][[:space:]]"