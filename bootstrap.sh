#!/bin/bash

sudo apt-get update

sudo apt-get install -y python-pip python-numpy python-matplotlib \
    python-scipy python-gdal python-shapely curl ipython

sudo pip install geojson

# automatically changes the dir to /vagrant on ssh
if ! grep -q "cd /vagrant" ~/.bashrc ; then
    echo "cd /vagrant" >> ~/.bashrc
fi