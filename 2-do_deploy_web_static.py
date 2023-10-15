#!/usr/bin/python3
"""Deploying archive to web_servers
"""
import os
from datetime import datetime
from fabric.api import *


env.hosts = ['54.84.245.176', '52.87.244.137']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """Deploying an archive to the web server
    """
    if not os.path.exists(archive_path):
        print('path does not exist')
        return False
    else:
        try:
            # Get archive name
            archive_name = archive_path.split('/')[-1]

            # Get archive name without extensions
            archive_name_without_extension = archive_name.split('.')[0]

            # Construct archive location
            remote_archive_location = "/tmp/{}".format(archive_name)

            # Upload the archive to tmp
            put(archive_path, remote_archive_location)

            # Web static location
            web_static_location = "/data/web_static/releases/{}".format(
                archive_name_without_extension)

            # Decompress/Uncompress the archive inside the tmp directory
            run('tar -xzvf {} -C {}/'.format(remote_archive_location, web_static_location))

            # Delete the archive
            run('rm -f {}'.format(remote_archive_location))

            # Delete the current symbolic link
            run("rm -f /data/web_static/current")

            # Create a new current symbolic link pointing to the web static location
            run("ln -sf {} /data/web_static/current".format(web_static_location))

            # Return true if all goes well
            return True
        except Exception as e:
            print(e)
            return False
