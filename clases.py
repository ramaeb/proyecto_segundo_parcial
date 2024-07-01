import pygame
from funciones import *


class MenuPrincipal():

    '''
    Escena de menu principal
    '''
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.escena = "Menu"
        self.imagen_fondo = pygame.image.load('proyecto_segundo_parcial/mult/img/preguntados_background.jpg')
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (800, 600))
        self.boton_inicio, self.text_rect, self.text_surface = crea_boton(300, 370, 200, 70, "Inicio")
        self.boton_salida, self.text_rect_2, self.text_surface_2 = crea_boton(300, 500, 200, 70, "Salida")
        self.sonido_inicio = pygame.mixer.Sound("proyecto_segundo_parcial/mult/img/sonido/inicio_efecto.mp3")
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
        pygame.mixer.music.load("proyecto_segundo_parcial\mult\img\sonido\musica_fondo.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)

    def render_menu(self):
        pygame.mixer.init()
        self.screen.fill((253, 87, 34))
        text_rect,text_surface = crea_texto("De que color es ?")
        self.screen.blit(text_surface,text_rect)
        print("Estoy en inicio")
        
        
    
    def eventos_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def iniciar_juego(self):
        '''
        Metodo para inicializar el menú.
        Utiliza las dos funciones, render y el lector de eventos.
        '''
        self.render_menu()
        self.eventos_menu()

class Boton(pygame.sprite.Sprite):
    '''
    Se lo trata como un sprite para que despues
    le podamos hacer un "KILL" y seguir con las funciones.
    '''