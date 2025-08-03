import pygame
import sys
from pygame import *
from constantes import *
import json
import csv
import datetime
import random

<<<<<<< HEAD
ruta_preguntas = "D:\Archivos\Descargas\proyecto_segundo_parcial-main\datos\preguntas.csv"
=======
ruta_preguntas = "proyecto_segundo_parcial\datos\preguntas.csv"
>>>>>>> 5cf1fd485d96c27f2757fc39e0a0cd439bc8ad44

def crea_texto(texto:str,fuente_nombre="Calibri"):
    fuente = font.SysFont(fuente_nombre,40)#Seteo de fuente
    text_surface = fuente.render(texto, True, (255,255,255))#
    text_rect = text_surface.get_rect()
    return text_rect,text_surface        
        
def agrega_diccioarios_a_lista(lista_diccionarios: list, lista_a_agregar: list):
    for item in lista_a_agregar:
        lista_diccionarios.append(item)
    return lista_diccionarios

def crea_boton(izquierda:int,arriba:int,ancho:int,alto:int,texto:str,color=(255,255,255)):
    '''                     
    Retorna BOTON INICIO, RECT DEL TEXT, Y LA SUPERFICIE DEL TEXTO
    '''
<<<<<<< HEAD
    fuente = pygame.font.Font("mult/font/pixel_art_font.ttf", 30)
=======
    fuente = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 30)
>>>>>>> 5cf1fd485d96c27f2757fc39e0a0cd439bc8ad44
    boton_inicio = Rect(izquierda,arriba,ancho,alto)#Rect del BOTÓN
    text_surface = fuente.render(texto, True, color)#
    text_rect = text_surface.get_rect(center=(izquierda + ancho / 2, arriba + alto / 2))
    return boton_inicio,text_rect,text_surface


def colision_boton(evento,boton):
    '''
    Recibe EVENTO PYGAME Y BOTÓN A COLISIONAR CON MOUSE CORTA.
    Retorna TRUE si se presionó el botón
    '''
    mouse_pos = evento.pos
    print(mouse_pos)
    if(mouse_pos[0]> boton.left and mouse_pos[0]<boton.right) and (mouse_pos[1]< boton.bottom and mouse_pos[1]> boton.top):
        return True
# LISTA JUGADORES TOP 10
def puntaje_jugadores(lista_jugadores):
        for i in range(len(lista_jugadores)):
            for j in range(i + 1,len(lista_jugadores)):
                if lista_jugadores[i]['puntaje'] < lista_jugadores[j]['puntaje']:
                    aux = lista_jugadores[i]
                    lista_jugadores[i] = lista_jugadores[j]
                    lista_jugadores[j] = aux
        print(lista_jugadores)


#FUNCIONES EN REVISION
def iniciar_juego(datos):
    '''
    No usar, en revision
    '''
    contador_fallas = 0
    puntaje = 0
    datos_jugadores = []

    for i in range(len(datos)):

        datos_jugador = {}

        if contador_fallas == 3: # si pierde 3 vidas se termina el juego 
            print('perdiste pete')  
            nombre = input('Ingresa tu nombre: ')   # pide nombre
            fecha_actual = datetime.datetime.now()  # pide fecha
            fecha_actual = str(fecha_actual)        # pasa fecha a str (para guardar en json)
            datos_jugador['nombre'] = nombre        # agrega valores al diccionario
            datos_jugador['puntaje'] = puntaje
            datos_jugador['fecha'] = fecha_actual          
            datos_jugadores.append(datos_jugador)   # agrega diccionario a lista 
            break

        print(datos[i]['pregunta'])             # printea preguntas y posibles respuestas
        print(datos[i]['respuesta_a'])
        print(datos[i]['respuesta_b'])
        print(datos[i]['respuesta_c'])

        respuesta = input('Ingrese respuesta: ') # opcion 


        while respuesta != datos[i]['respuesta_correcta']: # si responde mal

            contador_fallas += 1 # resta una vida

            if contador_fallas == 3: # al perder 3 vidas rompe
                break

            print('respuesta incorrecta')
            respuesta = input('Reingrese respuesta: ') # vuelve a preguntar 

            if respuesta == datos[i]['respuesta_correcta']: # si la respuesta es correcta suma punto
                puntaje += 1


def leer_csv(ruta_preguntas):
    '''
    No usar, en revision
    '''
    datos = []
    with open(ruta_preguntas, mode = 'r',encoding='utf-8') as arhivo:
        lectura = csv.DictReader(arhivo)

        for fila in lectura:
            datos.append(dict(fila))

    try:
        with open('jugadores.json', 'r',encoding='utf-8') as archivo:
            datos_jugadores = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, se crea una lista vacía
        datos_jugadores = []
    return datos


print(leer_csv(ruta_preguntas))