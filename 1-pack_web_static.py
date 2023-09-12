#!/usr/bin/python3
""" This is a fabfile script that locally creats a gzip file containing static
    content of the hbnb web site.
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """ This creates a gzip archive of the webstatic folder. """
    time = datetime.utcnow()
    timestamp = time.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive = local('tar -czvf "versions/web_static_{}.tgz" web_static/'.
                    format(timestamp))
    if archive.succeeded:
        local('echo "web_static packed: versions/web_static_{0}.tgz \
-> $(stat -c %s versions/web_static_{0}.tgz)Bytes"'.format(timestamp))
