#!/usr/bin/env bash
#This creates the necessary folders in webservers to serve webpages.
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "AirBnB Webpage file format correctly Implemented" > /data/web_static/releases/test/index.html
rm -df /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
service nginx restart
