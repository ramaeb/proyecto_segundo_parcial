import pygame
import sys
from funciones import *
from pygame import *
from constantes import *

#VARIABLES GLOBALES
escena = "Menu"
andando = True

def menu_principal():
    '''
    Escena de menu principal, crea dos botones.
    MISION: MOVER ESCENAS A UN ARCHIVO CON FUNCIONES PARA NO TENERLO ACÁ
    '''
    global andando
    global escena
    boton_inicio,text_rect,text_surface = crea_boton(200,500,100,200,"hola")
    boton_inicio_2,text_rect_2,text_surface_2 = crea_boton(150,300,100,200,"Inicio2")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pos = event.pos
                print(mouse_pos)
                if(mouse_pos[0]> boton_inicio.left and mouse_pos[0]<boton_inicio.right) and (mouse_pos[1]< boton_inicio.bottom and mouse_pos[1]> boton_inicio.top):
                    print("Toque Boton...")
                    escena = "Inicio"
                colision_boton(event,boton_inicio)

    screen.blit(imagen_fondo,(0,0))
    draw.rect(screen,VERDE,boton_inicio,0)#Boton inicio
    draw.rect(screen,AZUL,boton_inicio_2,0)#Boton 2
    screen.blit(text_surface_2, text_rect_2)
    screen.blit(text_surface, text_rect)   


pygame.init() #Inicialización de pygame
screen = pygame.display.set_mode((HEIGHT,WIDTH)) #Seteo del tamaño de la pantalla
pygame.display.set_caption("Preguntados!")#Seteo del nombre de la ventana.
imagen_fondo = pygame.image.load('proyecto_segundo_parcial/img/preguntados_background.jpg')
imagen_fondo = pygame.transform.scale(imagen_fondo, (HEIGHT,WIDTH))


while True:
    match escena:
        case "Menu":
            menu_principal()
        case "Inicio":
            print("HOLA")

    display.flip()
    pygame.display.update()
    