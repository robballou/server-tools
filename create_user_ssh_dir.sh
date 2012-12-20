#!/bin/bash

mkdir /home/$1/.ssh
touch /home/$1/.ssh/authorized_keys
chown -R $1:$1 /home/$1/.ssh
chmod 700 /home/$1/.ssh
chmod 600 /home/$1/.ssh/authorized_keys
