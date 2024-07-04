#-*- coding: utf-8 -*-
import pygame
import sys
from funciones import *
from pygame import *
from constantes import *
from escenas import *
from clases import *
'''

'''
#VARIABLES GLOBALES
escena = "Menu"
pygame.init() #Inicialización de pygame
screen = pygame.display.set_mode((HEIGHT,WIDTH)) #Seteo del tamaño de la pantalla
pygame.display.set_caption("Preguntados!")#Seteo del nombre de la ventana.
imagen_fondo = pygame.image.load('proyecto_segundo_parcial/mult/img/preguntados_background.jpg')
imagen_fondo = pygame.transform.scale(imagen_fondo, (HEIGHT,WIDTH))

#Seteo escenas
menu = MenuPrincipal(screen) 
inicio_juego = InicioJuego(screen)
'''
Inicio pygame
'''
while True:
    '''
    Falta escena ganador y nombre
    '''
    match escena:
        case "Menu":
            inicio_juego = InicioJuego(screen)
            menu.escena = "Menu"
            menu.inicio_menu()
            escena = menu.escena
        case "Inicio":
            menu.escena = "Inicio"
            inicio_juego.iniciar_juego()
            escena = inicio_juego.escena
            puntaje = inicio_juego.puntaje
        case "Perdiste":
            perdiste = Perdiste(screen,puntaje)
            perdiste.escena = "Perdiste"
            perdiste.inicio_perdiste()
            escena = perdiste.escena
        case "Ganaste":
            pass
        case "Config":
            pass
    display.flip()
    pygame.display.update()
    