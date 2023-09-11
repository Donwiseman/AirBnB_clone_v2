#!/usr/bin/env bash
#This creates the necessary folders in webservers to serve webpages.
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "AirBnB Webpage file format correctly Implemented" > /data/web_static/releases/test/index.html
rm -df /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "/^\tserver_name _;/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
