# Faça um programa em Python que leia e reproduza um arquivo MP3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("./CursoEmVideo/Exercícios/mundo01/ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()