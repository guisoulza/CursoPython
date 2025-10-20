# Módulos(Modules).

# 21 - faça um programa que abra e reproduza o aúdio de um arquivo MP3.
# 21 - Create a program that opens and plays the audio of an MP3 file.

import pygame
# pygame é uma biblioteca Python para desenvolver jogos 2D e aplicações multimídia.
# pygame is a Python library for developing 2D games and multimedia applications.
pygame.init()
# init() inicializa todos os módulos do Pygame que precisam ser ativados antes de usar: som, vídeo, joystick,
# fontes etc.
# init() initializes all Pygame modules that need to be activated before use: sound, video, joystick, fonts, etc.
pygame.mixer.music.load('C:\Windows\Media\Alarm06.wav')
# mixer.music.load() carrega um arquivo de áudio para reprodução.
# mixer.music.load() loads an audio file for playback.
pygame.mixer.music.play()
# mixer.music.play() toca a música que você carregou com pygame.mixer.music.load().
# mixer.music.play() plays the music that you loaded with pygame.mixer.music.load().

while pygame.mixer.music.get_busy():
    pass
# mixer.music.get_busy() retorna True ou False. Indica se uma música está tocando no momento.
# mixer.music.get_busy() returns True or False. It indicates whether a music track is currently playing.


"""
from playsound3 import playsound                            
playsound("C:\Windows\Media\Alarm06.wav") 
"""
# O playsound3 é uma biblioteca Python para reprodução de arquivos de áudio, baseada na versão original criada por
# Taylor Marks. Ela oferece uma interface simples para tocar sons, com suporte a diversos formatos e sistemas
# operacionais.
# playsound3 is a Python library for playing audio files, based on the original version created by Taylor Marks.
# It provides a simple interface to play sounds, supporting multiple formats and operating systems.

# Reproduz um arquivo de áudio (.mp3, .wav, etc.) de forma simples.
# Plays an audio file (.mp3, .wav, etc.) in a simple way.
