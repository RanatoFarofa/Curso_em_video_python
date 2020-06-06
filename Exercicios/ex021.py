#faça um programa que abra e reproduza um arquvio MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/renat/Documents/CursoEmVideo/python/Exercicios/audio2.mp3')
pygame.mixer.music.play()
parar = input('Quando quiser parar digite qualquer coisa.....')