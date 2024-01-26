#!/usr/bin/env python3

"Testing the idea of providing an off-the-shelf Tk event loop for asyncio"

import asyncio
import random
from tkinter import Tk, Button


class AsyncTk(Tk):
    "Basic Tk with an asyncio-compatible event loop"

    def __init__(self):
        super().__init__()
        self.running = True
        self.runners = [self.tk_loop()]

    async def tk_loop(self):
        "asyncio 'compatible' tk event loop?"
        # Is there a better way to trigger loop exit than using a state vrbl?
        while self.running:
            self.update()
            # obviously, sleep time could be parameterized
            await asyncio.sleep(0.05)

    def stop(self):
        self.running = False

    async def run(self):
        url = await asyncio.gather(*self.runners)
        return url


class App(AsyncTk):
    "User's app"

    def __init__(self):
        super().__init__()
        self.create_interface()
        self.runners.append(self.counter())

    def create_interface(self):
        b1 = Button(master=self, text='Random Float',
                    command=lambda: print("your wish, as they say...", random.random()))
        b1.pack()
        b2 = Button(master=self, text='Quit', command=self.stop)
        b2.pack()

    async def counter(self):
        "sample async worker... (with apologies to Lawrence Welk)"
        i = 1
        while self.running:
            print("yt_dlp checking for livestream", i)
            if i >= 5:
                self.running = False
                return "youtube.com/cdn/fileill"
            await asyncio.sleep(1)
            i += 1


async def main():
    app = App()
    tet = await app.run()
    print(tet[1])

if __name__ == '__main__':
    asyncio.run(main())
