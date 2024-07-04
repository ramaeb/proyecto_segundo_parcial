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
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial\mult\img\inicio_background.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (800, 600))
        self.fuente = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 14)
        self.fuente_vidas = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 30)
        self.color_variable_vida = VERDE
        self.lista_datos = leer_csv('proyecto_segundo_parcial\datos\preguntas.csv')
        self.indice = 0
        self.vidas = 3
        self.puntaje = 0
        self.rect_1 = pygame.Rect(150,10,500,50)
        self.rect_2 = pygame.Rect(50,500,200,50)
        self.rect_3 = pygame.Rect(300,500.08,200,50)
        self.rect_4 = pygame.Rect(550,500.62,200,50)
        self.rect_5 = pygame.Rect(10,100.62,200,50)
        self.escena = "Inicio"


    def render_menu(self):
        '''
        Muestra todo el inicio, sus botones y centra todo.
        '''
        self.screen.blit(self.imagen_fondo,(0,0))
        if self.indice < len(self.lista_datos):
            self.dato = self.lista_datos[self.indice]
            pygame.draw.rect(self.screen,GRIS,self.rect_1,border_radius=5)
            pygame.draw.rect(self.screen,GRIS,self.rect_2,border_radius=5)
            pygame.draw.rect(self.screen,GRIS,self.rect_3,border_radius=5)
            pygame.draw.rect(self.screen,GRIS,self.rect_4,border_radius=5)

            pregunta = self.fuente.render(self.dato['pregunta'], True, BLANCO)
            
            respuesta_a = self.fuente.render(self.dato['respuesta_a'], True, BLANCO)
            respuesta_b = self.fuente.render(self.dato['respuesta_b'], True, BLANCO)
            respuesta_c = self.fuente.render(self.dato['respuesta_c'], True, BLANCO)
            
            #muestreo de vidas restantes.
            vidas_texto = self.fuente_vidas.render("Vidas:", True, BLANCO)
            vidas_contador_texto = self.fuente_vidas.render(str(self.vidas), True, self.color_variable_vida) #varia color de la vida segun cantidad
            vidas_posicion = (120,5)

            texto_rect1 = pregunta.get_rect(center=(200 + 400 // 2, 10 + 50 // 2))
            texto_rect2 = respuesta_a.get_rect(center=(50 + 200 // 2, 500 + 50 // 2))
            texto_rect3 = respuesta_b.get_rect(center=(300 + 200 // 2, 500 + 50 // 2))
            texto_rect4 = respuesta_c.get_rect(center=(550 + 200 // 2, 500 + 50 // 2))

            self.screen.blit(pregunta,texto_rect1)
            self.screen.blit(respuesta_a,texto_rect2)
            self.screen.blit(respuesta_b,texto_rect3)
            self.screen.blit(respuesta_c,texto_rect4)
            self.screen.blit(vidas_contador_texto,vidas_posicion)
            self.screen.blit(vidas_contador_texto,vidas_posicion)
            self.screen.blit(vidas_texto,(0,5))
            
        else:
            self.escena = "Ganaste"

    def eventos_menu(self):
        '''
        Toma eventos, click de la respuesta correcta y recuenta vidas.
        '''
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
                            self.puntaje += 10
                        else:
                            self.vidas -= 1
                            if self.vidas == 0:
                                self.escena = 'Perdiste'

    def cambio_color_vidas(self):
        '''
        Toma las vidas del jugador y segun su cantidad blitea un color diferente.
        '''
        if self.vidas == 2:
            self.color_variable_vida = BLANCO
        elif self.vidas == 1:
            self.color_variable_vida = ROJO


    def iniciar_juego(self):
        '''
        Metodo para inicializar el menú.
        Utiliza las dos funciones, render y el lector de eventos.
        '''
        self.render_menu()
        self.cambio_color_vidas()
        self.eventos_menu()
        


class Perdiste():
    def __init__(self,screen,puntaje):
        self.rect_1 = pygame.Rect(0,500,100,50)#puntaje
        self.rect_2 = pygame.Rect(200,500,100,50)#puntos
        self.rect_3 = pygame.Rect(10,200,100,50)#nombre
        self.rect_4 = pygame.Rect(320,200,100,50)#input_nombre
        self.rect_5 = pygame.Rect(600,500,100,40)#atras
        self.rect_6 = pygame.Rect(200,10,100,40)#perdiste!
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial\mult\img\perdiste_background.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (1000, 700))
        self.fuente = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 36)
        self.fuente_grande = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 70)
        self.escena = "Perdiste"
        self.screen = screen
        self.puntaje = puntaje
        self.user_text = ""

    def render_perdiste(self):
        puntaje = self.fuente.render('PUNTAJE:', True, BLANCO)
        puntos = self.fuente.render(str(self.puntaje), True, BLANCO)
        nombre = self.fuente.render('Ingrese nombre: ', True, BLANCO)
        atras = self.fuente.render('ATRAS', True, BLANCO)
        texto_perdiste = self.fuente_grande.render('¡PERDISTE!', True, ROJO)
        texto_escrito = self.fuente.render(self.user_text,True,NEGRO,ROJO)
        #Ubicacion de los botones
        texto_rect1 = self.rect_1#puntaje
        texto_rect2 = self.rect_2#puntos
        texto_rect3 = self.rect_3 #nombre
        texto_rect4 = self.rect_4#input_nombre
        texto_rect5 = self.rect_5#atras
        texto_rect6 = self.rect_6

        #Muestra botones y texto
        self.screen.blit(self.imagen_fondo,(0,0))
        self.screen.blit(puntaje,texto_rect1)
        self.screen.blit(puntos,texto_rect2)
        self.screen.blit(nombre,texto_rect3)
        self.screen.blit(atras,texto_rect5)
        self.screen.blit(texto_perdiste,texto_rect6)
        self.screen.blit(texto_escrito,texto_rect4)
        print(self.user_text)
    def eventos_perdiste(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()  
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    if(colision_boton(evento,self.rect_5)):
                        self.escena = 'Menu'
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                else:
                        self.user_text += evento.unicode
    def inicio_perdiste(self):
        self.render_perdiste()
        self.eventos_perdiste()

class Ganaste():
    def __init__(self):
        pass  
