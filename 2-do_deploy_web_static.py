#!/usr/bin/python3
# Deploy archive
"""Deploy archive"""
from fabric.api import task, local, put, run, env
from datetime import datetime
import os


env.hosts = ['100.25.161.163', '52.2.14.222']

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

@task
def do_deploy(archive_path):
    """ do deploy commamnd
        sudo fab -f 2-do_deploy_web_static.py deploy:
        archive_path=versions/web_static_20240111213956.tgz
        -i ~/.ssh/id_rsa -u ubuntu
    """
    try:
        if not os.path.exists(archive_path):
            return False
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        # Uncompress the archive to the deployment folder
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link to the deployment folder
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
