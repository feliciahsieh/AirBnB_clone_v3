#!/usr/bin/python3
"""Deploy an archive of static html to my web servers with Fabric3"""

from fabric import api
import os


api.env.hosts = ['142.44.167.235', '144.217.246.199']
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/holberton'


def do_deploy(archive_path):
    """Function to transfer `archive_path` to web servers.

    Args:
        archive_path (str): path of the .tgz file to transfer

    Returns: True on success, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    with api.cd('/tmp'):
        basename = os.path.basename(archive_path)
        outpath = '/data/web_static/releases/{}'.format(basename)
        try:
            putpath = api.put(archive_path)
            api.run('mkdir -p {}'.format(outpath))
            api.run('tar -xzf {} -C {}'.format(putpath[0], outpath))
            api.run('rm {}'.format(putpath[0]))
            api.run('mv {}/web_static/* {}'.format(outpath, outpath))
            api.run('rm -rf {}/web_static'.format(outpath))
            api.run('rm -rf /data/web_static/current')
            api.run('ln -s {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except:
            return False
