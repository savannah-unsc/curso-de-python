import pygame
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play(0)
while pygame.mixer.music.get_busy():
    pygame.event.wait()