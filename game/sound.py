# sound.py
import os
import pygame

class GameSound:
    """Class to handle sound effects with pygame."""
    def __init__(self, base_path):
        pygame.mixer.init()
        sound_path = os.path.join(base_path, "..", "sounds")
        self.win_sound = pygame.mixer.Sound(os.path.join(sound_path, "win.wav"))
        self.lose_sound = pygame.mixer.Sound(os.path.join(sound_path, "lose.wav"))
        self.draw_sound = pygame.mixer.Sound(os.path.join(sound_path, "draw.wav"))

    def play_win_sound(self):
        self.win_sound.play()

    def play_lose_sound(self):
        self.lose_sound.play()

    def play_draw_sound(self):
        self.draw_sound.play()
