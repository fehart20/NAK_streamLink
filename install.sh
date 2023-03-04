#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3 -y
sudo apt install vlc -y
sudo apt install cec-utils -y

pip install youtube_dl
pip install python-vlc
pip install tk
pip install keyboard

sudo chmod ugo+x ./streamLink/start.sh
