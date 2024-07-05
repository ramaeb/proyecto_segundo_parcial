import pygame
import sys
from constantes import *
import json
import csv
import datetime

pygame.init()
corriendo = True
escribiendo = False
indice = 0
vidas_perdidas = 0
nombre_jugador = ''
lista_prueba = []

ruta_preguntas = 'proyecto_segundo_parcial/datos/preguntas.csv'
datos = []
with open(ruta_preguntas, mode = 'r') as arhivo:
    lectura = csv.DictReader(arhivo)

    for fila in lectura:
        datos.append(dict(fila))

try:
    with open('jugadores.json', 'r') as archivo:
        datos_jugadores = json.load(archivo)
except FileNotFoundError:
    # Si el archivo no existe, se crea una lista vacía
    datos_jugadores = []

def agrega_diccioarios_a_lista(lista_diccionarios: list, lista_a_agregar: list):
    for item in lista_a_agregar:
        lista_diccionarios.append(item)
    return lista_diccionarios

def formatea_diccionarios_a_str(lista_diccionarios: list):
    if len(lista_diccionarios) > 0:
        lista_final = []
        for item in lista_diccionarios:
            texto_aux = ''
            for clave,valor in item.items():
                texto_aux += '|{}: {}|'.format(clave,valor)
            lista_final.append(texto_aux)
        return lista_final
    else:
        return False
    



def comprueba_click(mouse_pos, rect):
    retorno = False
    if (mouse_pos[0] > rect.left and mouse_pos[0] < rect.right) and (mouse_pos[1] < rect.bottom and 
                                                                    mouse_pos[1] > rect.top):
        retorno = True
    return retorno 

