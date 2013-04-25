#!/usr/bin/env python
from fabric.api import task, run, local
import datetime

@task
def databases(user='root'):
    """Show a list of databases"""
    run('echo "show databases;" | mysql -u %s -p' % user)

@task
def dump(db, user='root'):
    """Backup database"""
    filename = "%s%s.sql" % (db, datetime.datetime.now().strftime("%Y%m%d%H%M"))
    run('mysqldump -u %(user)s -p %(db)s > %(filename)s' % {'user': user, 'db': db, 'filename': filename})

@task
def local_dump(db, user='root', password=True):
    """Backup local database"""
    filename = "%s%s.sql" % (db, datetime.datetime.now().strftime("%Y%m%d%H%M"))
    cmd = "mysqldump -u %s " % user
    if password == True:
        cmd = "%s-p " % cmd
    cmd = "%s%s > %s" % (cmd, db, filename)
    local(cmd)

@task
def local_tables(database, user='root', password=True):
    """Show a list of databases"""
    cmd = "mysql -u %s " % user
    if password == True:
        cmd = "%s-p " % cmd
    local('echo "show tables;" | %s %s' % (cmd, database))
