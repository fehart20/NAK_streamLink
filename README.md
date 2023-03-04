## Hardware
 - Raspberry Pi 4 (4GB)
 - SD card (min. 8GB)
 - Power Supply
 - Button with LED
 - (Colling-)Case for die Pi
 - Plastic Box with cable outlet to safely mount the Pi
 - Ethernet cable
 - Mini-HDMI to HDMI cable

### Cabling
From|To
---|---
Button/LED Gnd|GND (Port 6)
Button (+)|GPIO 3 (SCL)
LED (+)|GPIO 14 (TXD)


## Installation
 1. Flash *Raspbian Desktop* to the SD card via *Raspberry Pi Imager*
 2. Set it up with the following credentials and settings:
	 - Username: *nak-watchdog*
	 - Password: *VAULT*
	 - Hostname: *nak-streamLink-n* (Replace *n* with the corresponding number from the deployment sheet)
3. Clone this repository via 
	```git clone ```
4. Switch to 
   ```cd NAK_streamLink```
6. Run the installation script via 
	```./install.sh```
TODO


## Autostart durch Desktop
Datei unter ~/.config/autostart/start_streamLink.desktop
Folgende Ausführung:
	[Desktop Entry]
	Type=Application
	Name=streamLink
	Exec=/usr/bin/python3 /home/nak-watchdog/streamLink/streamLink_vlcOpener.py 

## Python-Script
Scripts liegen unter ~/streamLink
Google-Parser nicht in Verwendung - direkter (Short-)Link in Benutzung. (http://nactube.datagis.com/c/NAKNuertingen)
siehe Script


Einschalten: Lampe des Tasters ist am Seriellen Port verbunden. In /boot/config.txt ist folgendes 
konfiguriert (serieller Port GPIO14 (TXD) wird wird beim starten aktiviert und gibt Spannung aus):
[all]
enable_uart=1

Short von GPIO3 and Ground führt zum Aufwecken des PIs, wenn es sich im Hybernate-Zustand befindet.

Shutdown:
/etc/init.d/listen-for-shutdown.sh
/usr/local/bin/listen-for-shutdown.py
siehe auch: https://github.com/Howchoo/pi-power-button