def mostrar_menu_principal():
    global corriendo
    global escena

    rect_1 = pygame.Rect(300,30,200,100)
    rect_2 = pygame.Rect(300,450,200,100)
    rect_3 = pygame.Rect(83,500,100,50)
    rect_4 = pygame.Rect(616,500,100,50)

    fuente = pygame.font.Font(None, 37)
    #fuente = pygame.font.SysFont('Eras ITC',36)
    texto = fuente.render('PREGUNTADOS', True, ROJO)
    texto_rect = texto.get_rect(center=(300 + 200 // 2, 30 + 100 // 2))
    texto2 = fuente.render('INICIAR', True, ROJO)
    texto_rect2 = texto2.get_rect(center=(300 + 200 // 2, 450 + 100 // 2))
    texto3 = fuente.render('Top 10 partidas', True, ROJO)
    texto_rect3 = texto3.get_rect(center=(83 + 100 // 2, 500 + 50 // 2))
    texto4 = fuente.render('Fin', True, ROJO)
    texto_rect4 = texto4.get_rect(center=(616 + 100 // 2, 500 + 50 // 2))

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                mouse_pos = evento.pos
                if(comprueba_click(mouse_pos,rect_2)):
                    escena = 'iniciar_juego'
                elif(comprueba_click(mouse_pos,rect_3)):
                    escena = 'top_10_partidas'
                elif(comprueba_click(mouse_pos,rect_4)):
                    escena = 'fin'

    pantalla.blit(fondo_redimensionado, (0,0))

    pygame.draw.rect(pantalla,AZUL,rect_1)
    pygame.draw.rect(pantalla,AZUL,rect_2)
    pygame.draw.rect(pantalla,AZUL,rect_3)
    pygame.draw.rect(pantalla,AZUL,rect_4)

    pantalla.blit(texto,texto_rect)
    pantalla.blit(texto2,texto_rect2)
    pantalla.blit(texto3,texto_rect3)
    pantalla.blit(texto4,texto_rect4)

def mostrar_top_10_partidas(lista_top_10: list):
    global corriendo
    global escena

    rect_1 = pygame.Rect(0,0,800,54.54)
    rect_2 = pygame.Rect(0,54.54,800,54.54)
    rect_3 = pygame.Rect(0,109.08,800,54.54)
    rect_4 = pygame.Rect(0,163.62,800,54.54)
    rect_5 = pygame.Rect(0,218.16,800,54.540)
    rect_6 = pygame.Rect(0,272.7,800,54.540)
    rect_7 = pygame.Rect(0,327.24,800,54.54)
    rect_8 = pygame.Rect(0,381.78,800,54.54)
    rect_9 = pygame.Rect(0,436.32,800,54.540)
    rect_10 = pygame.Rect(0,490.86,800,54.54)
    rect_11 = pygame.Rect(0,545.4,800,54.54)

    fuente = pygame.font.Font(None, 37)
    #fuente = pygame.font.SysFont('Eras ITC',36)
    texto = fuente.render('partida1', True, ROJO)
    texto_rect = texto.get_rect(center=(0 + 800 // 2, 0 + 54.54 // 2))
    texto2 = fuente.render('partida2', True, ROJO)
    texto_rect2 = texto2.get_rect(center=(0 + 800 // 2, 54.54 + 54.54 // 2))
    texto3 = fuente.render('partida3', True, ROJO)
    texto_rect3 = texto3.get_rect(center=(0 + 800 // 2, 109.08 + 54.54 // 2))
    texto4 = fuente.render('partida4', True, ROJO)
    texto_rect4 = texto4.get_rect(center=(0 + 800 // 2, 163.62 + 54.54 // 2))
    texto5 = fuente.render('partida5', True, ROJO)
    texto_rect5 = texto5.get_rect(center=(0 + 800 // 2, 218.16 + 54.54 // 2))
    texto6 = fuente.render('partida6', True, ROJO)
    texto_rect6 = texto6.get_rect(center=(0 + 800 // 2, 272.7 + 54.54 // 2))
    texto7 = fuente.render('partida7', True, ROJO)
    texto_rect7 = texto7.get_rect(center=(0 + 800 // 2, 327.24 + 54.54 // 2))
    texto8 = fuente.render('partida8', True, ROJO)
    texto_rect8 = texto8.get_rect(center=(0 + 800 // 2, 381.78 + 54.54 // 2))
    texto9 = fuente.render('partida9', True, ROJO)
    texto_rect9 = texto9.get_rect(center=(0 + 800 // 2, 436.32 + 54.54 // 2))
    texto10 = fuente.render('partida10', True, ROJO)
    texto_rect10 = texto10.get_rect(center=(0 + 800 // 2, 490.86 + 54.54 // 2))
    texto11 = fuente.render('ATRAS', True, ROJO)
    texto_rect11 = texto11.get_rect(center=(0 + 800 // 2, 545.4 + 54.54 // 2))

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            corriendo = False  
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                mouse_pos = evento.pos
                if(comprueba_click(mouse_pos,rect_11)):
                    escena = 'menu_principal'  
    
    pantalla.blit(fondo_redimensionado, (0,0))
    pygame.draw.rect(pantalla,AZUL,rect_1)
    pygame.draw.rect(pantalla,NEGRO,rect_2)
    pygame.draw.rect(pantalla,NEGRO,rect_3)
    pygame.draw.rect(pantalla,NEGRO,rect_4)
    pygame.draw.rect(pantalla,NEGRO,rect_5)
    pygame.draw.rect(pantalla,NEGRO,rect_6)
    pygame.draw.rect(pantalla,NEGRO,rect_7)
    pygame.draw.rect(pantalla,NEGRO,rect_8)
    pygame.draw.rect(pantalla,NEGRO,rect_9)
    pygame.draw.rect(pantalla,NEGRO,rect_10)
    pygame.draw.rect(pantalla,AZUL,rect_11)
    y = 0  # Posición vertical inicial
    for texto in lista_top_10:
        pantalla.blit(texto, (0, y))
        y += 54.54  # Incrementar la posición vertical para el próximo texto
    pantalla.blit(texto11,texto_rect11)

def mostrar_ganaste():
    global corriendo
    global escena
    global escribiendo
    global nombre_jugador

    datos_jugador = {}

    rect_1 = pygame.Rect(100,10,100,50)
    rect_2 = pygame.Rect(215,10,100,50)
    rect_3 = pygame.Rect(100,70,100,50)
    rect_4 = pygame.Rect(215,70,100,50)
    rect_5 = pygame.Rect(600,500,100,40)

    pantalla.blit(fondo_redimensionado, (0,0))
    pygame.draw.rect(pantalla,NEGRO,rect_1)
    pygame.draw.rect(pantalla,NEGRO,rect_2)
    pygame.draw.rect(pantalla,NEGRO,rect_3)
    pygame.draw.rect(pantalla,NEGRO,rect_4)
    pygame.draw.rect(pantalla,NEGRO,rect_5)

    fuente = pygame.font.Font(None, 37)
    puntaje = fuente.render('PUNTAJE:', True, ROJO)
    puntos = fuente.render('80', True, ROJO)
    nombre = fuente.render('NOMBRE:', True, ROJO)
    entrada_nombre = fuente.render(nombre_jugador, True, ROJO)
    atras = fuente.render('ATRAS', True, ROJO)
    texto_rect1 = puntaje.get_rect(center=(100 + 100 // 2, 10 + 50 // 2))
    texto_rect2 = puntos.get_rect(center=(215 + 100 // 2, 10 + 50 // 2))
    texto_rect3 = nombre.get_rect(center=(100 + 70 // 2, 70 + 50 // 2))
    texto_rect4 = entrada_nombre.get_rect(center=(215 + 100 // 2, 70 + 50 // 2))
    texto_rect5 = atras.get_rect(center=(600 + 100 // 2, 500 + 40 // 2))
    pantalla.blit(puntaje,texto_rect1)
    pantalla.blit(puntos,texto_rect2)
    pantalla.blit(nombre,texto_rect3)
    pantalla.blit(entrada_nombre,texto_rect4)
    pantalla.blit(atras,texto_rect5)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            corriendo = False  
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                mouse_pos = evento.pos
                if(comprueba_click(mouse_pos,rect_5)):
                    escena = 'menu_principal'
                elif(comprueba_click(mouse_pos,rect_4)):
                    print('rect_4')
                    escribiendo = True
        elif evento.type == pygame.KEYDOWN and escribiendo:
            if evento.key == pygame.K_BACKSPACE:
                nombre_jugador = nombre_jugador[:-1]
            elif evento.key == pygame.K_RETURN:
                datos_jugador['nombre'] = nombre_jugador        # agrega valores al diccionario
                datos_jugador['puntaje'] = 80
                fecha_actual = datetime.datetime.now()  # pide fecha
                fecha_actual = str(fecha_actual)
                datos_jugador['fecha'] = fecha_actual
                lista_prueba.append(datos_jugador)
                print("Nombre ingresado:", nombre_jugador)
                nombre_jugador = ''
                datos_jugadores = agrega_diccioarios_a_lista(datos_jugadores,lista_prueba)
                escena = 'menu_principal'
            else:
                print(evento.unicode)
                nombre_jugador += evento.unicode


def mostrar_perdiste(datos_jugadores: list):
    global corriendo
    global escena
    global escribiendo
    global nombre_jugador

    datos_jugador = {}

    rect_1 = pygame.Rect(100,10,100,50)
    rect_2 = pygame.Rect(215,10,100,50)
    rect_3 = pygame.Rect(100,70,100,50)
    rect_4 = pygame.Rect(215,70,100,50)
    rect_5 = pygame.Rect(600,500,100,40)

    pantalla.blit(fondo_redimensionado, (0,0))
    pygame.draw.rect(pantalla,NEGRO,rect_1)
    pygame.draw.rect(pantalla,NEGRO,rect_2)
    pygame.draw.rect(pantalla,NEGRO,rect_3)
    pygame.draw.rect(pantalla,NEGRO,rect_4)
    pygame.draw.rect(pantalla,NEGRO,rect_5)

    fuente = pygame.font.Font(None, 37)
    puntaje = fuente.render('PUNTAJE:', True, ROJO)
    puntos = fuente.render('80', True, ROJO)
    nombre = fuente.render('NOMBRE:', True, ROJO)
    entrada_nombre = fuente.render(nombre_jugador, True, ROJO)
    atras = fuente.render('ATRAS', True, ROJO)
    texto_rect1 = puntaje.get_rect(center=(100 + 100 // 2, 10 + 50 // 2))
    texto_rect2 = puntos.get_rect(center=(215 + 100 // 2, 10 + 50 // 2))
    texto_rect3 = nombre.get_rect(center=(100 + 70 // 2, 70 + 50 // 2))
    texto_rect4 = entrada_nombre.get_rect(center=(215 + 100 // 2, 70 + 50 // 2))
    texto_rect5 = atras.get_rect(center=(600 + 100 // 2, 500 + 40 // 2))
    pantalla.blit(puntaje,texto_rect1)
    pantalla.blit(puntos,texto_rect2)
    pantalla.blit(nombre,texto_rect3)
    pantalla.blit(entrada_nombre,texto_rect4)
    pantalla.blit(atras,texto_rect5)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            corriendo = False  
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                mouse_pos = evento.pos
                if(comprueba_click(mouse_pos,rect_5)):
                    escena = 'menu_principal'
                elif(comprueba_click(mouse_pos,rect_4)):
                    print('rect_4')
                    escribiendo = True
        elif evento.type == pygame.KEYDOWN and escribiendo:
            if evento.key == pygame.K_BACKSPACE:
                nombre_jugador = nombre_jugador[:-1]
            elif evento.key == pygame.K_RETURN:
                datos_jugador['nombre'] = nombre_jugador        # agrega valores al diccionario
                datos_jugador['puntaje'] = 80
                fecha_actual = datetime.datetime.now()  # pide fecha
                fecha_actual = str(fecha_actual)
                datos_jugador['fecha'] = fecha_actual
                lista_prueba.append(datos_jugador)
                print("Nombre ingresado:", nombre_jugador)
                nombre_jugador = ''
                datos_jugadores = agrega_diccioarios_a_lista(datos_jugadores,lista_prueba)
                escena = 'menu_principal'
            else:
                print(evento.unicode)
                nombre_jugador += evento.unicode
    
    

def mostrar_inciciar_juego(lista_datos: list):
    global corriendo
    global escena
    global indice
    global vidas_perdidas 

    rect_1 = pygame.Rect(200,10,400,50)
    rect_2 = pygame.Rect(50,500,200,50)
    rect_3 = pygame.Rect(300,500.08,200,50)
    rect_4 = pygame.Rect(550,500.62,200,50)

    if indice < len(lista_datos):
        dato = lista_datos[indice]

        pantalla.blit(fondo_redimensionado, (0,0))
        pygame.draw.rect(pantalla,NEGRO,rect_1)
        pygame.draw.rect(pantalla,NEGRO,rect_2)
        pygame.draw.rect(pantalla,NEGRO,rect_3)
        pygame.draw.rect(pantalla,NEGRO,rect_4)

        fuente = pygame.font.Font(None, 37)

        pregunta = fuente.render(dato['pregunta'], True, ROJO)
        respuesta_a = fuente.render(dato['respuesta_a'], True, ROJO)
        respuesta_b = fuente.render(dato['respuesta_b'], True, ROJO)
        respuesta_c = fuente.render(dato['respuesta_c'], True, ROJO)
        texto_rect1 = pregunta.get_rect(center=(200 + 400 // 2, 10 + 50 // 2))
        texto_rect2 = respuesta_a.get_rect(center=(50 + 200 // 2, 500 + 50 // 2))
        texto_rect3 = respuesta_b.get_rect(center=(300 + 200 // 2, 500 + 50 // 2))
        texto_rect4 = respuesta_c.get_rect(center=(550 + 200 // 2, 500 + 50 // 2))
        pantalla.blit(pregunta,texto_rect1)
        pantalla.blit(respuesta_a,texto_rect2)
        pantalla.blit(respuesta_b,texto_rect3)
        pantalla.blit(respuesta_c,texto_rect4)

        pygame.display.flip()
    
    else:
        escena = 'ganaste'

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            corriendo = False  
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                mouse_pos = evento.pos
                respuesta = None  # Inicializar respuesta
                if(comprueba_click(mouse_pos,rect_2)):
                    respuesta = 'a'
                elif(comprueba_click(mouse_pos,rect_3)):
                    respuesta = 'b'
                elif(comprueba_click(mouse_pos,rect_4)):
                    respuesta = 'c'

                print(respuesta)

                if respuesta is not None:
                    if respuesta == dato['respuesta_correcta']:
                        indice += 1
                        #print(indice)
                    else:
                        vidas_perdidas += 1
                        print(vidas_perdidas)
                        if vidas_perdidas == 3:
                            escena = 'perdiste'


pantalla = pygame.display.set_mode((800, 600))

fondo = pygame.image.load('proyecto_segundo_parcial\mult\img\preguntados_background.jpg')
fondo_redimensionado = pygame.transform.scale(fondo, (800, 600))

escena = 'menu_principal'

while corriendo:

    if escena == 'menu_principal':
        indice = 0
        vidas_perdidas = 0
        mostrar_menu_principal()
    elif escena == 'iniciar_juego':
        mostrar_inciciar_juego(datos)
    elif escena == 'top_10_partidas':
        lista_textos = formatea_diccionarios_a_str(datos_jugadores)
        textos_renderizados = renderiza_lista_textos(lista_textos)
        mostrar_top_10_partidas(textos_renderizados)
    elif escena == 'perdiste':
        mostrar_perdiste(datos_jugadores)
    elif escena =='ganaste':
        mostrar_ganaste()
    elif escena == 'fin':
        corriendo = False

    pygame.display.flip()
print()
print(lista_prueba)
pygame.quit()
sys.exit()