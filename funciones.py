import pygame
import sys
from pygame import *
from constantes import *


def crea_boton(izquierda,arriba,ancho,alto,texto,fuente_nombre="Calibri",color=(255,255,255)):
    '''
    Retorna BOTON INICIO, RECT DEL TEXT, Y LA SUPERFICIE DEL TEXTO
    '''
    fuente = font.SysFont(fuente_nombre,40)#Seteo de fuente
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