#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.84.61.41', '54.197.43.33']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    # Check if the archive exists
    if not exists(archive_path):
        return False
    
    try:
        # Extract necessary information from the archive path
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')

        # Create the release directory
        run('mkdir -p {}{}/'.format(path, no_extension))

        # Extract the contents of the archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(file_name))

        # Move the contents to the release directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))

        # Remove the web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_extension))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))

        return True
    except Exception as e:
        print(e)
        return False
