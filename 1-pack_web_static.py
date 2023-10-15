#!/usr/bin/python3
"""Python module for packing web_static
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Function to pack web_static into .tgz folder
    """
    # Creating the datetime string
    now_string = datetime.now().strftime('%Y%m%d%H%M%S')

    # Generating the archive name
    archive_name = "web_static_{}.tgz".format(now_string)

    # Generating the archive using tar
    local('tar -czvf {} ./web_static'.format(archive_name))

    # Creating the versions directory if it doesn't already exist
    local('mkdir versions -p')

    # Moving the archive to the versions directory
    local('mv ./{} ./versions/{}'.format(archive_name, archive_name))
