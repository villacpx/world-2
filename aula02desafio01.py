print('CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS')
from time import sleep
import pygame
pygame.mixer.init()
pygame.init()
for c in range(10, 0, -1):
    sleep(1)
    print(c)
pygame.mixer.music.load('som.wav')
print('FELIZ ANO NOVO')
pygame.mixer.music.play()
pygame.event.wait()
