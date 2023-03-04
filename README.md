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

![Pinout](./pinout.svg)

## Installation
 1. Flash *Raspbian Desktop* to the SD card via *Raspberry Pi Imager*
 2. **IMPORTANT:** Set it up with the following credentials and settings:
	 - Username: *nak-watchdog*
	 - Password: *VAULT*
	 - Turn on *Auto Login*
	 - Hostname: *nak-streamLink-n* (Replace *n* with the corresponding number from the deployment sheet)
3. Clone this repository into ```/home/nak-watchdog/``` via  
	```bash
	git clone https://github.com/fehart20/NAK_streamLink.git
	```
4. Run the installation script via  
	```bash
	./NAK_streamLink/streamLink/scripts/install.sh
	```
5. You need to enable the Serial-Function for the button LED to work: (Settings?)
	```bash
	sudo echo 'enable_uart=1' >> /boot/config.txt 
	```

---
## Configuration
To configure the YouTube-Livestream Link (or better: a dynamically changed shortlink) use the config-script as follows:
```bash
./NAK_streamLink/streamLink/scripts/config.sh
```
There are some predefined Links but you can also provide your own link by selecting 'Others'.  
The script generates an entry inside ```./NAK_streamLink/streamLink/config.ini```.

---
## Updating
To Update *streamLink* simply run the following command in ```~```:  
```bash
./NAK_streamLink/streamLink/scripts/update.sh
```
This will pull all the changes from this repository. **Please be aware that all localy made changes will be lost.**

---
## Licenses
TODO
