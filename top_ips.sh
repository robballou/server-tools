#!/bin/bash

# check for command line argument
if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` [domain]"
    exit 1
fi

#
# Find apachectl command
#
find_apache_config() {
	apachectl=$(whereis apachectl)
	if [[ $apachectl ]]; then
		echo $apachectl
	fi

	apachectl=$(whereis apache2ctl)
	if [[ $apachectl ]]; then
		echo $apachectl
	fi
}

#
# Find the access log for the domain name
#
find_log_file() {
	domain=$1

	# find the apachectl command
	apachectl=$(find_apache_config)
	if [[ ! $apachectl ]]; then
		echo 'Error: could not find apachectl/apache2ctl'
		exit 1
	fi

	# find the vhost definition from the apachectl command
	# "apachectl -S" returns a list of the configured vhosts
	vhost=$((($apachectl -S) 2>&1) | grep $domain)

	# now parse out the vhost configuration file
	conf_file=$(echo $vhost | awk '{print $5}' | sed s/\(// | sed s/\)// | sed 's/:[[:digit:]]//')

	# grep the configuration file for the access log
	log=$(grep CustomLog $conf_file | awk '{print $2}' | sed 's/"//g')
	if [[ -f $log ]]; then
		echo $log
	fi
}


#
# Associate command line arguments with variable names
export DOMAIN=$1
export USERNAME=$1

if [[ -n "$2" ]]; then
	USERNAME=$2
fi

# get the domain log file
log_file=$(find_log_file $DOMAIN)
if [[ $log_file ]]; then
	awk '{ print $1}' $log_file | sort  | uniq -c  | sort -nr | grep -v "^[[:space:]]*[[:digit:]][[:space:]]"
fi
