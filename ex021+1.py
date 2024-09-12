#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#USAR O MODULO PYGAME
import pygame
#.init para iniciar o modulo
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()