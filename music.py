import pygame
class Music():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('music/1.mp3')
        pygame.mixer.music.set_volume(50)

    def update(self):
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()