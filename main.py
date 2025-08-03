#-*- coding: utf-8 -*-
import pygame
import sys
from funciones import *
from pygame import *
<<<<<<< HEAD
from constantes import *    
=======
from constantes import *
>>>>>>> 5cf1fd485d96c27f2757fc39e0a0cd439bc8ad44
from clases import *
import json
import csv
'''

'''
#VARIABLES GLOBALES
escena = "Menu"
pygame.init() #Inicialización de pygame
screen = pygame.display.set_mode((HEIGHT,WIDTH)) #Seteo del tamaño de la pantalla
pygame.display.set_caption("Preguntados!")#Seteo del nombre de la ventana.
<<<<<<< HEAD
imagen_fondo = pygame.image.load('mult/img/preguntados_background.jpg')
=======
imagen_fondo = pygame.image.load('proyecto_segundo_parcial/mult/img/preguntados_background.jpg')
>>>>>>> 5cf1fd485d96c27f2757fc39e0a0cd439bc8ad44
imagen_fondo = pygame.transform.scale(imagen_fondo, (HEIGHT,WIDTH))

#Seteo escenas
menu = MenuPrincipal(screen) 
inicio_juego = InicioJuego(screen)
perdiste = Perdiste(screen,0)
top10partidas = Top10Partidas(screen)
ganaste = Ganaste(screen,0)

try:
<<<<<<< HEAD
    with open('datos\partidas.json', 'r') as archivo:
=======
    with open('proyecto_segundo_parcial\datos\partidas.json', 'r') as archivo:
>>>>>>> 5cf1fd485d96c27f2757fc39e0a0cd439bc8ad44
        lista_jugadores = json.load(archivo)
except:
    # Si el archivo no existe, se crea una lista vacía
    lista_jugadores = []
top10partidas.lista_jugadores = lista_jugadores
'''
Inicio pygame
'''
while menu.corriendo:
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
            perdiste.puntaje = puntaje
            perdiste.escena = "Perdiste"
            perdiste.inicio_perdiste()
            escena = perdiste.escena
            
            if len(perdiste.datos_jugadores) == 1:
                for i in perdiste.datos_jugadores:
                    if i not in top10partidas.lista_jugadores:
                        top10partidas.lista_jugadores.append(perdiste.datos_jugadores[0])
            else:
                for i in perdiste.datos_jugadores:
                    if i not in top10partidas.lista_jugadores:
                        top10partidas.lista_jugadores.append(i)

                    

        case "Ganaste":
            ganaste.inicio_ganaste()
            escena = ganaste.escena
            ganaste.puntaje = puntaje

            if len(ganaste.datos_jugadores) == 1:
                for i in ganaste.datos_jugadores:
                    if i not in top10partidas.lista_jugadores:
                        top10partidas.lista_jugadores.append(ganaste.datos_jugadores[0])
            else:
                for i in ganaste.datos_jugadores:
                    if i not in top10partidas.lista_jugadores:
                        top10partidas.lista_jugadores.append(i)

        case "Config":
            pass
        case "Top10Partidas":
            top10partidas.escena = "Top10Partidas" 
            top10partidas.inicio_top10()
            escena = top10partidas.escena
    display.flip()
    pygame.display.update()

<<<<<<< HEAD
with open('datos\partidas.json', 'w') as archivo:
=======
with open('proyecto_segundo_parcial\datos\partidas.json', 'w') as archivo:
>>>>>>> 5cf1fd485d96c27f2757fc39e0a0cd439bc8ad44
        json.dump(top10partidas.lista_jugadores,archivo)
pygame.quit()
sys.exit()