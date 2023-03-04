#!/bin/bash
echo '
echo 'Installing Updates ...'
sudo apt update
sudo apt upgrade -y
sudo apt install python3 -y
sudo apt install vlc -y
sudo apt install cec-utils -y

pip install youtube_dl
pip install python-vlc
pip install tk
pip install keyboard

sudo chmod ugo+x ./start.sh

mkdir ~/.config/autostart/
cp ./streamLink/start_streamLink.desktop ~/.config/autostart/


sh ./start.sh
