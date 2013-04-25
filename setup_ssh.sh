#!/bin/bash

HOME_DIR=/home/$1
if [[ ! -e $HOME_DIR/.ssh ]]; then
        mkdir $HOME_DIR/.ssh
fi

if [[ ! -e $HOME_DIR/.ssh/authorized_keys ]]; then
        cp /root/authorized_keys $HOME_DIR/.ssh/authorized_keys
fi

chown -R $1:$1 $HOME_DIR/.ssh
chmod 700 $HOME_DIR/.ssh
chmod 600 $HOME_DIR/.ssh/authorized_keys