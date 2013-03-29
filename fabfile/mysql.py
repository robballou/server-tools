#!/usr/bin/env python
from fabric.api import task, run
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
