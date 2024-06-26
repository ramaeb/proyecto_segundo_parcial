import pygame
import sys

pygame.init() #Inicialización de pygame
screen = pygame.display.set_mode((800,600)) #Seteo del tamaño de la pantalla
pygame.display.set_caption("HOLA")#Seteo del nombre de la ventana.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #HOLAasasas
    pass