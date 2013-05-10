#!/usr/bin/env python

from fabric.api import task, run, env, execute
from fabric.context_managers import cd

@task(alias='a')
def alias():
    with cd(env.hosts_path):
        run('git config color.ui true')
        run('git config alias.st status')
        run('git config alias.ci commit')
        run('git config alias.co checkout')
        run('git config alias.pl pull')
        run('git config alias.ps push')
        run('git config alias.lg "log --pretty=oneline --abbrev-commit --graph"')

@task(alias='co')
def checkout(branch):
    with cd(env.hosts_path):
        run('git checkout %s' % branch)

@task
def checkout_clean(path="."):
    with cd(env.hosts_path):
        run('git checkout -- %s' % path)
    execute('git.status')

@task
def clean(test=True):
    with cd(env.hosts_path):
        if test == True:
            run('git clean -fdn .')
        else:
            run('git clean -fd .')

@task(alias='cpl')
def clean_pull():
    with cd(env.hosts_path):
        run('git checkout -- .')
        run('git pull')

@task
def current_branch():
    with cd(env.hosts_path):
        run('git rev-parse --symbolic-full-name --abbrev-ref HEAD')

@task(alias='br')
def branch():
    with cd(env.hosts_path):
        run('git branch')

@task(alias='d')
def diff():
    with(cd(env.hosts_path)):
        run('git diff')

@task(alias='f')
def fetch():
    with cd(env.hosts_path):
        run('git fetch')
    execute('git.status')

@task(alias='pl')
def pull():
    with cd(env.hosts_path):
        run('git pull')

@task
def remote():
    with cd(env.hosts_path):
        run('git remote -v')

@task(alias='st')
def status():
    with cd(env.hosts_path):
        run('git status -s')

@task
def version():
    run('git --version')
