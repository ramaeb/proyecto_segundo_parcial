#-*- coding: utf-8 -*-
import pygame
from funciones import *


class MenuPrincipal():

    '''
    Escena de menu principal
    '''
    def __init__(self, screen):
        self.screen = screen
        self.escena = "Menu"
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial/mult/img/preguntados_background.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (800, 600))
        self.boton_inicio, self.text_rect, self.text_surface = crea_boton(300, 370, 200, 70, "Inicio")
        self.boton_salida, self.text_rect_2, self.text_surface_2 = crea_boton(300, 500, 200, 70, "Salida")
        self.sonido_inicio = pygame.mixer.Sound("proyecto_segundo_parcial\mult\sonido\inicio_efecto.mp3")
        self.sonido_inicio.set_volume(0.2)
        self.sonido_inicio.play(loops=0)


    def render_menu(self):
        '''
        Hace el render de todos los botones SALIDA E INICIO
        '''
        
        self.screen.blit(self.imagen_fondo,(0,0))
        draw.rect(self.screen,(116, 191, 64),self.boton_inicio,0,10,10)#Boton inicio
        draw.rect(self.screen,(248, 41, 51),self.boton_salida,0,10,10)#Boton salida (despues del 0 parametros para redondeo del boton)
        self.screen.blit(self.text_surface_2, self.text_rect_2)
        self.screen.blit(self.text_surface, self.text_rect)


    def eventos_menu(self):
        '''
        Lee los eventos que van pasando por el menú
        La colision del mouse con los botones.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONUP):
                if event.button == 1:
                    mouse_pos = event.pos
                    print(mouse_pos)
                    if colision_boton(event,self.boton_inicio):
                            self.sonido_inicio.stop()
                            print("Toque Boton...")
                            pygame.mixer.music.load("proyecto_segundo_parcial\mult\sonido\musica_fondo.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(0.2)
                            self.escena = "Inicio"
                    elif (mouse_pos[0]> self.boton_salida.left and mouse_pos[0]<self.boton_salida.right) and (mouse_pos[1]< self.boton_salida.bottom and mouse_pos[1]> self.boton_salida.top):
                        pygame.quit()
                        sys.exit()


    def inicio_menu(self):
        '''
        Metodo para inicializar el menú.
        Utiliza las dos funciones, render y el lector de eventos.
        '''
        self.render_menu()
        self.eventos_menu()



class InicioJuego():

    def __init__(self,screen):
        self.screen = screen
        self.vidas = 3
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial/mult/img/preguntados_background.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (800, 600))
        self.fuente = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 14)
        self.lista_datos = leer_csv('proyecto_segundo_parcial\datos\preguntas.csv')
        self.indice = 0
        self.vidas = 3
        self.rect_1 = pygame.Rect(200,10,400,50)
        self.rect_2 = pygame.Rect(50,500,200,50)
        self.rect_3 = pygame.Rect(300,500.08,200,50)
        self.rect_4 = pygame.Rect(550,500.62,200,50)
        self.escena = "Inicio"


    def render_menu(self):
        if self.indice < len(self.lista_datos):
            self.dato = self.lista_datos[self.indice]

            self.screen.fill(NARANJA)
            pygame.draw.rect(self.screen,NEGRO,self.rect_1,border_radius=5)
            pygame.draw.rect(self.screen,NEGRO,self.rect_2,border_radius=5)
            pygame.draw.rect(self.screen,NEGRO,self.rect_3,border_radius=5)
            pygame.draw.rect(self.screen,NEGRO,self.rect_4,border_radius=5)

            pregunta = self.fuente.render(self.dato['pregunta'], True, ROJO)
            
            respuesta_a = self.fuente.render(self.dato['respuesta_a'], True, ROJO)
            respuesta_b = self.fuente.render(self.dato['respuesta_b'], True, ROJO)
            respuesta_c = self.fuente.render(self.dato['respuesta_c'], True, ROJO)
            
            texto_rect1 = pregunta.get_rect(center=(200 + 400 // 2, 10 + 50 // 2))
            texto_rect2 = respuesta_a.get_rect(center=(50 + 200 // 2, 500 + 50 // 2))
            texto_rect3 = respuesta_b.get_rect(center=(300 + 200 // 2, 500 + 50 // 2))
            texto_rect4 = respuesta_c.get_rect(center=(550 + 200 // 2, 500 + 50 // 2))

            self.screen.blit(pregunta,texto_rect1)
            self.screen.blit(respuesta_a,texto_rect2)
            self.screen.blit(respuesta_b,texto_rect3)
            self.screen.blit(respuesta_c,texto_rect4)
        else:
            self.escena = "Ganaste"

    def eventos_menu(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()  
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    respuesta = None  # Inicializar respuesta
                    if(colision_boton(evento,self.rect_2)):
                        respuesta = 'a'
                    elif(colision_boton(evento,self.rect_3)):
                        respuesta = 'b'
                    elif(colision_boton(evento,self.rect_4)):
                        respuesta = 'c'
                    print(respuesta)
                    if respuesta is not None:
                        if respuesta == self.dato['respuesta_correcta']:
                            self.indice += 1
                            print(f"Indice: {self.indice}")
                        else:
                            self.vidas -= 1
                            print(f"Vidas: {self.vidas}")
                            if self.vidas == 0:
                                self.escena = 'Perdiste'

    def iniciar_juego(self):
        '''
        Metodo para inicializar el menú.
        Utiliza las dos funciones, render y el lector de eventos.
        '''
        self.render_menu()
        self.eventos_menu()


class Perdiste():
    def __init__(self):
        pass

class Ganaste():
    def __init__(self):
        pass





class Boton(pygame.sprite.Sprite):
    '''
    Se lo trata como un sprite para que despues
    le podamos hacer un "KILL" y seguir con las funciones.
    '''
    def __init__(self,izquierda:int,arriba:int,ancho:int,alto:int,texto:str,screen,fuente_nombre="Calibri",color=(255,255,255)):
        self.izquierda = izquierda
        self.arriba = arriba
        self.ancho = ancho
        self.alto = alto
        self.texto = texto
        self.fuente_nombre = fuente_nombre
        self.color = color
        self.screen = screen

    def render_boton(self):
        fuente = font.SysFont(self.fuente_nombre,40)#Seteo de fuente
        self.boton_inicio = Rect(self.izquierda,self.arriba,self.ancho,self.alto)#Rect del BOTÓN
        self.text_surface = fuente.render(self.texto, True, color)#
        self.text_rect = self.text_surface.get_rect(center=(self.izquierda + self.ancho / 2, self.arriba + self.alto / 2))
        self.screen.blit(self.text_surface,self.text_rect)

