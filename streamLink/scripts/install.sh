#!/bin/bash
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
pip install RPi.GPIO

sudo chmod ugo+x ./start.sh

# Autostart
echo 'Adding Script to autostart ...'
mkdir ~/.config/autostart/
cp ./streamLink/start_streamLink.desktop ~/.config/autostart/

# Button functionality
echo 'Adding button config ...'
sudo echo '[all]' >> /boot/config.txt
sudo echo 'enable_uart=1' >> /boot/config.txt
 # Pi Power Button
git clone https://github.com/fehart20/pi-power-button.git
sh ./pi-power-button/script/install

sh ./start.sh
