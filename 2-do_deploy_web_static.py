#!/usr/bin/python3
"""
Fabric script for deploying a web static archive to web servers.
"""

from fabric.api import put, run, env
from os.path import exists

# Update the IP addresses
env.hosts = ['54.84.61.41', '54.197.43.33']

def do_deploy(archive_path):
    """
    Distributes a web static archive to the web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    # Check if the archive exists
    if not exists(archive_path):
        return False
    
    try:
        # Extract necessary information from the archive path
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the server
        put(archive_path, '/tmp/')
        
        # Create the necessary directories and extract the archive
        run('mkdir -p {}{}/'.format(path, no_extension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))
        
        # Cleanup temporary files
        run('rm /tmp/{}'.format(file_name))
        
        # Move contents of the extracted folder
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))
        
        # Remove the empty web_static folder
        run('rm -rf {}{}/web_static'.format(path, no_extension))
        
        # Update the symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))
        
        return True
    except Exception as e:
        print(e)
        return False
