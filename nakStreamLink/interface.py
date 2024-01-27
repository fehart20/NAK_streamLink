import asyncio
import yt_dlp
from yt_dlp import DownloadError
import os
from ttkbootstrap import Button, Label, Window, Frame
from ttkbootstrap.constants import *

os.environ["DISPLAY"] = ":0"
SLEEP_TIMEOUT = 30


class AsyncTk(Window):
    "Basic Tk with an asyncio-compatible event loop"

    def __init__(self):
        super().__init__()
        self.running = True
        self.attributes('-fullscreen', True)
        self.title = "NAK StreamLink - Message"

        self.runners = [self.tk_loop()]

    async def tk_loop(self):
        while self.running:
            self.update()
            await asyncio.sleep(0.05)

    def stop(self):
        self.running = False

    async def run(self):
        url = await asyncio.gather(*self.runners)
        return url


class App(AsyncTk):

    def __init__(self, stream_url: str, stream_location: str):
        super().__init__()
        self.create_interface(stream_location)
        self.runners.append(self.wait_for_livestream(stream_url))

    def create_interface(self, stream_location: str):

        frame = Frame(self, style="TFrame")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label = Label(
            frame,
            text=
            f"Gottesdienst-Livestream aus {stream_location} hat noch nicht begonnen.\nBitte warten ...",
            font=("Helvetica", 40),
            style="TLabel")
        label.pack()

        button = Button(frame,
                        text="Beenden",
                        command=self.destroy,
                        bootstyle="light-outline")
        button.pack()

    async def wait_for_livestream(self, stream_link: str) -> str:
        "Waits for livestream to come online"
        while self.running:
            try:
                with yt_dlp.YoutubeDL() as ytdl:
                    meta = ytdl.extract_info(stream_link, download=False)
                    self.running = False
                    return meta['url']
            except DownloadError:
                await asyncio.sleep(SLEEP_TIMEOUT)
                continue


async def main(stream_link: str, stream_location: str):
    app = App(stream_link, stream_location)
    youtube_url = await app.run()
    return (youtube_url[1])
