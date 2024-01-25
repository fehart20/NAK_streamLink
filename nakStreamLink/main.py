import logging
import cec
import yt_dlp
import vlc
import os
import time
from read_config import StreamConfig
from interface import show_message_in_gui

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

# if not tv.is_on():
#     logging.info("CEC - Powering on tv")
#     tv.power_on()
#     logging.info("CEC - Set active source")
#     cec.set_active_source()

while True:
    try:  #Try to catch Youtube URL and start own instance of VLC - no success: Popup-Message and reload after 30 seconds
        with yt_dlp.YoutubeDL(yt_dlp_options) as ydl:
            info = ydl.extract_info(stream_config.stream_link, download=False)
            video = info['url']

            print(f'Playing video: {info["title"]}')
            # Play the video using python-vlc
            instance = vlc.Instance(
                "prefer-insecure"
            )  # Prefer-Insecure 'cause of certificate errors
            player = instance.media_player_new()
            player.set_fullscreen(True)
            media = instance.media_new(video)
            media.get_mrl()
            player.set_media(media)
            player.play()
            player.audio_set_volume(100)

            while player.get_state(
            ) != vlc.State.Ended:  # Check every 15s if stream is still playing
                time.sleep(15)
                pass

            player.stop()  # Stopping the VLC instance when stream is over
            show_message_in_gui(
                "Gottesdienst beendet ...\n\nGerät schaltet sich automatisch aus",
                15)
            tv.standby()

            break  # End of script
    except:
        show_message_in_gui(
            f"Gottesdienst aus {stream_config.stream_location}\nhat noch nicht begonnen ...\n\nBitte warten!",
            30)
