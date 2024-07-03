#-*- coding: utf-8 -*-
import pygame
import sys
from funciones import *
from pygame import *
from constantes import *
from escenas import *
from clases import *
'''
Sugerencia: Cambio altura y ancho para que las preguntas entren? 
'''
#VARIABLES GLOBALES
escena = "Menu"
pygame.init() #Inicialización de pygame
screen = pygame.display.set_mode((HEIGHT,WIDTH)) #Seteo del tamaño de la pantalla
pygame.display.set_caption("Preguntados!")#Seteo del nombre de la ventana.
imagen_fondo = pygame.image.load('proyecto_segundo_parcial/mult/img/preguntados_background.jpg')
imagen_fondo = pygame.transform.scale(imagen_fondo, (HEIGHT,WIDTH))

menu = MenuPrincipal(screen)
inicio_juego = InicioJuego(screen)

'''
Inicio pygame
'''
while True:
    '''
    OJO, escenas perdiste y ganaste rompen el juego.
    Falta agregar sus escenas mediante una clase por cada una
    '''
    match escena:
        case "Menu":
            menu.inicio_menu()
            escena = menu.escena
        case "Inicio":
            inicio_juego.iniciar_juego()
            escena = inicio_juego.escena
        case "Perdiste":
            pass
        case "Ganaste":
            pass
    display.flip()
    pygame.display.update()
    