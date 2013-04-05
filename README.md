# Server Tools

This contains some various server tools that I have found useful on multiple
servers. Many of these need a bit of work to be applicable to ever server, but
they may prove useful for others.

## Fabric

I have added some [Fabric](http://fabfile.org) commands to this repo that I use
almost daily. They currently include some generic server, git and mysql commands.

To install this, I recommend adding it as a symlink in your site-packages directory:

    pushd `python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`
    sudo ln -s /path/to/server-tools/fabfile server_tools_fabfile
    popd

You will then be able to add these commands via an import in your own fabfile.

Available commands:

    git.a
    git.alias
    git.br
    git.branch
    git.checkout
    git.clean
    git.clean_pull
    git.co
    git.cpl
    git.current_branch
    git.d
    git.diff
    git.f
    git.fetch
    git.pl
    git.pull
    git.remote
    git.st
    git.status
    git.version
    mysql.databases           Show a list of databases
    mysql.dump                Backup database
    mysql.local_dump          Backup local database
    mysql.tables              Show a list of databases
    server.apache_configtest
    server.apt_check_updates
    server.check_updates
    server.free               Show memory information
    server.groups
    server.iptables_list
    server.last
    server.ls                 Run ls on a directory
    server.memory             Show memory information
    server.os_version
    server.passwd
    server.php_version
    server.processes          List or search processes
    server.ps                 List or search processes
    server.pwd                Print the current working directory for the connection
    server.restart_apache     Restart apache
    server.restart_mysql      Restart mysql
    server.sls                Same as ls, but using sudo
    server.ssh_fingerprint
    server.ssh_setup
    server.uptime             Run uptime
    server.user_add           Add a new user to the system
    server.yum_check_updates
    server.yum_install
    server.yum_update