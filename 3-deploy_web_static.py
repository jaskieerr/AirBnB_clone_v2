#!/usr/bin/python3
'''all in one'''

from datetime import datetime
from fabric.api import *
from os.path import exists


env.hosts = ["54.146.90.168", "100.25.138.247"]
env.user = "ubuntu"


def do_pack():
    '''  setting up your web servers for the deployment of web_static'''
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(path), capture=True)
    if result.failed:
        return None
    return path


def do_deploy(archive_path):
    '''  generates a .tgz archive from the contents of the web_static'''
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False


def deploy():
    '''All in one'''
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)

