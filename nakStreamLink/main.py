import logging
import cec
import os
import asyncio

from nakStreamLink.read_config import StreamConfig
from nakStreamLink.video_player import VLCPlayer
import nakStreamLink.interface as gui

# Setup
os.environ["DISPLAY"] = ":0"
CONFIG_FILE = "config.ini"
# Configure logging
logging.basicConfig(filename='streamlink.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
### Options for Youtube-DL Lib ###
yt_dlp_options = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'quiet': False,
    'no_warnings': True,
}

logging.info("--- NAK StreamLink ---")

logging.info("CONFIG - Reading config")
stream_config = StreamConfig(CONFIG_FILE)

logging.info("CEC - Initialising")
cec.init()
tv = cec.Device(cec.CECDEVICE_TV)

try:
    if not tv.is_on():
        logging.info("CEC - Powering on tv")
        tv.power_on()
        logging.info("CEC - Set active source")
        cec.set_active_source()
except OSError:
    logging.critical("CEC - No CEC-Device found")

logging.info("INTERFACE - Starting GUI and Livestream-Check")
youtube_url = asyncio.run(
    gui.main(stream_config.stream_link, stream_config.stream_location))
logging.info("STREAM - Found Livestream-URL")

logging.info("VLC - Starting player")
player = VLCPlayer(youtube_url)
player.play_until_end()
logging.info("VLC - Player stopped")

tv.standby()
os.system("shutdown -h now")
