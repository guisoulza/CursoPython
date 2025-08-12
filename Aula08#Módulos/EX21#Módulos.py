#Módulos.

import pygame

pygame.init()
pygame.mixer.music.load('C:\Windows\Media\Alarm06.wav')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

"""
from playsound3 import playsound
playsound("C:\Windows\Media\Alarm06.wav")
"""