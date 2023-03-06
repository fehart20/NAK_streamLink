#!/bin/bash

echo -e '=> Installing Updates ...\n'
sudo apt update
sudo apt upgrade -y
echo -e '=> Installing needed packages ...\n'
sudo apt install python3 -y
sudo apt install vlc -y
sudo apt install cec-utils -y

# Install Python Package
echo -e '=> Installing Python Packages ...\n'
#pip install youtube_dl
pip install yt_dlp
pip install python-vlc
pip install tk
pip install RPi.GPIO
pip install ConfigParser

# Autostart
echo -e '=> Adding script to autostart ...\n'
mkdir ~/.config/autostart/
cp ./NAK_streamLink/streamLink/start_streamLink.desktop ~/.config/autostart/start_streamLink.desktop

# Button functionality
echo -e '=> Adding button config ...\n'
sudo touch /boot/config.txt

sudo echo 'enable_uart=1' >> /boot/config.txt
 # Pi Power Button
cd ~
git clone https://github.com/fehart20/pi-power-button.git
sh ./pi-power-button/script/install # Why is this starting?

# Config script
echo -e "=> You can now run the config script to select a stream location via \n ./NAK_streamLink/streamLink/scripts/config.sh"