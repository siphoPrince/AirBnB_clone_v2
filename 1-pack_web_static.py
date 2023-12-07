#!/usr/bin/python3
"""
Fabric script to generate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local, task


@task
def do_pack():
    """
    Making an archive in the web_static folder
    """
    time = datetime.now()
    archive = f"web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/{archive} web_static")
    return archive if result.succeeded else None
