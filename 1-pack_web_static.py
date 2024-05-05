#!/usr/bin/python3
''' generates a .tgz archive from the contents of the web_static'''

from fabric.api import local
from datetime import datetime


def do_pack():
    '''packing'''

    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time)
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path
