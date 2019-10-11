import os
import time
from random import randint
import vlc
	
SOUNDS_DIR = './sounds/'
SOUNDS_ALLOWED_FORMATS = ('.mp3', '.aif', '.wav')

class Player:
    playlist = []
    instance = vlc.Instance()
    player = instance.media_player_new()
   
    def __init__(self):
        self.playlist = [SOUNDS_DIR + file for file in os.listdir(SOUNDS_DIR) if
                         os.path.isfile(SOUNDS_DIR + file) and file.endswith(SOUNDS_ALLOWED_FORMATS)]
        self._set_max_volume()

    def play_random(self):
            media = self.instance.media_new(self._next_sound())
            self.player.set_media(media)
            self.player.play()
            time.sleep(0.5)
            duration = self.player.get_length()/1000
            time.sleep(duration)
    
    def _set_max_volume(self):
        os.system('amixer set Master 100%')

    def _next_sound(self):
        return self.playlist[randint(0, len(self.playlist) - 1)]
