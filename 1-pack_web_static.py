#!/usr/bin/python3
"""Python module for packing web_static
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Function to pack web_static into .tgz folder
    """
    now_string = datetime.now().strftime('%Y%M%d%H%M%S')

    archive_name = "web_static_{}.tgz".format(now_string)
    
    local('tar -czvf {} ./web_static'.format(archive_name))

    local('mv ./{} ./versions/{} -p'.format(archive_name, archive_name))