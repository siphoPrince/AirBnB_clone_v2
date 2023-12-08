#!/usr/bin/python3
from fabric.api import *
from os.path import exists
from datetime import datetime
from fabric.api import local

env.hosts = ['54.84.61.41', '54.197.43.33']


def do_clean(number=0):
    '''
    Clean extra arhive files servers
    '''
    files = local('ls -tr versions', capture=True)
    number_of_files = int(number)
    if number_of_files == 0:
        number_of_files = 1
    files = files.split('\n')
    file_length = len(files)
    for num in range(0, file_length - number_of_files):
        local('rm -rf versions/{}'.format(files[num]))
    files = run('ls -tr /data/web_static/releases')
    files = files.split('\n')
    file_length = len(files)
    for num in range(0, file_length - number_of_files):
        run('rm -rf /data/web_static/releases/{}'.format(files[num]))
