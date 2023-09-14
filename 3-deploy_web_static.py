#!/usr/bin/python3
""" This cript combines the do_pack and d0_deploy fabfile functions in order
    to deploy them to both serers. """

from fabric.api import *
pack = __import__('1-pack_web_static').do_pack
deploy = __import__('2-do_deploy_web_static').do_deploy

env.user = 'ubuntu'
env.hosts = ['100.26.49.0', '18.207.236.171']


def deploy():
    """Deploys the created archive to the webservers using already established
       functions in task 1 and 2 earlier."""
    pathname = pack()
    if not pathname:
        return False
    return deploy(pathname)
