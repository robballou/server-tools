#!/usr/bin/env python

from fabric.api import task, run, sudo, put
import os

@task
def apache_configtest():
    sudo('/sbin/service httpd configtest', shell=False)

@task
def apache_modules():
    run('/usr/sbin/apachectl -t -D DUMP_MODULES')

@task
def apt_check_updates():
    sudo('apt-get update')
    sudo('apt-get upgrade -n')

@task
def check_updates():
    sudo('if [ -e /usr/bin/yum ]; then /usr/bin/yum check-update; fi')
    sudo('if [ -e /usr/bin/apt-get ]; then /usr/bin/apt-get update 2&>1 /dev/null; /usr/bin/apt-get upgrade -s; fi')

@task
def disk_usage():
    run('df -h')

@task
def groups():
    run('groups')

@task
def iptables_list():
    sudo("/sbin/iptables --list --line-numbers")

@task
def last():
    run('last -a')

@task
def ls(directory = None):
    "Run ls on a directory"
    if not directory:
        directory = "."
    run("ls -Hal %s" % directory)

@task(alias='free')
def memory():
    """Show memory information"""
    run('free -m')

@task
def os_version():
    run('if [ -f /etc/issue ]; then cat /etc/issue; fi')
    run('if [ -f /etc/release ]; then cat /etc/release; fi')

@task
def passwd(user):
    sudo('passwd %s' % user)

@task
def php_version():
    run('php --version')

@task(alias='ps')
def processes(search=None):
    """List or search processes"""
    if not search:
        sudo('ps -ef')
    else:
        sudo('ps -ef | grep %s' % search)

@task(alias="puppet_install")
def puppet_module_install(module):
    """Install a puppet module"""
    sudo('puppet module install %s' % module)

@task
def puppet_modules():
    """List modules"""
    sudo('puppet module list')

@task
def restart_puppet():
    sudo('/sbin/service puppet restart', shell=False)

@task
def pwd():
    """Print the current working directory for the connection"""
    run('pwd')

@task
def restart_apache():
    """Restart apache"""
    sudo('/sbin/service httpd restart', shell=False)

@task
def restart_mysql():
    """Restart mysql"""
    sudo('/sbin/service mysql restart', shell=False)

@task
def sls(directory = None):
    "Same as ls, but using sudo"
    if not directory:
        directory = "."
    sudo("ls -Hal %s" % directory)

@task
def ssh_fingerprint():
    run('ssh-keygen -lf /etc/ssh/ssh_host_rsa_key.pub')

@task
def ssh_setup(keyfile=None):
    run('if [ ! -d .ssh ]; then mkdir .ssh && chown `whoami` .ssh && chmod 700 .ssh; fi')
    if keyfile and os.path.exists(keyfile):
        put(keyfile, '.ssh/')
        filename = os.path.split(keyfile)
        if filename[1] != 'authorized_keys':
            run('if [ -f .ssh/authorized_keys ]; then mv .ssh/authorized_keys .ssh/authorized_keys.old; fi')
            run('mv ".ssh/%s" .ssh/authorized_keys' % filename[1])
    else:
        print "Keyfile does not exist: %s" % keyfile
    run('chmod 700 .ssh')
    run('chmod 600 .ssh/authorized_keys')

@task
def tail_puppet_log(n=None):
    if not n:
        sudo('tail -f /var/log/puppet/puppet.log')
    else:
        sudo('tail -n %s /var/log/puppet/puppet.log' % n)

@task
def uptime():
    """Run uptime"""
    run('uptime')

@task
def user_add(username, groups=None):
    """Add a new user to the system"""
    if not groups:
        sudo('/usr/sbin/useradd -m %s' % username)
    else:
        sudo('/usr/sbin/useradd -m -G %s %s' % (groups, username))

@task
def yum_check_updates():
    sudo('yum check-update')

@task
def yum_install(package):
    sudo('yum install %s' % package)

@task
def yum_update(package = None):
    if package:
        sudo('yum update %s' % package)
    else:
        sudo('yum update')
