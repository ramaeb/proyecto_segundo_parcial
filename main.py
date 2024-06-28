import pygame
import sys
from pygame import *
from constantes import *
pygame.init() #Inicialización de pygame

screen = pygame.display.set_mode((HEIGHT,WIDTH)) #Seteo del tamaño de la pantalla
pygame.display.set_caption("Preguntados!")#Seteo del nombre de la ventana.
imagen_fondo = pygame.image.load('proyecto_segundo_parcial/img/preguntados_background.jpg')
imagen_fondo = pygame.transform.scale(imagen_fondo, (HEIGHT,WIDTH))
fuente = font.SysFont("Calibri",40)

boton_inicio = Rect(300,450,200,50)#Boton inicio
text_surface = fuente.render("Inicio", True, BLANCO)
text_rect = text_surface.get_rect(center=(300 + 200 / 2, 450 + 50 / 2))
 
while True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(imagen_fondo,(0,0))
    draw.rect(screen,(70,189,34),boton_inicio,0)#Boton inicio
    screen.blit(text_surface, text_rect)
   
    display.flip()
    pygame.display.update()
    