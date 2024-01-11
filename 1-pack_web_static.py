#!/usr/bin/python3
""" Compress before sending """
from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """ do pack commamnd
        sudo fab -f 1-pack_web_static.py do_pack
    """
    date_formatted = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    dirpath = "versions/web_static_{}.tgz".format(date_formatted)
    print("Packing web_static to {}".format(dirpath))
    if local("{} && tar -cvzf {} web_static".format(mkdir, dirpath)).succeeded:
        return dirpath
    return None
