import vlc
import time

PLAYER_TIMEOUT_CHECK = 15


class VLCPlayer:

    def __init__(self, youtube_url: str):
        self.instance = vlc.Instance("prefer-insecure")
        self.player = self.instance.media_player_new()
        self.player.set_fullscreen(True)
        self.media = self.instance.media_new(youtube_url)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.play()
        self.player.audio_set_volume(100)

    def play_until_end(self):
        while self.player.get_state() != vlc.State.Ended:
            time.sleep(PLAYER_TIMEOUT_CHECK)
        self.player.stop()
