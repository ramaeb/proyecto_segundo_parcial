#-*- coding: utf-8 -*-
import pygame
from funciones import *
import time
TIEMPO_LIMITE = 30

class MenuPrincipal():

    '''
    Escena de menu principal
    '''
    def __init__(self, screen):
        self.screen = screen
        self.escena = "Menu"
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial/mult/img/preguntados_background.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (800, 600))
        self.boton_inicio, self.text_rect, self.text_surface = crea_boton(300, 370, 200, 70, "Inicio")#Boton inicio
        self.boton_salida, self.text_rect_2, self.text_surface_2 = crea_boton(300, 500, 200, 70, "Salida")#Boton salida
        self.boton_config, self.text_rect_3, self.text_surface_3 = crea_boton(600, 0, 200, 70, "Config")#Boton config
        self.boton_top10, self.text_rect_4, self.text_surface_4 = crea_boton(0, 0, 200, 70, "Top10")#Boton top10
        self.sonido_inicio = pygame.mixer.Sound("proyecto_segundo_parcial\mult\sonido\inicio_efecto.mp3")
        self.sonido_inicio.set_volume(0.2)
        self.sonido_inicio.play(loops=0)
        self.corriendo = True

    def subir_volumen(self):
        # Sube el volumen en 0.1 unidades, máximo 1.0
        nuevo_volumen = min(2.0, pygame.mixer.music.get_volume() + 0.1)
        pygame.mixer.music.set_volume(nuevo_volumen)
        print("Su volumen subio:{}" .format(nuevo_volumen))

    def bajar_volumen(self):
        # Baja el volumen en 0.1 unidades, mínimo 0.0
        nuevo_volumen = max(0.0, pygame.mixer.music.get_volume() - 0.1)
        pygame.mixer.music.set_volume(nuevo_volumen)
        print("Su volumen bajo:{}".format(nuevo_volumen))

    def render_menu(self):
        '''
        Hace el render de todos los botones SALIDA E INICIO
        '''
        self.screen.blit(self.imagen_fondo,(0,0))
        draw.rect(self.screen,(116, 191, 64),self.boton_inicio,0,10,10)#Boton inicio
        draw.rect(self.screen,(248, 41, 51),self.boton_salida,0,10,10)#Boton salida (despues del 0 parametros para redondeo del boton)
        draw.rect(self.screen,GRIS,self.boton_config,0,10,10)#boton config
        draw.rect(self.screen,NARANJA,self.boton_top10,0,10,10)#boton top 10
        self.screen.blit(self.text_surface, self.text_rect)
        self.screen.blit(self.text_surface_2, self.text_rect_2)
        self.screen.blit(self.text_surface_3, self.text_rect_3)
        self.screen.blit(self.text_surface_4, self.text_rect_4)


    def eventos_menu(self):
        '''
        Lee los eventos que van pasando por el menú
        La colision del mouse con los botones.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.corriendo = False
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
                        self.corriendo = False
                    elif colision_boton(event,self.boton_top10):
                        self.escena = "Top10Partidas"
                    elif colision_boton(event,self.boton_top10):
                        self.escena = "Config"
    
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
        self.lista_datos = leer_csv('proyecto_segundo_parcial/datos/preguntas.csv')
        self.indice = 0
        self.vidas = 3
        self.puntaje = 0
        self.rect_1 = pygame.Rect(150,10,500,50)
        self.rect_2 = pygame.Rect(50,500,200,50)
        self.rect_3 = pygame.Rect(300,500.08,200,50)
        self.rect_4 = pygame.Rect(550,500.62,200,50)
        self.rect_5 = pygame.Rect(10,100.62,200,50)
        self.escena = "Inicio"
        self.start_time = time.time()#Tiempo inicial
        self.tiempo_corriendo = time.time() #Tiempo transcurrido

        
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

            #tiempoooo
    
            self.tiempo_corriendo = time.time() - self.start_time
            self.tiempo_restante = max(TIEMPO_LIMITE - self.tiempo_corriendo, 0)
            self.calculo_tiempo = self.tiempo_corriendo - self.start_time
            self.texto_tiempo = self.fuente.render(f"Tiempo restante:{self.tiempo_restante:.1f} segundos ", True , BLANCO)
            self.screen.blit(self.texto_tiempo, (60, 60))
            print(self.tiempo_corriendo)
            

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
    
            if self.tiempo_restante <= 0:
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
        self.rect_4 = pygame.Rect(320,200,1000,50)#input_nombre
        self.rect_5 = pygame.Rect(400,500,100,40)#atras
        self.rect_6 = pygame.Rect(200,10,100,40)#perdiste!
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial\mult\img\perdiste_background.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (1000, 700))
        self.fuente = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 36)
        self.fuente_grande = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 70)
        self.escena = "Perdiste"
        self.screen = screen
        self.puntaje = puntaje
        self.nombre_jugador = "Click, enter para ingresar."
        self.toque_caja_input = False
        self.datos_jugadores = []
        self.enter = False
        self.contador = 0

    def render_perdiste(self):
        puntaje = self.fuente.render('PUNTAJE:', True, BLANCO)
        puntos = self.fuente.render(str(self.puntaje), True, BLANCO)
        nombre = self.fuente.render('Ingrese nombre: ', True, BLANCO)
        atras = self.fuente.render('', True, BLANCO,BLANCO)
        texto_perdiste = self.fuente_grande.render('¡PERDISTE!', True, ROJO)
        texto_escrito = self.fuente.render(self.nombre_jugador,True,NEGRO,ROJO)
        #Ubicacion de los botones
        texto_rect1 = self.rect_1#puntaje
        texto_rect2 = self.rect_2#puntos
        texto_rect3 = self.rect_3 #nombre
        texto_rect4 = self.rect_4
        texto_rect5 = self.rect_5#atras
        texto_rect6 = self.rect_6
        pygame.draw.rect(self.screen,NEGRO,self.rect_4)

        #Muestra botones y texto
        self.screen.blit(self.imagen_fondo,(0,0))
        self.screen.blit(puntaje,texto_rect1)
        self.screen.blit(puntos,texto_rect2)
        self.screen.blit(nombre,texto_rect3)
        self.screen.blit(atras,texto_rect5)
        self.screen.blit(texto_perdiste,texto_rect6)
        self.screen.blit(texto_escrito,texto_rect4)

    def crea_dict_datos_jugador(self,lista_jugadores:list):
        diccionario_datos = {}
        diccionario_datos['nombre'] = self.nombre_jugador        # agrega valores al diccionario
        diccionario_datos['puntaje'] = self.puntaje
        fecha_actual = datetime.datetime.now().date().strftime('%d/%m/%Y')  #pide fecha
        diccionario_datos['fecha'] = fecha_actual
        
        lista_jugadores.append(diccionario_datos)
        self.datos_jugadores = lista_jugadores
        return lista_jugadores

    def eventos_perdiste(self):
        '''
        Input de nombre
        '''
        self.enter = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()  
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    if colision_boton(evento,self.rect_4):
                        print("HOLA")
                        self.nombre_jugador = ""
                        self.toque_caja_input = True #variable tocar click
    
            elif evento.type == pygame.KEYDOWN and self.toque_caja_input:
                if evento.key == pygame.K_BACKSPACE:
                        self.nombre_jugador = self.nombre_jugador[:-1]
                elif evento.key == pygame.K_RETURN:
                        self.escena = "Menu"
                        self.datos_jugadores = self.crea_dict_datos_jugador(self.datos_jugadores)
                        self.nombre_jugador = "Click, enter para ingresar."
                        self.contador = 0
                else:
                        self.nombre_jugador += evento.unicode

    def inicio_perdiste(self):
        self.render_perdiste()
        self.eventos_perdiste()

class Ganaste():
    def __init__(self,screen,puntaje):
        self.rect_1 = pygame.Rect(0,500,100,50)#puntaje
        self.rect_2 = pygame.Rect(200,500,100,50)#puntos
        self.rect_3 = pygame.Rect(10,200,100,50)#nombre
        self.rect_4 = pygame.Rect(320,200,1000,50)#input_nombre
        self.rect_5 = pygame.Rect(400,500,100,40)#atras
        self.rect_6 = pygame.Rect(200,10,100,40)#perdiste!
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial\mult\img\ganaste.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (1000, 700))
        self.fuente = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 36)
        self.fuente_grande = pygame.font.Font("proyecto_segundo_parcial/mult/font/pixel_art_font.ttf", 70)
        self.escena = "Ganaste"
        self.screen = screen
        self.puntaje = puntaje
        self.nombre_jugador = "Click, enter para ingresar."
        self.toque_caja_input = False
        self.datos_jugadores = []
    
    def render_ganaste(self):
        puntaje = self.fuente.render('PUNTAJE:', True, BLANCO)
        puntos = self.fuente.render(str(self.puntaje), True, BLANCO)
        nombre = self.fuente.render('Ingrese nombre: ', True, BLANCO)
        atras = self.fuente.render('', True, BLANCO,BLANCO)
        texto_perdiste = self.fuente_grande.render('¡GANASTE!', True, VERDE)
        texto_escrito = self.fuente.render(self.nombre_jugador,True,NEGRO,ROJO)
        #Ubicacion de los botones
        texto_rect1 = self.rect_1#puntaje
        texto_rect2 = self.rect_2#puntos
        texto_rect3 = self.rect_3 #nombre
        texto_rect4 = self.rect_4
        texto_rect5 = self.rect_5#atras
        texto_rect6 = self.rect_6
        pygame.draw.rect(self.screen,NEGRO,self.rect_4)

        #Muestra botones y texto
        self.screen.blit(self.imagen_fondo,(0,0))
        self.screen.blit(puntaje,texto_rect1)
        self.screen.blit(puntos,texto_rect2)
        self.screen.blit(nombre,texto_rect3)
        self.screen.blit(atras,texto_rect5)
        self.screen.blit(texto_perdiste,texto_rect6)
        self.screen.blit(texto_escrito,texto_rect4)

    def crea_dict_datos_jugador(self,lista_jugadores:list):
        diccionario_datos = {}
        diccionario_datos['nombre'] = self.nombre_jugador        # agrega valores al diccionario
        diccionario_datos['puntaje'] = self.puntaje
        fecha_actual = datetime.datetime.now().date().strftime('%d/%m/%Y')  #pide fecha
        diccionario_datos['fecha'] = fecha_actual
        
        lista_jugadores.append(diccionario_datos)
        self.datos_jugadores = lista_jugadores
        return lista_jugadores

    def eventos_ganaste(self):
        '''
        Input de nombre
        '''
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()  
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    if colision_boton(evento,self.rect_4):
                        print("HOLA")
                        self.nombre_jugador = ""
                        self.toque_caja_input = True #variable tocar click
    
            elif evento.type == pygame.KEYDOWN and self.toque_caja_input:
                if evento.key == pygame.K_BACKSPACE:
                        self.nombre_jugador = self.nombre_jugador[:-1]
                elif evento.key == pygame.K_RETURN:
                        self.escena = "Menu"
                        self.datos_jugadores = self.crea_dict_datos_jugador(self.datos_jugadores)
                        print(self.datos_jugadores)
                        self.nombre_jugador = "Click, enter para ingresar."
                else:
                        self.nombre_jugador += evento.unicode

    def inicio_ganaste(self):
        self.render_ganaste()
        self.eventos_ganaste()


class Configuracion():
    def __init__(self):
        pass

class Top10Partidas():
    '''
    Falta ordenar el TOP10
    '''
    def __init__(self,screen):
        self.lista_jugadores = []
        self.lista_jugadores_parajson = []
        self.screen = screen
        self.escena = "Top10Partidas"
        self.rect_1 = pygame.Rect(0,0,800,54.54)
        self.rect_2 = pygame.Rect(0,54.54,800,54.54)
        self.rect_3 = pygame.Rect(0,109.08,800,54.54)
        self.rect_11 = pygame.Rect(0,545.4,800,54.54)

        self.fuente = pygame.font.Font(None, 37)
        #fuente = pygame.font.SysFont('Eras ITC',36)
        texto = self.fuente.render('partida1', True, ROJO)
        self.texto_rect = texto.get_rect(center=(0 + 800 // 2, 0 + 54.54 // 2))
        self.texto2 = self.fuente.render('partida2', True, ROJO)
        self.texto_rect2 = self.texto2.get_rect(center=(0 + 800 // 2, 54.54 + 54.54 // 2))
        self.texto3 = self.fuente.render('NO HAY PARTIDAS PARA TOP 10', True, ROJO)
        self.texto_rect3 = self.texto3.get_rect(center=(0 + 800 // 2, 109.08 + 54.54 // 2))
        self.texto11 = self.fuente.render('ATRAS', True, ROJO)
        self.texto_rect11 = self.texto11.get_rect(center=(0 + 800 // 2, 545.4 + 54.54 // 2))

    def eventos_top10(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()  
            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    if(colision_boton(evento,self.rect_11)):
                        self.escena = 'Menu'

    def render_top10(self):
        self.screen.fill(NEGRO)
        pygame.draw.rect(self.screen,NEGRO,self.rect_11)
        y = 0  # Posición vertical inicial
        if len(self.lista_jugadores) < 1:
            self.screen.blit(self.texto3,(0,100))
            self.screen.blit(self.texto11,self.texto_rect11)
            self.lista_jugadores = self.lista_jugadores[0:11]
        else:
            self.ordena_lista_maximo()
            textos_renderizados = self.renderiza_lista_textos()
            for texto in textos_renderizados:
                self.screen.blit(texto, (0, y))
                y += 54.54  # Incrementar la posición vertical para el próximo texto
            self.screen.blit(self.texto11,self.texto_rect11)
    
    def ordena_lista_maximo(self):
        for i in range(len(self.lista_jugadores)):
            for j in range(i + 1,len(self.lista_jugadores)):
                if self.lista_jugadores[i]['puntaje'] < self.lista_jugadores[j]['puntaje']:
                    aux = self.lista_jugadores[i]
                    self.lista_jugadores[i] = self.lista_jugadores[j]
                    self.lista_jugadores[j] = aux

    def renderiza_lista_textos(self):
        '''
        Hace un render de los textos para mostrarlos en pantalla.
        '''
        lista_textos_renderizados = []
        lista_jugadores_texto = self.formatea_diccionarios_a_str() 
        for texto in lista_jugadores_texto:
            texto_renderizado = self.fuente.render(texto,True,ROJO)
            lista_textos_renderizados.append(texto_renderizado)
        return lista_textos_renderizados
    
    def formatea_diccionarios_a_str(self):
        '''
        Formatea la listas de diccionarios a un string grande.
        '''
        if len(self.lista_jugadores) > 0:
            lista_final = []
            for item in self.lista_jugadores:
                texto_aux = ''
                for clave,valor in item.items():
                    texto_aux += '|{}: {}|'.format(clave,valor)
                lista_final.append(texto_aux)
            return lista_final

    def inicio_top10(self):
        self.eventos_top10()
        self.render_top10()