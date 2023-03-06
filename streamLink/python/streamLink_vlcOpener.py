#!/usr/bin/env python
# coding: utf-8
#import youtube_dl #used for youtube-connection
import yt_dlp
import vlc #used for playback
import tkinter as tk #used for message-popup
import time
import sys
import os #used for cec
import configparser

os.environ["DISPLAY"] = ":0"

### Get Config Parameters from config.ini
config = configparser.ConfigParser()
config.read("/home/nak-watchdog/NAK_streamLink/streamLink/config.ini")
youtubeLink = config.get("youtube", "link")
location = config.get("youtube", "location")

### Options for Youtube-DL Lib ###
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'quiet': False,
    'no_warnings': True,
}

### Function for Fullscreen Popup messages ###
def show_message_in_gui(message, duration):
    root = tk.Tk()
    root.attributes('-fullscreen',True)
    root.title("streamLink - Message")
    root.geometry("600x400")

    label = tk.Label(root, text=message, font=("Arial", 72), justify='center')
    label.pack(side='top', fill='both', expand=True)
    label.bind("<1>", quit) # When messagebox is clicked the script will exit
    
    root.after(duration * 1000, root.destroy)
    root.mainloop()

def quit(event):
    sys.exit()

#Turn on the TV if it's off
if os.system("echo 'pow 0' | cec-client -s -d 1") == "power status: standby":
    print("TV is in standby - turning it on ...") #DEBUG
    os.system("echo 'on 0' | cec-client -s -d 1")
    time.sleep(15) #wait till tv is on
os.system("echo 'as' | cec-client -s -d 1") #Always change raspi to active source


while True:
    try: #Try to catch Youtube URL and start own instance of VLC - no success: Popup-Message and reload after 30 seconds
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtubeLink, download=False)
            video = info['url']

            print(f'Playing video: {info["title"]}')
            # Play the video using python-vlc
            instance = vlc.Instance("prefer-insecure") # Prefer-Insecure 'cause of certificate errors
            player = instance.media_player_new()
            player.set_fullscreen(True)
            media = instance.media_new(video)
            media.get_mrl()
            player.set_media(media)
            player.play()
            player.audio_set_volume(100)
                      
            while player.get_state() !=vlc.State.Ended: # Check every 15s if stream is still playing
                time.sleep(15)
                pass

            player.stop() # Stopping the VLC instance when stream is over
            show_message_in_gui("Gottesdienst beendet ...\n\nGerät schaltet sich automatisch aus", 15)
            os.system("echo 'standby 0' | cec-client -s -d 1") #Turn off TV
            os.system("/home/nak-watchdog/NAK_streamLink/streamLink/script/update.sh")
            os.system("shutdown -h now")
            break # End of script
    except:
        show_message_in_gui(f"Gottesdienst aus {location}\nhat noch nicht begonnen ...\n\nBitte warten!", 30)
