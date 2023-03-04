#!/usr/bin/env python
# coding: utf-8
import youtube_dl #used for youtube-connection
import vlc #used for playback
import tkinter as tk #used for message-popup
import time
import sys
import os #used for cec
import configparser

os.environ["DISPLAY"] = ":0"

### Get Config Parameters from config.ini
config = configparser.ConfigParser()
config.read("../config.ini")
youtubeLink = config.get("youtube", "link")

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
    root.title("Message")
    root.geometry("600x400")

    label = tk.Label(root, text=message, font=("Arial", 72), justify='center')
    label.pack(side='top', fill='both', expand=True)
    label.bind("<1>", quit)
    
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


#youtubeLink = sys.argv[1] #Get Link from googleParser which started this script through subprocess
#youtubeLink = "http://nactube.datagis.com/c/NAKNuertingen"
#print(youtubeLink) #DEBUG


while True:
    try: #Try to catch Youtube URL and start own instance of VLC - no success: Popup-Message and reload after 30 seconds
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtubeLink, download=False)
            video = info['url']

            print(f'Playing video: {info["title"]}')
            # Play the video using your preferred media player, such as VLC
            # The following line is an example using the python-vlc library
            instance = vlc.Instance("prefer-insecure") #"--aout alsa"
            player = instance.media_player_new()
            player.set_fullscreen(True)
            media = instance.media_new(video)
            media.get_mrl()
            player.set_media(media)
            player.play()
            #player.toggle_fullscreen()
            player.audio_set_volume(100)
                      
            
            while player.get_state() !=vlc.State.Ended: #Check if stream is over
                time.sleep(1)
                pass

            player.stop() #Stoping the VLC instance when stream is over
            show_message_in_gui("Gottesdienst beendet ...\n\nGerät schaltet sich automatisch aus", 15)
            os.system("echo 'standby 0' | cec-client -s -d 1") #Turn off TV
            os.system("shutdown -h now")
            break #End of script
    except:
        show_message_in_gui("Gottesdienst hat noch nicht begonnen ...\n\nBitte warten!", 30)
