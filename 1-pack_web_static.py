#!/usr/bin/python3
from datetime import datetime
from fabric.api import local

def do_pack():
    now_string = datetime.now().strftime('%Y%M%d%H%M%S')

    archive_name = "web_static_{}.tgz".format(now_string)
    
    local('tar -czvf {} ./web_static'.format(archive_name))

    local('mv ./{} ./versions/{} -p'.format(archive_name, archive_name))