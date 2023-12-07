#!/usr/bin/python3
"""
writing a Fabric script to generate tgz archive
"""

from datetime import datetime
from fabric.api import local, task


@task
def do_pack():
    """
    creating an archive in the web_static folder
    """
    time = datetime.now()
    archive = f"web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz"
    
    # Create versions directory
    local("mkdir -p versions")
    
    # Create tgz archive
    result = local(f"tar -cvzf versions/{archive} web_static")
    
    return archive if result.succeeded else None
