#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""


from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

# Define the user and hosts
env.user = 'ubuntu'
env.hosts = ['54.84.61.41', '54.197.43.33']

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -czvf {} web_static".format(file_path))  # Use -czvf for consistency
        return file_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Deploys the archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        file_name = archive_path.split('/')[-1].split('.')[0]
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name + ".tgz", file_name))

        # Delete the archive from the server
        run("rm /tmp/{}".format(file_name + ".tgz"))

        # Move contents to the web_static folder
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(file_name, file_name))

        # Delete the unnecessary web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(file_name))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
