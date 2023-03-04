#!/bin/bash

cd ./NAK_streamLink

echo -e "=> Updating streamLink via GitHub ... \n"
git reset --hard
git fetch --all
git pull --no-rebase

echo -e '=> Installing Updates ...\n'
sudo apt update
sudo apt upgrade -y

# Python Package
echo -e '=> Updating Python Packages ...\n'
pip install youtube_dl --upgrade
pip install python-vlc --upgrade
pip install tk --upgrade
pip install RPi.GPIO --upgrade
pip install ConfigParser --upgrade

# Autostart
echo -e '=> Adding script to autostart ...\n'
cp ./NAK_streamLink/streamLink/start_streamLink.desktop ~/.config/autostart/start_streamLink.desktop

# Run config script
echo -e "=> You can now run the config script again to select a stream location via \n ./NAK_streamLink/streamLink/scripts/config.sh"