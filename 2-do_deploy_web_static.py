#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
from fabric.api import *
import os.path

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Get the filename of the archive
    filename = os.path.basename(archive_path)
    # Get the name of the folder where the contents of the archive will be extracted
    foldername = filename.split('.')[0]

    # Create the folder where the contents of the archive will be extracted
    run("mkdir -p /data/web_static/releases/{}".format(foldername))

    # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, foldername))

    # Delete the archive from the web server
    run("rm /tmp/{}".format(filename))

    # Move the contents of the extracted folder up one level
    run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(foldername, foldername))

    # Remove the now-empty folder
    run("rm -rf /data/web_static/releases/{}/web_static".format(foldername))

    # Delete the symbolic link /data/web_static/current from the web server
    run("rm -rf /data/web_static/current")

    # Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(foldername))

    return True
