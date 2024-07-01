import pygame
import sys
from funciones import *
from pygame import *
from constantes import *
from main import imagen_fondo
def menu_principal(screen):
    '''
    Escena de menu principal, crea dos botones.
    MISION: MOVER ESCENAS A UN ARCHIVO CON FUNCIONES PARA NO TENERLO ACÁ
    '''
    boton_inicio,text_rect,text_surface = crea_boton(300,370,200,70,"Inicio")
    boton_salida,text_rect_2,text_surface_2 = crea_boton(300,500,200,70,"Salida")
    sonido_inicio = pygame.mixer.Sound("proyecto_segundo_parcial/mult/img/sonido/inicio_efecto.mp3")
    sonido_inicio.set_volume(0.2)
    sonido_inicio.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == pygame.MOUSEBUTTONUP):
            if event.button == 1:
                mouse_pos = event.pos
                print(mouse_pos)
                if colision_boton(event,boton_inicio):
                        print("Toque Boton...")
                        escena = "Inicio"
                elif (mouse_pos[0]> boton_salida.left and mouse_pos[0]<boton_salida.right) and (mouse_pos[1]< boton_salida.bottom and mouse_pos[1]> boton_salida.top):
                    pygame.quit()
                    sys.exit()
                
    screen.blit(imagen_fondo,(0,0))
    draw.rect(screen,(116, 191, 64),boton_inicio,0,10,10)#Boton inicio
    draw.rect(screen,(248, 41, 51),boton_salida,0,10,10)#Boton salida (despues del 0 parametros para redondeo del boton)
    screen.blit(text_surface_2, text_rect_2)
    screen.blit(text_surface, text_rect)    


def inicio(screen):
    musica_fondo = pygame.mixer.Sound("proyecto_segundo_parcial\mult\img\sonido\musica_fondo.mp3")
    musica_fondo.set_volume(0.2)
    musica_fondo.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((253, 87, 34))
    text_rect,text_surface = crea_texto("De que color es ?")
    screen.blit(text_surface,text_rect)
    print("Estoy en inicio")