#Módulos.

#21 - faça um programa que abra e reproduza o aúdio de um arquivo MP3.

import pygame                                               #pygame é uma biblioteca Python para desenvolver jogos 2D e aplicações multimídia.

pygame.init()                                               #init() inicializa todos os módulos do Pygame que precisam ser ativados antes de usar: som, vídeo, joystick, fontes etc.
pygame.mixer.music.load('C:\Windows\Media\Alarm06.wav')     #mixer.music.load() carrega um arquivo de áudio para reprodução.
pygame.mixer.music.play()                                   #mixer.music.play() toca a música que você carregou com pygame.mixer.music.load().

while pygame.mixer.music.get_busy():                        #mixer.music.get_busy() retorna True ou False. Indica se uma música está tocando no momento.
    pass

"""
from playsound3 import playsound                            #O playsound3 é uma biblioteca Python para reprodução de arquivos de áudio, baseada na versão original criada por Taylor Marks. Ela oferece uma interface simples para tocar sons, com suporte a diversos formatos e sistemas operacionais.
playsound("C:\Windows\Media\Alarm06.wav")                   #Reproduz um arquivo de áudio (.mp3, .wav, etc.) de forma simples.
"""