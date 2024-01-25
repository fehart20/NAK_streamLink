<h1 align="center">

Welcome to NAK_streamLink 👋

</h1>
<p>
<img alt="Version" src="https://img.shields.io/badge/version-1.2-blue.svg?cacheSeconds=2592000" />
<a href="https://github.com/fehart20/NAK_streamLink" target="_blank"><img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" /></a>
<a href="https://github.com/fehart20/NAK_streamLink/graphs/commit-activity" target="_blank"><img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /></a>

</p>

> Python-App to view YouTube livestreams without the need of any user interaction other than a click of a button.
### 🏠 [Homepage](https://github.com/fehart20/NAK_streamLink)

---
## New Steps

cec:
```bash
sudo apt-get install libcec-dev build-essential python-dev
```

Install poetry:
```bash
pip install poetry --break-system-packages
python -m venv .venv
source .venv/bin/activate
poetry install
```

Setup:
```bash
python -m nakStreamLink.setup
```

Run:
```bash
python -m nakStreamLink.main
```
---

## Hardware
 - Raspberry Pi 4 (4GB)
 - SD card (min. 8GB)
 - Power Supply
 - Button with LED
 - (Colling-)Case for die Pi
 - Plastic Box with cable outlet to safely mount the Pi
 - Ethernet cable
 - Mini-HDMI to HDMI cable
 - TV with CEC enabled

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
5. You need to enable the Serial-Function for the button LED to work. Add the following entry into the end of ```/boot/config.txt```:
	```bash
	enable_uart=1
	```
6. If needed: Install some remote solution (e.g. AnyDesk)

## Configuration
To configure the YouTube-Livestream Link (or better: a dynamically changed shortlink) use the config-script as follows:
```bash
./NAK_streamLink/streamLink/scripts/config.sh
```
There are some predefined links and locations but you can also provide your own link and location by selecting 'Others'.  
The script generates an entry inside ```./NAK_streamLink/streamLink/config.ini```.

---
## Updating
To Update *streamLink* simply run the following command in ```~```:  
```bash
./NAK_streamLink/streamLink/scripts/update.sh
```
This will pull all the changes from this repository. **Please be aware that all localy made changes will be lost.**

## Author
👤 **FHCOM**
* Website: https://fhcom.de

* GitHub: [@fehart20](https://github.com/fehart20)


## 🤝 Contributing
Issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/fehart20/NAK_streamLink/issues).
## Show your support
Give a ⭐️ if this project helped you!
